#!/usr/bin/env python3
"""Beat-grid / breathing-point analysis for the generated soothing BGM.

Outputs (stdout, JSON):
  - duration, sample rate, channels
  - rms envelope (50ms hop) summary + 0.25s grid
  - onset envelope peaks (gentle onsets = phrase starts / swell starts)
  - breathing points (local RMS minima with min spacing = musical breaths)
  - tempo estimate (autocorrelation of onset envelope, 30-180 BPM)
"""
import json
import sys

import numpy as np
import soundfile as sf

PATH = sys.argv[1]

data, sr = sf.read(PATH, always_2d=True)
mono = data.mean(axis=1)
dur = len(mono) / sr

hop = 2048          # 64ms at 32k
win = 4096          # 128ms window
n_frames = 1 + (len(mono) - win) // hop

# --- RMS envelope ---
rms = np.zeros(n_frames, dtype=np.float64)
for i in range(n_frames):
    seg = mono[i * hop : i * hop + win]
    rms[i] = float(np.sqrt(np.mean(seg * seg))) if len(seg) else 0.0
rms_db = 20.0 * np.log10(np.maximum(rms, 1e-9))
t_rms = np.arange(n_frames) * hop / sr

# --- spectral flux onset envelope ---
n_fft = 2048
flux = np.zeros(n_frames, dtype=np.float64)
prev_mag = None
for i in range(n_frames):
    seg = mono[i * hop : i * hop + n_fft]
    if len(seg) < n_fft:
        break
    windowed = seg * np.hanning(n_fft)
    mag = np.abs(np.fft.rfft(windowed))
    if prev_mag is not None:
        d = mag - prev_mag
        flux[i] = float(np.sum(d[d > 0]))
    prev_mag = mag

# smooth flux (3-frame moving avg)
kernel = np.ones(3) / 3.0
flux_s = np.convolve(flux, kernel, mode="same")

def smooth(x, k):
    return np.convolve(x, np.ones(k) / k, mode="same")

# --- breathing points: local minima of smoothed RMS, min spacing 0.9s ---
rms_smooth = smooth(rms, 9)  # ~0.58s smoothing
min_gap = int(0.9 / (hop / sr))
breaths = []
for i in range(2, n_frames - 2):
    window = rms_smooth[max(0, i - min_gap) : i + min_gap + 1]
    if rms_smooth[i] == window.min() and rms_smooth[i] < np.percentile(rms_smooth, 60):
        t = float(t_rms[i])
        if not breaths or t - breaths[-1]["t"] >= 0.9:
            # depth: how far below the local max on both sides
            left = rms_smooth[max(0, i - min_gap * 2) : i]
            right = rms_smooth[i : i + min_gap * 2]
            depth_db = float(
                min(
                    (left.max() - rms_smooth[i]) if len(left) else 0.0,
                    (right.max() - rms_smooth[i]) if len(right) else 0.0,
                )
            ) / max(rms_smooth[i], 1e-9)
            breaths.append({"t": round(t, 3), "rms_db": round(float(20 * np.log10(max(rms_smooth[i], 1e-9))), 1), "relief_ratio": round(depth_db, 2)})

# --- onsets: peaks in smoothed flux with prominence ---
flux_thr = np.percentile(flux_s, 75)
onsets = []
i = 1
while i < n_frames - 1:
    if flux_s[i] > flux_thr and flux_s[i] >= flux_s[i - 1] and flux_s[i] > flux_s[i + 1]:
        t = float(t_rms[i])
        if not onsets or t - onsets[-1]["t"] > 0.35:
            onsets.append({"t": round(t, 3), "strength": round(float(flux_s[i]), 1)})
    i += 1

# --- tempo: autocorrelation of the (mean-removed) flux envelope ---
f = flux_s - flux_s.mean()
ac = np.correlate(f, f, mode="full")[len(f) - 1 :]
ac /= ac[0] if ac[0] else 1
lag_min = int(60.0 / 180.0 / (hop / sr))  # 180 BPM
lag_max = int(60.0 / 30.0 / (hop / sr))   # 30 BPM
best_lag = lag_min + int(np.argmax(ac[lag_min:lag_max]))
bpm = 60.0 / (best_lag * hop / sr)

# --- 0.25s RMS grid for shape reading ---
grid = {}
step = int(0.25 / (hop / sr))
for i in range(0, n_frames, step):
    grid[round(float(t_rms[i]), 2)] = round(float(rms_db[i]), 1)

# --- loop seam check: 28s seed xfade ~27.7-28.0 ---
seam = {"seed_end": 28.0, "note": "crossfade 0.3s before 28.0"}

out = {
    "path": PATH,
    "duration_s": round(dur, 3),
    "sr": sr,
    "channels": data.shape[1],
    "tempo_bpm_est": round(float(bpm), 1),
    "rms_db_grid_025": grid,
    "rms_db_min": round(float(rms_db.min()), 1),
    "rms_db_max": round(float(rms_db.max()), 1),
    "breathing_points": breaths,
    "onsets_first_40": onsets[:40],
    "onset_count": len(onsets),
    "seam": seam,
}
print(json.dumps(out, indent=1))

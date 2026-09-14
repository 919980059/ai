---
format: 1920x1080
duration: 10.74s
message: "POCO F9 Ultra — Ultrapower Unbound"
arc: Future Pacing
audience: global mi.com visitors evaluating the POCO F9 Ultra
mode: autonomous
music: soothing
---

# POCO F9 Ultra — tagline reveal

A 10.7-second, no-narration tagline reveal: one continuous dark footage world
(the phone's own Live-cinematography demo, seamless loop), the product name
fading in over it, and the page's hero tagline held as the closing lockup.
Soothing BGM underneath; every text arrival lands on the music's breathing
points.

## Video direction

- **palette system** (frame.md, dark register): near-black ground; display type in white ink; secondary gray for the quietest line if one ever appears; POCO yellow is the only chromatic voice — the tracked label and the single hairline, never a fill, never headline ink. The footage world is the only imagery in the film; type is the only other actor.
- **footage treatment**: the Live-cinematography loop is never raw — one restrained Product Polish grade (whole-video correction per media-treatments: gentle contrast, protected highlights, a touch of shadow lift) is applied identically to every frame's video element; under text the graded footage carries a black scrim that deepens frame by frame (none → ~35% → ~50%).
- **motion grammar + reveal model**: long-tail eases only (`power3` house curve — smooth over bouncy, zero overshoot). There is no narration, so the **BGM's breathing points are the cue track**: every text arrival completes on a named point of the analyzed beat grid, and the frame cuts land on the grid too. Reveals spread across each frame's duration — nothing dumps at t=0. During holds, stillness over motion: the footage's own slow light-drift is the film's aliveness, held type never breathes, at most a subtle jitter, and no camera push in any back half.
- **rhythm / held-frame allocation**: Frame 1 is the opening breather — pure atmosphere, zero DOM motion. Frame 2 carries one restrained move (the title's fade-in, the brief's 淡入标题). Frame 3 carries the lockup assembly, then the closing allocated stillness — the held read to the final frame. One reveal per frame, never more; the video's energy curve is breath → arrival → payoff.
- **caption band**: no captions in this film, but every lockup still composes into the top ~83% — nothing load-bearing in the bottom band, for bottom-edge consistency.
- **negative list**: no slideshow (front-load then freeze) and no screensaver (independent floating elements); no bouncy/overshoot eases; no lazy breathing on type; no invented POCO logo marks (the wordmark is set typographically in the brand face); no off-brand gradients, floating bokeh, or purple-blue "AI" washes; no browser chrome, nav bars, or cursors; no shadows, no rounded rectangles, no thick borders — the 1px POCO-yellow hairline is the only structural line.

## Frame 1 — Atmosphere

- key: atmosphere
- src: compositions/frames/01-atmosphere.html
- status: animated
- scene: full-bleed dark "flowing light and shadow" phone-cinematography footage (the POCO F9 Ultra's own Live cinematography demo) playing as one continuous, gently moving world — light drifts, nothing else happens; no text yet, the film opens already alive
- voiceover: —
- duration: 4.22s
- transition_in: none (first frame)
- type: hook
- persuasion: immersion — Future Pacing opening; pull the viewer into the product's world before any words
- beat: curiosity
- asset_candidates: assets/video-screen32-live.mp4 — [video] dark flowing-light cinematography loop, ~2560×1194, gentle continuous motion, seamless loop
- narrativeRole: wordless immersion — establish the dark premium world; the footage's slow light-play does all the talking
- keyMessage: the world before the name — atmosphere first
- blueprint: compose
- focal: the footage's bright drifting light-band — the frame's own subject
- roles: assets/video-screen32-live.mp4 = background (full-bleed cover, Product Polish grade, NO scrim in this frame — no text to protect; the footage plays at full graded strength)
- sfx: none — the soothing bed alone carries the immersion beat
- handoff_out: video (assets/video-screen32-live.mp4, full-bleed cover) — x: 0, y: 0, scale: 1.0, opacity: 1.0, motion: native seamless-loop playback only (its own slow light-drift; no transform motion); scrim: none (dim 0%) in this frame

Scene 1 (0.0–4.22s): the graded footage alone, full-bleed — layered-depth is the footage's own (bright drifting light-band focal against mid grays and near-black edges); zero DOM motion, zero text, no letterbox. No card shape applies here — the held, moving world IS the shot. The deliberate opening hold: the film is already alive because the footage moves, and nothing else happens. The frame closes on the BGM's breathing point at cut-time 4.22s — the cut lands in the music's rest. Full-bleed cover; the squint test passes on the light-band itself.

## Frame 2 — The name arrives

- key: name-reveal
- src: compositions/frames/02-name-reveal.html
- status: animated
- scene: the same footage world continues unbroken; "POCO F9 Ultra" fades in and settles as the film's title — POCOTech display, centered over the dimmed footage, the fade landing on a musical breathing point
- voiceover: —
- duration: 3.39s
- transition_in: crossfade
- type: product_intro
- persuasion: arrival — the reveal names the world we've been immersed in
- beat: recognition
- blueprint: titlecard-reveal (Reproduce)

Reproduce: the titlecard-reveal shape fits this beat directly — empty stage after the cut, then the ONE move (gentle fade-in + 95→100% scale settle) completing exactly on the 6.02s breathing point, then hold. No card surface — the dimmed footage world is the stage. Low motion is the payload, not a deficiency.
- asset_candidates: assets/video-screen32-live.mp4 — [video] the bed continues — same visual world, seamless loop, dimmed slightly under the title
- narrativeRole: the brief's fade-in title — the product's name arrives over its own footage
- keyMessage: this is the POCO F9 Ultra
- focal: "POCO F9 Ultra" — POCOTech 400, `h1` register (6.2cqw), white ink, one line, centered at optical center
- roles: assets/video-screen32-live.mp4 = background (full-bleed cover, the SAME Product Polish grade as Frame 1; scrim deepening to ~35% black across this frame to protect the type)
- sfx: none — the title's arrival is carried by landing on the music's breath, not by a sting
- handoff_in: video (assets/video-screen32-live.mp4, full-bleed cover) — x: 0, y: 0, scale: 1.0, opacity: 1.0, motion: native seamless-loop playback only (its own slow light-drift; no transform motion); scrim: none (0% — Frame 1's handoff state; this frame deepens it)
- handoff_out: video (assets/video-screen32-live.mp4, full-bleed cover) — x: 0, y: 0, scale: 1.0, opacity: 1.0, motion: native seamless-loop playback only; scrim: ~35% black; title "POCO F9 Ultra" — x: centered, y: optical center, scale: 1.0, opacity: 1.0, motion: none (held; it exits across the crossfade with this frame)

Scene 1 (0.0–0.50s): the incoming 0.5s crossfade — the footage world continues unbroken beneath it; no text yet.
Scene 2 (0.50–1.80s): first visible instant — the scrim deepens 0% → ~35% (0.50–0.83s) and the ONE move begins: "POCO F9 Ultra" fades in (opacity 0→1, power3.out long tail) with a 95→100% scale settle, one continuous gesture completing at 1.80s — cut-time 6.02s, the BGM's breathing point. Nothing else moves.
Scene 3 (1.80–3.39s): allocated stillness — the title holds dead still over the drifting footage while the music resumes beneath it (cut-time 6.34s). No breathing on type, no camera move, no second gesture.

## Frame 3 — Ultrapower Unbound

- key: tagline-lockup
- src: compositions/frames/03-tagline-lockup.html
- status: animated
- scene: the footage holds beneath a deeper dim; "Ultrapower Unbound" rises as the closing statement in the POCOTech display, with the POCO wordmark set in the brand face above it and a single POCO-yellow hairline beneath — held still to the final frame
- voiceover: —
- duration: 3.13s
- transition_in: crossfade
- type: branding
- persuasion: future identity — Future Pacing payoff; the viewer leaves on the promise
- beat: payoff
- blueprint: titlecard-reveal (Adapt)

Adapt — keep: the one-move-then-hold signature (a single reveal gesture completing on a breathing point, then allocated stillness). Change: the card is a three-element lockup (tracked POCO label, 1px yellow hairline, tagline) assembling as one continuous gesture instead of a single title, and the hold sits under the track's final swell — stillness set against the music's strongest moment.
- asset_candidates: assets/video-screen32-live.mp4 — [video] bed continues, dimmed deeper under the lockup
- narrativeRole: the closing lockup — the page's own hero tagline, held as the last read
- keyMessage: Ultrapower Unbound
- focal: "Ultrapower Unbound" — POCOTech 400, `display` register (8.0cqw), white ink, one line, centered; the tracked "POCO" label above and the single 1px POCO-yellow hairline beneath are its chrome
- roles: assets/video-screen32-live.mp4 = background (full-bleed cover, SAME Product Polish grade; scrim deepened to ~50% black for the closing read)
- sfx: none — the swell itself carries the payoff
- handoff_in: video (assets/video-screen32-live.mp4, full-bleed cover) — x: 0, y: 0, scale: 1.0, opacity: 1.0, motion: native seamless-loop playback only; scrim: ~35% black (Frame 2's handoff state; this frame deepens it toward ~50%); Frame 2's title exits across the crossfade — this frame opens on a text-free stage
- handoff_out: final frame (10.74s) — video (assets/video-screen32-live.mp4, full-bleed cover) — x: 0, y: 0, scale: 1.0, opacity: 1.0, motion: native seamless-loop playback only; scrim: ~50% black; lockup (POCO label + hairline + "Ultrapower Unbound") — x: centered, y: optical center, scale: 1.0, opacity: 1.0, motion: none — the held closing read, all of it within the top ~83% band

Scene 1 (0.0–0.50s): the incoming 0.5s crossfade — the footage continues beneath it, the scrim holding at Frame 2's ~35% handoff; text-free stage.
Scene 2 (0.50–1.54s): first visible instant — the scrim deepens ~35% → ~50% (0.50–0.90s) and the ONE move, one continuous assembly gesture, begins: the tracked "POCO" label ramps in above (0.50–1.20s), the single 1px POCO-yellow hairline draws beneath it (0.65–1.35s), and "Ultrapower Unbound" rises (0.80–1.54s, fade + slight rise, power3.out), completing at 1.54s — cut-time 9.15s, the deepest breathing point on the grid.
Scene 3 (1.54–3.13s): allocated stillness — the full lockup holds dead still while the music's final swell arrives (onset cut-time 9.86s, peak 10.36s) and resolves under it; nothing moves but the footage's own light-drift. The film ends on the held read.

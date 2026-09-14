# Frame packet: 02-name-reveal

## Project inputs

- Project: /Users/mi/workspace/.codex-worktrees/nrfe-xlab/feature/product-fastlane-final/videos/poco-f9-ultra-intro
- Design tokens: /Users/mi/workspace/.codex-worktrees/nrfe-xlab/feature/product-fastlane-final/videos/poco-f9-ultra-intro/frame.md
- RULES_DIR: /Users/mi/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 2 — The name arrives

- key: name-reveal
- src: compositions/frames/02-name-reveal.html
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

Scene 1 (0.0–0.33s): the cut settles — the footage world continues unbroken, the scrim deepens from 0% toward ~35%; no text yet. Static establish.
Scene 2 (0.33–1.80s): the ONE move — "POCO F9 Ultra" fades in (opacity 0→1, power3.out long tail) with a 95→100% scale settle, one continuous gesture completing at 1.80s — cut-time 6.02s, the BGM's breathing point. Nothing else moves.
Scene 3 (1.80–3.39s): allocated stillness — the title holds dead still over the drifting footage while the music resumes beneath it (cut-time 6.34s). No breathing on type, no camera move, no second gesture.

## Selected blueprint: titlecard-reveal

# titlecard-reveal — Title-Card / Single-Card Reveal

**intent**: The calm breather/landing beat — one clean title or single brand/proof card revealed with exactly one restrained move (a slide-up crossfade, or a wipe-away-to-reveal), then a still hold. Low motion is the payload, not a deficiency.

**roles served**

- Benefits (from `benefits-titlecard-crossfade`, #34): a calm two-line value title card — headline value line, then one slide-up crossfade to a qualifier/elaboration line that holds center.
- Social_Proof (from `social-proof-reveal-card`, #35): wipe a busy app-collage open away with one diagonal pill-sweep to reveal a clean brand lockup (icon + wordmark) plus a centered "loved by [N]+ [audience] teams" social-proof line that spring-settles and holds.
- CTA (from `hard-cut-card-stack-to-logo`): a monochrome end-card
  CHAIN — statement → CTA / availability line → brand wordmark/logo — separated by instant hard
  cuts at full opacity; each card is its own allocated stillness, and the sequence terminates on
  the logo held to the final frame.
- Product_Intro (from `title-card-prelude-chain`): a three-beat dark title
  PRELUDE before any product UI — `[logo]` pop → `[name]` (a `[version]` appends grey→bright) →
  `[tagline]` card — chained by clears and blur-snap handoffs rather than hard cuts.

**duration**: 3–5s (Benefits 3–4s; Social_Proof ~5s / observed 4.7s). Card chains run 2–3s per
card, ~5.5–9.5s total.

**shot structure**

```
Scene 1 (0.0–~0.4s): static camera on [neutral / dark background]. Establish the opening state.
  Variant — Benefits: empty-to-text — [benefit line 1] is about to fade in centered (no busy open).
  Variant — Social_Proof: a busy intro frame holds briefly — an [app-screenshot / use-case collage] of overlapping cards under a [setup line].

Scene 2 (~0.4–~1.5s): the ONE move executes — a single restrained reveal that brings the calm card to center.
  Variant — Benefits: [benefit line 1] fades in centered while scaling slightly (~95%→100%, smooth ease-out) and holds.
  Variant — Social_Proof: a large [accent-color] rounded pill sweeps diagonally bottom-left → top-right and exits the corner, clip-path wiping the collage away to reveal the [brand logo lockup] beneath as the [logo icon] strokes draw on.

Scene 3 (~1.5s–end): the revealed/settled card holds to the end (the allocated stillness). At most one subtle live element (a slow breathing pulse on the card, or a very slow camera drift). No second development phase.
  Variant — Benefits: [benefit line 1] translates up and fades out as [benefit line 2 — qualifier / elaboration] translates up from below center and fades in to take center; holds. (This single slide-up crossfade IS the one move — Benefits front-loads no Scene-2 wipe.)
  Variant — Social_Proof: the lockup — [logo icon] centered, [wordmark] below, centered [social-proof tagline] "Loved by [N]+ [audience] teams" (the [N]+ may count up) — spring-settles small, then holds.

Variant — card chain (CTA end-card stack / Product_Intro title prelude): the single-card contract
repeats 2–3 times in sequence. Each card is a complete Scene 1–3 in miniature — arrive (or simply
BE there), at most one restrained move, hold — and the seams between cards are INSTANT hard cuts
at full opacity (no crossfade, no fade-through-black) or, in the prelude flavor, a blur-away →
snap-into-focus handoff.
  Card moves stay on budget: a character-by-character type-on with visible partial states, a
  right-to-left backspace that resolves the [wordmark] into the small [logo icon], a grey→bright
  append ("[name]" gains "[version]"), a blur-snap into focus — or nothing beyond a
  barely-perceptible continuous slow scale-up across the hold.
  The final card is always the [brand logo / lockup], held static to the last frame.
```

**motion vocabulary**: single restrained reveal (gentle fade-in + subtle scale-up settle | diagonal clip-path pill-wipe), one slide-up crossfade between two centered lines (Benefits), icon stroke draw-on (Social_Proof), optional "[N]+ teams" count-up, logo+tagline spring-settle-and-hold, subtle breathing on the held card, hold-to-end. Calm register — no spring chains, no tumble, no per-beat flips, no second phase. Camera static (optional very slow drift only). Card-chain register: instant hard cut at full opacity as the only seam, barely-perceptible
continuous slow scale-up across each hold, character-by-character type-on with visible partial
states, right-to-left backspace collapsing the wordmark into the logo icon, grey→bright text
append, blur-away → snap-into-focus card handoff, logo pop with overshoot + glow (prelude opener),
monochrome text-on-solid throughout.

**rule mapping**

- gentle fade-in + subtle scale-up settle (Benefits Scene 2) → `rules/scale-swap-transition.md` (restrained in/settle; cross-reference the fade ease in `techniques.md`)
- single slide-up crossfade between two centered lines (Benefits Scene 3) → `rules/discrete-text-sequence.md` (one line hands off to the next; translate-up + crossfade)
- diagonal pill-wipe reveal (Social_Proof Scene 2) → `rules/techniques.md` (clip-path reveal masks — the wipe)
- icon stroke draw-on (Social_Proof Scene 2) → `rules/svg-path-draw.md`
- "[N]+ teams" count-up (Social_Proof Scene 3, optional) → `rules/counting-dynamic-scale.md`
- logo + tagline spring-settle-and-hold (Social_Proof Scene 3) → `rules/spring-pop-entrance.md` (single soft settle; intentionally one beat, not a chain)
- subtle breathing on the held card (the one live element during the hold) → `rules/sine-wave-loop.md`
- type-on / backspace / grey→bright append (chain cards) → `rules/discrete-text-sequence.md`
  (non-linear typing incl. backspace; drive the version append as a bulk addition)
- wordmark remainder resolves into the logo icon → `rules/scale-swap-transition.md` (same-center
  swap fired as the last character deletes)
- barely-perceptible slow scale-up across a hold → the camera-modifier drift
  (`rules/multi-phase-camera.md`, micro-drift register) applied per-card
- blur-away → snap-into-focus handoff (prelude flavor) → `rules/depth-of-field-blur.md` (single
  pull on the outgoing / incoming card)
- logo pop with overshoot + glow (prelude card 1) → `rules/spring-pop-entrance.md` +
  `rules/ambient-glow-bloom.md`
- instant hard cut at full opacity → not a rule: a timeline `tl.set` swap — deliberately NO
  transition entry.

**camera modifier**: optional — a single very slow drift/push under the hold only → `rules/multi-phase-camera.md`. Default is fully static; do not add unless the held beat would otherwise read as a freeze-frame.

**stillness note**: This is a legitimate allocated-stillness beat. The hold in Scene 3 is the deliverable, not an unanimated gap — do NOT manufacture a development phase, extra swaps, or force-animation. One restrained move + a subtle hold (optionally one breathing element or one slow drift) is the correct and complete shape. The card-chain variant does not break this: each card individually obeys the one-move + hold
contract, and the hard cut is a seam, not a move. Boundary: if the cards flip at sub-second tempo
or each beat carries its own entrance/exit energy, you have left this blueprint — that is
`kinetic-type-beats` (its CTA variant owns the high-tempo value-line stack).

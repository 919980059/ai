---
format: 1920x1080
duration: 30.5s
message: "一车一世界，自在即澎程"
arc: 「一车一世界」三幕 — 型（identity）→ 世界（space）→ 远方（range）→ 定版（slogan）
audience: 中文市场关注小米澎程 SkyNomad N90 的家庭与商务高意向用户
mode: autonomous
language: zh
music: soothing warm ambient electronic — 科技潮流 × 高端舒适（soft sustained pads, gentle slow pulse, spacious calm modern production）；2026-09-11 起音乐为唯一声轨
voice: none（2026-09-11 移除旁白与全部音效 — 音乐独奏版） · bgm assets/bgm/track-38s.wav @ volume 0.95 · 尾音 fade 28.5→30.5
---

## Video direction

**两界系统（two registers）.** 全片在两个质感界面上交替：**纸界**（F2–F5）—— biennale 纸白编辑版面：paper 底、单一 ink 字色、酒红 `sun #643C31` 只作 bloom / panel / 发丝线电压色、1px hairline、0 圆角 0 阴影；**影界**（F1/F6）—— 品牌原生暗色电影面：near-black 底、白字、酒红 accent、摄影全幅。纸界内永不反白；影界内永不铺纸。交替即全片呼吸：暗（问）→ 纸（答）→ 暗（远）→ 明（定）——F7 定版以原图亮场 + 墨色 lockup 收束（2026-09-11 原图直出修订），是全片唯一的 register 反转。pagenum（bottom-right mono）跨两界常驻 — 纸界 ink 75%，影界 white 75%。

**Motion grammar.** power3 长尾是唯一默认落法 — 无弹跳、无 overshoot（弹簧只许「收」不许「过」）；一切入场 `fromTo` 显式 from 态；**VO-reveal 律**：元素在旁白点到它之前不可出现，揭示密度压在各 Scene 的后 ~50%；宁静止勿坏动 — hold 期唯一活性是 subtle jitter；帧内接缝一律 velocity-matched（cut-catalog：blur-snap / cut-the-curve）；帧间转场归 harness 注入（transition_in 即出场），帧内不做出场，出场只属于末帧与转场。

**Beat-timing model（音乐独奏版）.** 2026-09-11 修订：全片移除旁白与音效，BGM 为唯一声轨（volume 0.95 独奏级）。各帧镜头序列的节拍结构沿用原 silencedetect 实测词点网格（各帧 `vo_cues:` 保留为历史节拍参考，已无音频对位）；动画落点即视觉节拍，全部保持不变。

**Rhythm.** 七帧问答弧：问（F1）→ 命名（F2）→ 展开（F3）→ 证据（F4）→ 并置（F5）→ 远方（F6）→ 定版（F7）。静持分配：F2 卡片近静止（一卡一动作）；F6 数字落定后纯持；F7 尾段 ≥20% dead static。影帧相机推进连续不断（一根时间线一个 writer）；纸帧动线短促克制（进槽即停）。

**Caption band（已移除字幕）.** 2026-09-11 修订：字幕合成（compositions/captions.html）已从主时间线移除，全片不再渲染字幕带；既有帧布局仍保持底部 ~17% 留白习惯。

**Negative list.** 幻灯片式（前 25% 倾倒全部内容后冻结）；懒呼吸（循环 scale 冒充活性）；后半程慢推慢 pan 打断视线；弹跳入场（back/bounce/elastic 作默认）；无限循环 / repeat / yoyo；Math.random / Date.now；屏保感（多元素各自漂浮）；纸界反白或影界铺纸；帧中段退场。

---

## Frame 1 — 多少种生活

- scene: 黑场冷开，小米澎程字标隐现，开场暗色整车 hero 缓慢推近；提问逐短语落在画面上
- voiceover: none（2026-09-11 移除）
- duration: 3.8s
- vo_cues: 01.wav slot 0.00 @+0.00 (3.432s) — zf_xiaoyi 短语拆分实测（帧内 = WAV + 0.00）：「一辆车」0.24–0.96（顿 0.96–1.34）·「能装下」1.34–1.95 ·「多少种生活」2.29–3.24 · VO 尾 3.24
- transition_in: cut
- status: animated
- src: compositions/frames/01-lives-question.html
- type: hook
- persuasion: Future pacing（打开可能性空间——观众自己的生活在提问里）
- beat: curiosity
- blueprint: kinetic-type-beats
- focal: push-in — 居中文字在一根连续慢推中获得焦点
- roles: hero=提问双短语 · support=1.jpg 暗色整车全幅 · chrome=字标 ghost + pagenum
- asset_candidates: assets/1.jpg — 开场暗色整车 hero 2560×1440; assets/inline-svgs/wordmark-xiaomipengcheng.webp — 小米澎程字标

narrativeRole: 用一个问题把观众自己的生活放进画面——不为车而来，为「装得下多少种生活」这个可能性而来。整支片是对这个问题的回答。
keyMessage: 这支片要回答的问题：一辆车与你的全部生活。

**Shot sequence**

- **Scene 1 (0.0–0.25s) 冷开定场** — 近黑场；整车 hero（assets/1.jpg，影界低亮度级）全幅经 soft-blur-in 入场（blur→sharp）；**一根连续慢推**自 t=0 起于根节点、贯穿全帧不中断（单相机多相位推进的 push 相位，中途不得 re-push）；小米澎程字标 ghost 置左上 rail（低透明度，rail-label 字级）。此外画面为空。
- **Scene 2 (0.25–1.02s) 第一拍** — VO「一辆车」0.24 起读 → 短语以**一个整体**经弹收式入场落于画面中心（smooth 长尾收，无 overshoot），白色 display 字级压在暗色照片上。
- **Scene 3 (1.02–2.3s) 第二拍** — VO「能装下多少种生活？」1.34 起读 → 中心同位换拍：「一辆车」缩小淡出让位，完整问句到达同一中心（kinetic beat 的 token 换拍，阈值切替；换拍本身即节拍）。
- **Scene 4 (2.3–3.8s) 悬问静持** — 问句 held read 静止；相机同一速率继续慢推（subject 在动，非假活性）；至多 subtle jitter 于问句行（~2.80 / ~3.15）。帧末：hero 约 1.06× 起始 scale，问句居中，全画面静止。

**handoff_in** — 全片第一帧，画面自黑起。
**handoff_out** — 暗色整车全幅照片（x/y 0，scale ≈1.06，opacity 1）+ 居中白色问句（opacity 1，静止）+ 左上字标 ghost；场亮度深暗。

---

## Frame 2 — 型方面润

- scene: 纸白编辑版面，两张暗色摄影卡（造型 hero／蜻蜓大灯）以 blur-snap 接力；名称锁定「小米澎程 N90 Max」+ 微标签「大七座旗舰增程 SUV」；「型方面润」四字随旁白逐字落下
- voiceover: none（2026-09-11 移除）
- duration: 5.0s
- vo_cues: 02.wav slot 3.20 @+0.00 (4.601s) — zf_xiaoyi 短语拆分实测（帧内 = WAV + 0.00）：「小米澎程 N90 Max」0.24–3.09（N90｜Max 换气 2.27–2.38）·「型方面润」3.45–4.40；四字：型 3.45 · 方 3.69 · 面 3.93 · 润 4.16 · VO 尾 4.40
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/02-form.html
- type: product_intro
- persuasion: Show-don't-tell proof（设计语言用摄影证明，不用形容词）
- beat: awe → appreciation
- blueprint: titlecard-reveal
- focal: caption-editorial-emphasis — 双字级戏剧对比承载名称锁定与四字宣言
- roles: hero=「型方面润」四字 display 行 · support=摄影卡链（6.jpg→8-1.jpg）+ 名称锁定 · chrome=vertical rail + 微标签
- asset_candidates: assets/6.jpg — 型方面润造型 hero 2560×1440; assets/7-2.jpg — 棱镜轮毂 21″; assets/8-1.jpg — 蜻蜓大灯细节 1152×852; assets/New_1-1.jpg — 酒红车身色彩 hero 2560×1440

narrativeRole: 命名产品并立住气质——方正的框架（版面）承载圆润的形（摄影），型方面润由观看得出而非由旁白宣称。
keyMessage: 小米澎程 N90 Max——型方面润。

**Shot sequence**

- **Scene 1 (0.0–0.25s) 纸面起手** — paper 场 + sun-bloom（偏左）一次性 bloom-in（finite，不循环）；左缘 vertical-rail「型 · FORM」；空台。
- **Scene 2 (0.25–3.10s) 命名** — VO 点名 0.24 起读 → 名称锁定 per-word staggered reveal 组装（dynamic-content-sequencing）：「小米澎程」display → 「N90 Max」接续；微标签「大七座旗舰增程 SUV」~1.78 落于其下（caption-editorial-emphasis 双字级对比）；造型 hero 卡（6.jpg）~0.35 短距 direct-into-slot 入左面板（低戏剧，进槽即停）。
- **Scene 3 (3.10–3.45s) 卡链缝** — VO 短语间隙 → blur-snap 接力：6.jpg 经 depth-of-field-blur 出焦，蜻蜓大灯（8-1.jpg）同位 snap 入焦（titlecard-reveal 卡链缝，两侧峰值模糊一致）；名称锁定降为次级（一次性状态变化，opacity →0.35）。
- **Scene 4 (3.45–5.0s) 四字落** — 「型」「方」「面」「润」各随 VO 音节（3.45/3.69/3.93/4.16）经 discrete-text-sequence 阈值步进落于卡侧 display 位，每字 soft-blur-in 落定；微标签换「细节设计 · 风格鲜明」~3.80（方｜面顿 3.69–3.93 内）。4.40–5.0 held read，全画面静止。

**handoff_in** — t=0 纸面空场；sun-bloom 正在到达（F1 暗场 → 纸界的 register 切换由 blur-crossfade 承担）。
**handoff_out** — paper 场；8-1.jpg 卡静置于左面板（scale 1，静止）；「型方面润」四字 display 行完整（opacity 1）于卡右；名称锁定次级悬于上；微标签在场。全静止。

---

## Frame 3 — 一个空间，不止一种答案

- scene: 纸白版面，2+2+3 hero 作锚定面板，空间模式卡（会客厅／电影院／卧房）随旁白逐一点名级联组装；宣言行随后落下
- voiceover: none（2026-09-11 移除）
- duration: 5.6s
- vo_cues: 03.wav slot 7.60 @+0.00 (5.161s) — zf_xiaoyi 短语拆分实测（帧内 = WAV + 0.00）：「一个空间」0.24–1.18（顿 1.18–1.55）·「不止一种」1.55–2.44 ·「答案」2.48–2.90 · 破折号顿 2.90–3.26 ·「会客厅」3.26–3.62 ·「电影院」3.66–3.98 ·「卧房」4.03–4.97 · VO 尾 4.97
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/03-space-answers.html
- type: feature_showcase
- persuasion: Feature-to-benefit translation（空间模式翻译成生活的场景，不是配置表）
- beat: aspiration + belonging
- blueprint: grid-card-assemble
- focal: grid-card-assemble — N 张能力卡交错组装进网格
- roles: hero=宣言行「一个空间，不止一种答案——」 · support=12.jpg 锚定面板 + 三张模式卡（VO 点名入场） · chrome=微标签 + strand 行标
- asset_candidates: assets/12.jpg — 2+2+3 大七座布局 hero 2560×1440; assets/16-1.jpg — 智能可变空间模式卡 1556×778; assets/17-1cover.jpg — 床／露营空间模式封面; assets/19-3cover.jpg — 后排私人影院模式封面

narrativeRole: 把「大空间」从容积数字升维成「生活的多种答案」——车内的每一形态对应观众的一种生活时刻，为双世界与远方铺垫。
keyMessage: 空间是可变的，答案不止一种。

**Shot sequence**

- **Scene 1 (0.0–0.25s) 锚定** — paper 场延续；2+2+3 hero（12.jpg）锚定面板自左短距 direct-into-slot 入左上位（进槽即停）；微标签「智能可变大空间」；sun-bloom 置对角（一帧一 bloom 律）。
- **Scene 2 (0.25–1.55s) 首句** — VO「一个空间，」0.24–1.18 → 宣言行 per-word staggered reveal 落于锚定面板侧（display 字级）；落定后静止。
- **Scene 3 (1.55–3.26s) 答案行** — VO「不止一种答案」1.55–2.90 → 第二行以同一 word-beat 级联续接（连续节拍，非倾倒）；破折号「——」2.90–3.26 以 svg-path-draw 发丝线画出。
- **Scene 4 (3.30–4.97s) 三卡点名** — 模式卡严格踩 VO 点入场：「会客厅」3.30 → 16-1.jpg（对坐）、「电影院」3.66 → 19-3cover.jpg（影院）、「卧房」4.05 → 17-1cover.jpg（床／露营）；各为短距 direct-into-slot 入场（grid-card-assemble 交错级联，~0.3s 行程，center-outward-expansion 次序落位锚定面板下方的 strand 行），各卡标签随卡落为 strand-row 标注。
- **Scene 5 (4.97–5.6s) 满编静持** — 网格满编静止（至多最新一卡 subtle jitter ~5.08）。

**handoff_in** — paper 场延续（push-slide LEFT 自 F2 同界递进）；锚定面板正在入槽。
**handoff_out** — paper 场；12.jpg 锚定面板左上，三张模式卡成行于其下，宣言行完整；全静止。

---

## Frame 4 — 1831L

- scene: 纸白版面，1831 巨型数字（MiSans 340）计数上行；后备厢 hero 面板与骑行生活方式卡作为「说走就走」的兑现
- voiceover: none（2026-09-11 移除）
- duration: 5.0s
- vo_cues: 04.wav slot 12.60 @+0.00 (4.556s) — zf_xiaoyi 短语拆分实测（帧内 = WAV + 0.00）：「1831（壹仟捌佰叁拾壹）」0.24–1.51（微顿 1.51–1.63）·「升后备厢」1.63–2.61 · 逗号 2.61–2.96 ·「装下说走就走」2.96–4.37 · VO 尾 4.37
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/04-trunk-1831.html
- type: feature_showcase
- persuasion: Statistical proof（数字先行，生活方式兑现）
- beat: ease + freedom
- blueprint: dataviz-countup
- focal: mk-progress-stat — 巨字统计 + 计数 + 细填充轨道
- roles: hero=1831 numeral-jumbo + 填充轨道 · support=20.jpg 后备厢面板 + 20-2.jpg 骑行卡 · chrome=单位标签 + 微标签
- asset_candidates: assets/20.jpg — 1831L 超大后备厢 hero 2560×1440; assets/20-2.jpg — 户外骑行生活方式卡 1556×778

narrativeRole: 用一个可数的证据兑现上一帧的可能性——装载力被翻译成「说走就走」的自由感。
keyMessage: 1831L——自由是有容积的。

**Shot sequence**

- **Scene 1 (0.0–0.20s) 起手** — paper 场；微标签「超大后备厢 · CARGO」；sun-bloom 置数字区之后；空台。
- **Scene 2 (0.24–2.61s) 计数** — 「1831」numeral-jumbo 随读音 0→1831 计数上行（counting-dynamic-scale — scale 随值同 ease 增长，读音毕数字毕 1.51）；mk-progress-stat 细填充轨道在其下同程填充（stat-bars-and-fills，轨道即「装载线」）；「升后备厢」单位标签 1.63 落定。
- **Scene 3 (2.96–3.95s) 兑现** — VO「装下说走就走」2.96 起读 → 后备厢 hero（20.jpg）2.96 短距 direct-into-slot 入右面板；骑行生活方式卡（20-2.jpg）3.55 续接落位（两步交错级联，均进槽即停）。
- **Scene 4 (3.95–5.0s) 静持** — 数字保持原位（不呼吸），双卡静止；held read 至帧末（VO 尾 4.37）。

**handoff_in** — paper 场空台（push-slide LEFT 自 F3 同界递进，内容重置）。
**handoff_out** — paper 场；1831 巨字 + 单位标签居左上，两摄影面板居右；全静止。

---

## Frame 5 — 双世界

- scene: 纸白版面左右对开：陆地公务舱（商务）与全家舒适（家庭）两张等重摄影面板自中缝镜像滑入（2D 平面入场，照片零形变）；中缝酒红发丝线
- voiceover: none（2026-09-11 移除）
- duration: 5.0s
- vo_cues: 05.wav slot 17.00 @+0.00 (4.617s) — zf_xiaoyi 短语拆分实测（帧内 = WAV + 0.00）：「商务」0.23–1.02（微顿 1.02–1.06）·「是陆地公务舱」1.06–1.78 连读 · 分号 1.78–2.14 ·「家庭」2.14–2.92（微顿 2.92–2.99）·「是移动的生活空间」2.99–4.42 · VO 尾 4.42
- transition_in: crossfade
- status: animated
- src: compositions/frames/05-two-worlds.html
- type: benefit_highlight
- persuasion: Value stacking（同一辆车对两种人生的双重价值）
- beat: confidence + trust
- blueprint: comparison-split
- focal: comparison-split — 双全幅面板 + 中缝分隔线
- roles: hero=两张镜像摄影面板（New_2.jpg 左 / New_4.jpg 右） · support=内缘 pill 徽标 + 界别标签 · chrome=中缝酒红发丝线 + 微标签
- asset_candidates: assets/New_2.jpg — 商务旗舰「陆地公务舱」hero 2560×1440; assets/New_4.jpg — 家庭旗舰「全家舒适」hero 2560×1440

narrativeRole: 回答第一帧的问题的一半——不止装得下多种生活，还同时在两种人生里都成立；「一车一世界」的世界在此显形为复数。
keyMessage: 一辆车，两种人生，都从容。

**Shot sequence**

- **Scene 1 (0.0–0.20s) 中缝立轴** — paper 场；中缝一条酒红发丝线自上而下 svg-path-draw 画出（两世界将在此会合）；微标签「一车 · 两世界」置顶。
- **Scene 2 (0.20–1.02s) 左界开** — VO「商务」0.23 起读 → 左面板（New_2.jpg）自中缝短距滑出：镜像 2D 入场（x/scale/opacity 全在包装层，零透视零 3D — 照片全程原比例；2026-09-11 拉伸修订：原 book-open rotateY 在成片中渲染为照片横向压扁再展开的仿射挤压，实测 19.35s 面板右缘被压进 56px，已整体移除），0.85→1 落定；「商务」标签 0.20 落于面板外缘。
- **Scene 3 (1.02–2.14s) 左界徽标** — VO「是陆地公务舱」1.06–1.78 连读 → pill 徽标「陆地公务舱」~1.10 落于面板内缘（克制落定 — 全帧唯一 spring 强调，无 overshoot）。
- **Scene 4 (2.14–2.99s) 右界开** — VO「家庭」2.14 → 右面板（New_4.jpg）以同形 2D 滑出自中缝镜像入场（同一入场形、同一落法定成镜像，零形变）；「家庭」标签 2.14。
- **Scene 5 (2.99–5.0s) 右界徽标 + 静持** — VO「是移动的生活空间」2.99–4.42 → pill「移动的生活空间」~3.90 落于右面板内缘（与左侧节奏呼应）；4.42–5.0 held read；**双面板静止不浮**（面板零 3D 倾斜零漂浮，照片以原比例呈现 — 静止胜于坏动）。

**handoff_in** — paper 场，中缝发丝线正在画出（crossfade 自 F4 同界递进）。
**handoff_out** — paper 场；左右双面板关于中缝满幅对称，双徽标落定；全静止。

---

## Frame 6 — 1705km

- scene: 暗色全幅——昆仑超级增程横幅缓慢电影式推进；1705 白色数字计数落定，mono 标签「km · CLTC 综合续航」；「远方」意象收束
- voiceover: none（2026-09-11 移除）
- duration: 5.3s
- vo_cues: 06.wav slot 21.40 @+0.00 (4.795s) — zf_xiaoyi 短语拆分实测（帧内 = WAV + 0.00）：「1705（壹仟柒佰零伍）」0.24–1.07（微顿 1.07–1.14）·「公里综合续航」1.14–2.76 · 破折号 2.76–3.13 ·「远方，就在脚下」3.13–4.60 · VO 尾 4.60
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/06-range-1705.html
- type: benefit_highlight
- persuasion: Future pacing（续航被翻译成「可达的远方」）
- beat: liberation + aspiration
- blueprint: camera-journey
- focal: pan-stations — 横幅上一根横向镜头移动 + 驻点落定
- roles: hero=1705 数字 + 相机旅程本身 · support=28.jpg 昆仑横幅长条 + mono 技术站位（76kWh 龙甲电池 / 60L 油箱）+ 20-4.jpg 海边观景 · chrome=「km · CLTC 综合续航」mono 标签 + pagenum
- asset_candidates: assets/28.jpg — 昆仑超级增程 1879×836 横幅; assets/20-4.jpg — 海边观景生活方式卡 1556×778; assets/31.jpg — 性能底盘 hero 2560×1440

narrativeRole: 把全部室内世界推向室外——空间叙事升维为距离叙事，增程技术以「远方」而非 kWh 讲出。
keyMessage: 1705km——世界大，是因为够得着。

**Shot sequence**

- **Scene 1 (0.0–0.20s) 影界启程** — near-black 场；一个 oversized `.world` wrapper 装下全程：昆仑横幅（28.jpg）作宽幅长条、沿条 mono 技术站位（「76kWh 龙甲电池」「60L 油箱」文字站位）、1705 数字区、其外 20-4.jpg 海边观景区；相机起于横幅纹理的紧框（world 处于起始 pose）。
- **Scene 2 (0.20–1.10s) 横向推进** — VO 数「壹仟柒佰零伍」0.24–1.07 → 相机沿横幅横向 tracking（pan-stations 横移，施于 `.world` 包装层）；速度峰值模糊随速度起峰、驻点前收零；技术站位随相机抵达逐一 soft-blur-in 现身（~0.50 / ~0.78）。
- **Scene 3 (1.10–2.76s) 俯冲落数字** — VO「公里综合续航」1.14–2.76 → 相机俯冲向 1705 数字区（坐标俯冲缩放，power4.out 落法）；数字随读音 0→1705 计数（counting-dynamic-scale，读音毕数字毕 2.76）；「km · CLTC 综合续航」mono 标签 ~2.30 落于其下。
- **Scene 4 (2.76–3.13s) 破折号屏息** — 相机持住（全程唯一静拍）。
- **Scene 5 (3.13–3.93s) 远方拉开** — VO「远方，就在脚下」3.13 起读 → 相机 pull-back（world scale 收小），20-4.jpg 海边观景自数字身后升起、世界围绕数字变宽；「远方」3.13 落字，拉阔 ~3.93 完成；数字收势落定。
- **Scene 6 (3.95–5.30s) 静持** — 数字 + 景观静止。

**Seek-safety（非协商）** — 整程在**一根 paused GSAP 时间线**上：单一 camera state object + 单一 `applyCamera()` writer；各 leg 目标在 `fonts.ready` 后**一次测得**（onUpdate 内禁止 getBoundingClientRect）；wrapper 近旁零 CSS transition；scene 根 overflow:hidden + `.world` 挂 data-layout-allow-overflow。

**handoff_in** — 影界暗场（blur-crossfade 自 F5 纸界 — register 切换）；world 于起始 pose，相机紧框横幅纹理。
**handoff_out** — 暗场；1705 白字数字居中偏左、20-4.jpg 全幅在其后；相机 rest pose（world scale ≈1，translate 0）；全静止。

---

## Frame 7 — 定版

- scene: zoom-through 收进整车原图；小米澎程字标（原生深色、亮度键出底版）自件组装落定，slogan「一车一世界，自在即澎程」墨字落下；微标签「为那些活得明白、过得丰富的人而来」；CTA 行「预约试驾 · 26.99 万起」mono；静持收尾
- voiceover: none（2026-09-11 移除）
- duration: 4.4s
- vo_cues: 07.wav slot 26.10 @+0.00 (2.884s) — zf_xiaoyi 短语拆分实测（帧内 = WAV + 0.00）：「一车一世界」0.25–1.31 · 留白 1.31–1.54 ·「自在即澎程」1.54–2.69（五字各 ~0.23s：自 1.54 · 在 1.77 · 即 2.00 · 澎 2.23 · 程 2.46）· VO 尾 2.69 · hold 2.69–4.40
- transition_in: zoom-through
- status: animated
- src: compositions/frames/07-slogan-lockup.html
- type: branding
- persuasion: Identity resolution（slogan 作为观众自我定义的收束）+ 轻量 CTA
- beat: peace of mind + inevitability
- blueprint: logo-assemble-lockup
- focal: logo-outro — 逐件组装 + tagline 淡入 + 收束行
- roles: hero=小米澎程字标 + slogan 行 · support=2.jpg 原图直出全幅（无特殊处理、无 scrim，车区零遮蔽；文字全部落在车上方亮背景带） · chrome=微标签 + CTA 行 + pagenum
- asset_candidates: assets/inline-svgs/wordmark-xiaomipengcheng.webp — 小米澎程字标; assets/2.jpg — 整车 hero 原图直出

narrativeRole: 回答完成——开头的问题以 slogan 收束：装得下多少种生活？一个世界那么多。品牌定版与行动入口同框。
keyMessage: 一车一世界，自在即澎程。

**Shot sequence**

- **Scene 1 (0.0–0.25s) 原图接引** — 整车原图（2.jpg 全不透明、无调色直出）t=0 即在场（不自有入场）；其上空台。zoom-through 转场接引自 F6 的 rest pose 收进。
- **Scene 2 (0.25–1.41s) 字标组装** — 小米澎程字标以左→右分段遮罩扫现（logo-outro 逐件组装适配于字标图像；discrete 揭示，无弹跳），~1.41 完成。（原 glow bloom 已随原图直出修订移除）
- **Scene 3 (1.54–2.69s) slogan 落定** — slogan 行随五音节（1.54/1.77/2.00/2.23/2.46）per-word staggered reveal 落于字标下方（墨色 headline 字级）。
- **Scene 4 (2.85–3.52s) 收束** — 微标签「为那些活得明白、过得丰富的人而来」2.85 soft-blur-in 至次级透明度；发丝线 3.10 + CTA 行 3.20–3.52 落定：「预约试驾 · 26.99 万起」mono（一次克制落定）。
- **Scene 5 (3.52–4.40s) dead static** — lockup 律：终局 ≥20% 绝对静止（0.88s / 4.4s），静默向黑；BGM 尾音衰减（bed fade 28.5→30.5，即帧内 2.4→4.4）。

**handoff_in** — 整车原图在场；相机经 zoom-through 自 F6 rest pose 抵达。
**handoff_out** — 末帧：完整 lockup 静止至片尾（无退场 — 影片终止于 hold）。

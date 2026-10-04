# Presentation update

- Jumpscares live exclusively in the Troll Panel. The separate HUD shortcut/modal was retired; the seven target-player actions use a compact two-column layout.
- The game keeps the engine-created All Out avatar and cosmetics. It no longer swaps the live skeleton to the legacy character rig or forces Pileo's rainbow tint. Weapon animation data is attached alongside the native rig; compatible native holding poses and hand-anchored weapon art preserve combat and emotes.
- Interpretation used for the ambiguous character replacement: Lily Lovebraids (purple-haired girl, second attachment) replaces Lovity only during the Mrlovebraids event, including morph art, labels, and jumpscare art. The hugging pair remains available. Existing morphs refresh when the event starts/stops, and synced clients refresh their presentation.

## Art
Built-in image_gen was used, saved as `res/mrlovebraids/purple_braids_girl.png`.
Prompt: Extract only the full purple-haired girl from the last attached reference; preserve her face, pose, purple star shirt, black skirt, star boots, purple shoes, and enormous heart-shaped purple braids. Remove the checkerboard and screenshot controls. True transparent alpha, full silhouette, no text/UI; do not include the hugging pair.

## Verification
`test_troll_panel_avatar_and_event_replacement`: 23 checks passed on PC and on iPhone SE phone emulation. Live screenshots verified native avatar, weapon art, and event replacement. Scripts compile; new assets validate as publishable.
`test_shop_revision_emotes_and_catalog`: 27 checks passed with fresh test persistence. A live late-joining multiplayer client initialized its own avatar/weapon presentation without warnings.

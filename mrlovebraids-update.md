# Mrlovebraids update

## Custom art
Built-in image generation was used. Final assets are in `res/mrlovebraids/`:
- `verity.png`: isolated glossy yellow smiley from reference 1.
- `lovity.png`: isolated glossy magenta smiley from reference 2.
- `mrlovebraids_marcat.png`: reference 3 hugging pair and purple braid-heart frame, without screenshot background/UI.
- `hair_trap.png`: purple braid loop with white flowers matching reference 3.
- `bat.png`: thick-outlined wooden baseball bat.
- `durp_space_armor.png`: isolated cobalt-blue/silver cartoon space armor, round smiley visor, purple accents and star badge.
- `lasernick_grappler.png`: isolated silver/navy grappling launcher, cyan coils, three-prong hook and cable reel.

Prompt set: clean alpha silhouettes; preserve the supplied reference identities; purple plaits and white flowers for the trap; thick black cartoon outlines and glossy highlights for the bat, armor and grappler; no text or screenshot controls. The first five assets were extracted from the generated sprite sheet. Originals remain in the built-in generator output directory.

## Gameplay
Mrlovebraids lasts 10 minutes and features Hair Trap, Lasernick's Grappler and Durp Space Armor (incoming damage divided by 30). Fling Bat is in the normal shop. Jump Pad is the last item in the normal shop. New morphs have reversible selected-player controls in the troll panel.

Pileo Snap lasts 10 minutes, exposes the combined catalog from all events in both shops, and enables event abilities/armor. Birthday items remain usable without forcing players back to its gun. Pileo appears at spawn immediately during Snap, or after all 13 event choices have been started in a session. The completion display remains until the session ends.

New item prices: Hair Trap 150, Fling Bat 250, Lasernick's Grappler 300, Durp Space Armor 10000 Coins. Existing weapon shop VIP discounts apply; armor retains the existing exact-price rule.

Tests: test_mrlovebraids_content (PC and phone), test_mrlovebraids_bat_and_grappler (multiplayer PC), test_mrlovebraids_wall_and_hair_trap (multiplayer PC). Live UI and spawn art also inspected.

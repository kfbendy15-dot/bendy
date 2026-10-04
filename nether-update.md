# Avatar, travel, and Nether update

- Preserve the engine avatar outfit when switching to the custom emote/weapon rig. PileoHarse uses a white recolor palette with animated rainbow tint.
- Jumpscares are inside the Troll Panel; the existing shortcut opens that panel.
- Selected-player travel buttons send players to Normal Map, Backrooms, Splash, and Forest spawns; all reset momentum and world state.
- Claim Hunter enters World 4 (Nether). Survive 35 seconds against personal blaze rods and ghasts firing aimed fireballs, then teleport to the sanctuary to claim Lava.
- Lava is permitted by the badge/title allowlist, stored in the persistent badge inventory, and additionally restored from lava_badge_unlocked if needed. The sanctuary blocks weapon damage.
- Pair morph and jumpscare display names are now Mrlovebraids & Lily. The picture is unchanged: no Lily reference image was attached to this request.

## Verified locally
- Compilation succeeds.
- Actual Troll Panel buttons: Normal [0,0], Backrooms [0,30], Splash [100,-10], Forest [200,-13].
- Hunter interaction enters Nether; blaze rods and ghasts spawn with stable user-id ownership.
- Movement stops at the southern boundary without triggering an out-of-bounds fall.
- Survival moves to [444,-2], claim persists Lava, and the badge remains after restarting.
- A second player remains in their own world with independent survival state.

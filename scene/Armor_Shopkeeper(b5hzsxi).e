14
287762808833
2054998760
{
  "name": "Armor_Shopkeeper",
  "local_enabled": true,
  "local_position": {
    "X": -4.5000000000000000,
    "Y": 14
  },
  "local_rotation": 0,
  "local_scale": {
    "X": 1,
    "Y": 1
  },
  "previous_sibling": 2057679844
},
{
  "cid": 1,
  "aoid": 2050350497,
  "component_type": "Internal_Component",
  "internal_component_type": "Spine_Animator",
  "data": {
    "skeleton_data_asset": "013_shopkeep_78071c/013_shopkeep.spine",
    "ordered_skins": [
      "default"
    ],
    "initial_animation": "idle",
    "loop_initial_animation": true
  }
},
{
  "cid": 2,
  "aoid": 2059366751,
  "component_type": "Internal_Component",
  "internal_component_type": "Interactable",
  "data": {
    "text": "Armor Shop",
    "hold_text": "Open",
    "subtitle": "Armor",
    "radius": 4,
    "required_hold_time": 0,
    "prompt_offset": {
      "Y": 24
    }
  }
},
{
  "cid": 3,
  "aoid": 2050423261,
  "component_type": "Internal_Component",
  "internal_component_type": "Manipulable_Target",
  "data": {
    "hold_distance": 2,
    "lift_height": 1.1000000238418579
  }
},
{
  "cid": 5,
  "aoid": 2059721836,
  "component_type": "Internal_Component",
  "internal_component_type": "Armor_Shop_Interactable",
  "data": {
    "interactable": 2059366751
  }
}

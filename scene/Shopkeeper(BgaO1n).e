14
55834574849
1617489255
{
  "name": "Shopkeeper",
  "local_enabled": true,
  "local_position": {
    "Y": 14
  },
  "local_rotation": 0,
  "local_scale": {
    "X": 1,
    "Y": 1
  },
  "previous_sibling": 1625399302,
  "next_sibling": 1626483089
},
{
  "cid": 1,
  "aoid": 1615288312,
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
  "aoid": 2000000001,
  "component_type": "Internal_Component",
  "internal_component_type": "Interactable",
  "data": {
    "text": "Shop",
    "hold_text": "Open",
    "radius": 4,
    "required_hold_time": 0,
    "prompt_offset": {
      "Y": 24
    }
  }
},
{
  "cid": 3,
  "aoid": 1621031447,
  "component_type": "Internal_Component",
  "internal_component_type": "Manipulable_Target",
  "data": {
    "hold_distance": 2,
    "lift_height": 1.1000000238418579
  }
},
{
  "cid": 4,
  "aoid": 2054134057,
  "component_type": "Internal_Component",
  "internal_component_type": "Shopkeeper_Interactable",
  "data": {
    "interactable": 2000000001
  }
}

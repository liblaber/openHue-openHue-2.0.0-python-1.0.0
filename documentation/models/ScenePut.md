# ScenePut

**Properties**

| Name         | Type             | Required | Description                                                                          |
| :----------- | :--------------- | :------- | :----------------------------------------------------------------------------------- |
| type\_       | ScenePutType     | ❌       |                                                                                      |
| actions      | List[ActionPost] | ❌       | List of actions to be executed synchronously on recall                               |
| recall       | SceneRecall      | ❌       |                                                                                      |
| metadata     | SceneMetadata    | ❌       |                                                                                      |
| palette      | ScenePalette     | ❌       | Group of colors that describe the palette of colors to be used when playing dynamics |
| speed        | float            | ❌       | Speed of dynamic palette for this scene                                              |
| auto_dynamic | bool             | ❌       | Indicates whether to automatically start the scene dynamically on active recall      |

# ScenePutType

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| SCENE | str  | ✅       | "scene"     |

<!-- This file was generated by liblab | https://liblab.com/ -->

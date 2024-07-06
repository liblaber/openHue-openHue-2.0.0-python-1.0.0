# SceneService

A list of all methods in the `SceneService` service. Click on the method name to view detailed information about that method.

| Methods                       | Description                                              |
| :---------------------------- | :------------------------------------------------------- |
| [get_scenes](#get_scenes)     | List all available scenes                                |
| [create_scene](#create_scene) | Creates a new scene                                      |
| [get_scene](#get_scene)       | Get details of a single scene from its given `{sceneId}` |
| [update_scene](#update_scene) | Update a single scene from its given `{sceneId}`         |
| [delete_scene](#delete_scene) | Delete a single scene from its given `{sceneId}`         |

## get_scenes

List all available scenes

- HTTP Method: `GET`
- Endpoint: `/clip/v2/resource/scene`

**Return Type**

`GetScenesOkResponse`

**Example Usage Code Snippet**

```python
from open_hue import OpenHue, Environment

sdk = OpenHue(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.scene.get_scenes()

print(result)
```

## create_scene

Creates a new scene

- HTTP Method: `POST`
- Endpoint: `/clip/v2/resource/scene`

**Parameters**

| Name         | Type                                | Required | Description       |
| :----------- | :---------------------------------- | :------- | :---------------- |
| request_body | [ScenePost](../models/ScenePost.md) | ❌       | The request body. |

**Return Type**

`CreateSceneOkResponse`

**Example Usage Code Snippet**

```python
from open_hue import OpenHue, Environment
from open_hue.models import ScenePost

sdk = OpenHue(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = ScenePost(
    type_="scene",
    actions=[
        {
            "target": {
                "rid": "42edd1f5-9538-4180-9ced-2d9e07f26d0f",
                "rtype": "device"
            },
            "action": {
                "on": {
                    "on": False
                },
                "dimming": {
                    "brightness": 11.42
                },
                "color": {
                    "xy": {
                        "x": 0,
                        "y": 0.47
                    }
                },
                "color_temperature": {
                    "mirek": 163
                },
                "gradient": {
                    "points": [
                        {
                            "xy": {
                                "x": 0,
                                "y": 0.47
                            }
                        }
                    ],
                    "mode": "interpolated_palette"
                },
                "effects": {
                    "effect": "prism"
                },
                "dynamics": {
                    "duration": 7
                }
            }
        }
    ],
    metadata={
        "name": "aute null",
        "image": {
            "rid": "42edd1f5-9538-4180-9ced-2d9e07f26d0f",
            "rtype": "device"
        },
        "appdata": "magn"
    },
    group={
        "rid": "42edd1f5-9538-4180-9ced-2d9e07f26d0f",
        "rtype": "device"
    },
    palette={
        "color": [
            {
                "color": {
                    "xy": {
                        "x": 0,
                        "y": 0.47
                    }
                },
                "dimming": {
                    "brightness": 11.42
                }
            }
        ],
        "dimming": [
            {
                "brightness": 11.42
            }
        ],
        "color_temperature": [
            {
                "color_temperature": {
                    "mirek": 376
                },
                "dimming": {
                    "brightness": 11.42
                }
            }
        ],
        "effects": [
            {
                "effect": "prism"
            }
        ]
    },
    speed=0.93,
    auto_dynamic=True
)

result = sdk.scene.create_scene(request_body=request_body)

print(result)
```

## get_scene

Get details of a single scene from its given `{sceneId}`

- HTTP Method: `GET`
- Endpoint: `/clip/v2/resource/scene/{sceneId}`

**Parameters**

| Name     | Type | Required | Description      |
| :------- | :--- | :------- | :--------------- |
| scene_id | str  | ✅       | ID of the scene. |

**Return Type**

`GetSceneOkResponse`

**Example Usage Code Snippet**

```python
from open_hue import OpenHue, Environment

sdk = OpenHue(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.scene.get_scene(scene_id="sceneId")

print(result)
```

## update_scene

Update a single scene from its given `{sceneId}`

- HTTP Method: `PUT`
- Endpoint: `/clip/v2/resource/scene/{sceneId}`

**Parameters**

| Name         | Type                              | Required | Description       |
| :----------- | :-------------------------------- | :------- | :---------------- |
| request_body | [ScenePut](../models/ScenePut.md) | ❌       | The request body. |
| scene_id     | str                               | ✅       | ID of the scene.  |

**Return Type**

`UpdateSceneOkResponse`

**Example Usage Code Snippet**

```python
from open_hue import OpenHue, Environment
from open_hue.models import ScenePut

sdk = OpenHue(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = ScenePut(
    type_="scene",
    actions=[
        {
            "target": {
                "rid": "42edd1f5-9538-4180-9ced-2d9e07f26d0f",
                "rtype": "device"
            },
            "action": {
                "on": {
                    "on": False
                },
                "dimming": {
                    "brightness": 11.42
                },
                "color": {
                    "xy": {
                        "x": 0,
                        "y": 0.47
                    }
                },
                "color_temperature": {
                    "mirek": 163
                },
                "gradient": {
                    "points": [
                        {
                            "xy": {
                                "x": 0,
                                "y": 0.47
                            }
                        }
                    ],
                    "mode": "interpolated_palette"
                },
                "effects": {
                    "effect": "prism"
                },
                "dynamics": {
                    "duration": 7
                }
            }
        }
    ],
    recall={
        "action": "active",
        "duration": 7,
        "dimming": {
            "brightness": 11.42
        }
    },
    metadata={
        "name": "aute null",
        "image": {
            "rid": "42edd1f5-9538-4180-9ced-2d9e07f26d0f",
            "rtype": "device"
        },
        "appdata": "magn"
    },
    palette={
        "color": [
            {
                "color": {
                    "xy": {
                        "x": 0,
                        "y": 0.47
                    }
                },
                "dimming": {
                    "brightness": 11.42
                }
            }
        ],
        "dimming": [
            {
                "brightness": 11.42
            }
        ],
        "color_temperature": [
            {
                "color_temperature": {
                    "mirek": 376
                },
                "dimming": {
                    "brightness": 11.42
                }
            }
        ],
        "effects": [
            {
                "effect": "prism"
            }
        ]
    },
    speed=0.1,
    auto_dynamic=False
)

result = sdk.scene.update_scene(
    request_body=request_body,
    scene_id="sceneId"
)

print(result)
```

## delete_scene

Delete a single scene from its given `{sceneId}`

- HTTP Method: `DELETE`
- Endpoint: `/clip/v2/resource/scene/{sceneId}`

**Parameters**

| Name     | Type | Required | Description      |
| :------- | :--- | :------- | :--------------- |
| scene_id | str  | ✅       | ID of the scene. |

**Return Type**

`DeleteSceneOkResponse`

**Example Usage Code Snippet**

```python
from open_hue import OpenHue, Environment

sdk = OpenHue(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.scene.delete_scene(scene_id="sceneId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->

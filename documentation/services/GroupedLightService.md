# GroupedLightService

A list of all methods in the `GroupedLightService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                              |
| :-------------------------------------------- | :----------------------------------------------------------------------- |
| [get_grouped_lights](#get_grouped_lights)     | List all grouped lights                                                  |
| [get_grouped_light](#get_grouped_light)       | Get details of a single grouped light from its given `{groupedLightId}`. |
| [update_grouped_light](#update_grouped_light) | Update a single grouped light from its given `{groupedLightId}`.         |

## get_grouped_lights

List all grouped lights

- HTTP Method: `GET`
- Endpoint: `/clip/v2/resource/grouped_light`

**Return Type**

`GetGroupedLightsOkResponse`

**Example Usage Code Snippet**

```python
from open_hue import OpenHue, Environment

sdk = OpenHue(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.grouped_light.get_grouped_lights()

print(result)
```

## get_grouped_light

Get details of a single grouped light from its given `{groupedLightId}`.

- HTTP Method: `GET`
- Endpoint: `/clip/v2/resource/grouped_light/{groupedLightId}`

**Parameters**

| Name             | Type | Required | Description             |
| :--------------- | :--- | :------- | :---------------------- |
| grouped_light_id | str  | ✅       | ID of the grouped light |

**Return Type**

`GetGroupedLightOkResponse`

**Example Usage Code Snippet**

```python
from open_hue import OpenHue, Environment

sdk = OpenHue(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.grouped_light.get_grouped_light(grouped_light_id="groupedLightId")

print(result)
```

## update_grouped_light

Update a single grouped light from its given `{groupedLightId}`.

- HTTP Method: `PUT`
- Endpoint: `/clip/v2/resource/grouped_light/{groupedLightId}`

**Parameters**

| Name             | Type                                            | Required | Description       |
| :--------------- | :---------------------------------------------- | :------- | :---------------- |
| request_body     | [GroupedLightPut](../models/GroupedLightPut.md) | ❌       | The request body. |
| grouped_light_id | str                                             | ✅       | ID of the light   |

**Return Type**

`UpdateGroupedLightOkResponse`

**Example Usage Code Snippet**

```python
from open_hue import OpenHue, Environment
from open_hue.models import GroupedLightPut

sdk = OpenHue(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = GroupedLightPut(
    type_="grouped_light",
    on={
        "on": False
    },
    dimming={
        "brightness": 11.42
    },
    dimming_delta={
        "action": "up",
        "brightness_delta": 56.69
    },
    color_temperature={
        "mirek": 360
    },
    color_temperature_delta={
        "action": "up",
        "mirek_delta": 121
    },
    color={
        "xy": {
            "x": 0,
            "y": 0.47
        }
    },
    alert={
        "action": "breathe"
    },
    signaling={
        "signal": "no_signal",
        "duration": 53090288,
        "color": [
            {
                "xy": {
                    "x": 0,
                    "y": 0.47
                }
            }
        ]
    },
    dynamics={
        "duration": 7
    }
)

result = sdk.grouped_light.update_grouped_light(
    request_body=request_body,
    grouped_light_id="groupedLightId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->

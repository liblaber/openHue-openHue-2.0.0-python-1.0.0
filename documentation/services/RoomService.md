# RoomService

A list of all methods in the `RoomService` service. Click on the method name to view detailed information about that method.

| Methods                     | Description                                            |
| :-------------------------- | :----------------------------------------------------- |
| [get_rooms](#get_rooms)     | List all available rooms                               |
| [create_room](#create_room) | Create a new room                                      |
| [get_room](#get_room)       | Get details of a single room from its given `{roomId}` |
| [update_room](#update_room) | Update a single room from its given `{roomId}`         |
| [delete_room](#delete_room) | Delete a single room from its given `{roomId}`         |

## get_rooms

List all available rooms

- HTTP Method: `GET`
- Endpoint: `/clip/v2/resource/room`

**Return Type**

`GetRoomsOkResponse`

**Example Usage Code Snippet**

```python
from open_hue import OpenHue, Environment

sdk = OpenHue(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.room.get_rooms()

print(result)
```

## create_room

Create a new room

- HTTP Method: `POST`
- Endpoint: `/clip/v2/resource/room`

**Parameters**

| Name         | Type                            | Required | Description       |
| :----------- | :------------------------------ | :------- | :---------------- |
| request_body | [RoomPut](../models/RoomPut.md) | ❌       | The request body. |

**Return Type**

`CreateRoomOkResponse`

**Example Usage Code Snippet**

```python
from open_hue import OpenHue, Environment
from open_hue.models import RoomPut

sdk = OpenHue(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = RoomPut(
    type_="type",
    children=[
        {
            "rid": "42edd1f5-9538-4180-9ced-2d9e07f26d0f",
            "rtype": "device"
        }
    ],
    metadata={
        "name": "name",
        "archetype": "living_room"
    }
)

result = sdk.room.create_room(request_body=request_body)

print(result)
```

## get_room

Get details of a single room from its given `{roomId}`

- HTTP Method: `GET`
- Endpoint: `/clip/v2/resource/room/{roomId}`

**Parameters**

| Name    | Type | Required | Description    |
| :------ | :--- | :------- | :------------- |
| room_id | str  | ✅       | ID of the room |

**Return Type**

`GetRoomOkResponse`

**Example Usage Code Snippet**

```python
from open_hue import OpenHue, Environment

sdk = OpenHue(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.room.get_room(room_id="roomId")

print(result)
```

## update_room

Update a single room from its given `{roomId}`

- HTTP Method: `PUT`
- Endpoint: `/clip/v2/resource/room/{roomId}`

**Parameters**

| Name         | Type                            | Required | Description       |
| :----------- | :------------------------------ | :------- | :---------------- |
| request_body | [RoomPut](../models/RoomPut.md) | ❌       | The request body. |
| room_id      | str                             | ✅       | ID of the room    |

**Return Type**

`UpdateRoomOkResponse`

**Example Usage Code Snippet**

```python
from open_hue import OpenHue, Environment
from open_hue.models import RoomPut

sdk = OpenHue(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = RoomPut(
    type_="type",
    children=[
        {
            "rid": "42edd1f5-9538-4180-9ced-2d9e07f26d0f",
            "rtype": "device"
        }
    ],
    metadata={
        "name": "name",
        "archetype": "living_room"
    }
)

result = sdk.room.update_room(
    request_body=request_body,
    room_id="roomId"
)

print(result)
```

## delete_room

Delete a single room from its given `{roomId}`

- HTTP Method: `DELETE`
- Endpoint: `/clip/v2/resource/room/{roomId}`

**Parameters**

| Name    | Type | Required | Description    |
| :------ | :--- | :------- | :------------- |
| room_id | str  | ✅       | ID of the room |

**Return Type**

`DeleteRoomOkResponse`

**Example Usage Code Snippet**

```python
from open_hue import OpenHue, Environment

sdk = OpenHue(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.room.delete_room(room_id="roomId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->

# MotionPut

**Properties**

| Name        | Type                 | Required | Description                                               |
| :---------- | :------------------- | :------- | :-------------------------------------------------------- |
| type\_      | str                  | ❌       | Type of the supported resources (always `motion` here)    |
| enabled     | bool                 | ❌       | true when the sensor is activated, false when deactivated |
| sensitivity | MotionPutSensitivity | ❌       |                                                           |

# MotionPutSensitivity

**Properties**

| Name        | Type | Required | Description                                                         |
| :---------- | :--- | :------- | :------------------------------------------------------------------ |
| sensitivity | int  | ❌       | Sensitivity of the sensor. Value in the range 0 to sensitivity_max. |

<!-- This file was generated by liblab | https://liblab.com/ -->

# Powerup

Feature containing properties to configure powerup behaviour of a lightsource.

**Properties**

| Name       | Type            | Required | Description                                                                                                                      |
| :--------- | :-------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------- |
| preset     | PowerupPreset2  | ❌       | When setting the custom preset the additional properties can be set. For all other presets, no other properties can be included. |
| configured | bool            | ❌       | Indicates if the shown values have been configured in the lightsource.                                                           |
| on         | PowerupOn2      | ❌       |                                                                                                                                  |
| dimming    | PowerupDimming2 | ❌       |                                                                                                                                  |

# PowerupPreset_2

When setting the custom preset the additional properties can be set. For all other presets, no other properties can be included.

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| SAFETY        | str  | ✅       | "safety"        |
| POWERFAIL     | str  | ✅       | "powerfail"     |
| LAST_ON_STATE | str  | ✅       | "last_on_state" |
| CUSTOM        | str  | ✅       | "custom"        |

# PowerupOn_2

**Properties**

| Name | Type    | Required | Description                                                                                                                                                                                                                                                                                 |
| :--- | :------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mode | OnMode2 | ❌       | State to activate after powerup. On will use the value specified in the “on” property. When setting mode “on”, the on property must be included. Toggle will alternate between on and off on each subsequent power toggle. Previous will return to the state it was in before powering off. |
| on   | On      | ❌       |                                                                                                                                                                                                                                                                                             |

# OnMode_2

State to activate after powerup.
On will use the value specified in the “on” property.
When setting mode “on”, the on property must be included.
Toggle will alternate between on and off on each subsequent power toggle.
Previous will return to the state it was in before powering off.

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| ON       | str  | ✅       | "on"        |
| TOGGLE   | str  | ✅       | "toggle"    |
| PREVIOUS | str  | ✅       | "previous"  |

# PowerupDimming_2

**Properties**

| Name    | Type          | Required | Description                                                                                                                                                                                                         |
| :------ | :------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mode    | DimmingMode2  | ❌       | Dimming will set the brightness to the specified value after power up. When setting mode “dimming”, the dimming property must be included. Previous will set brightness to the state it was in before powering off. |
| dimming | float         | ❌       | Brightness percentage. value cannot be 0, writing 0 changes it to lowest possible brightness                                                                                                                        |
| color   | DimmingColor2 | ❌       |                                                                                                                                                                                                                     |

# DimmingMode_2

Dimming will set the brightness to the specified value after power up.
When setting mode “dimming”, the dimming property must be included.
Previous will set brightness to the state it was in before powering off.

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| DIMMING  | str  | ✅       | "dimming"   |
| PREVIOUS | str  | ✅       | "previous"  |

# DimmingColor_2

**Properties**

| Name              | Type                   | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :---------------- | :--------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mode              | ColorMode2             | ❌       | State to activate after powerup. Availability of “color_temperature” and “color” modes depend on the capabilities of the lamp. Colortemperature will set the colortemperature to the specified value after power up. When setting color_temperature, the color_temperature property must be included Color will set the color tot he specified value after power up. When setting color mode, the color property must be included Previous will set color to the state it was in before powering off. |
| color_temperature | ColorColorTemperature2 | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

# ColorMode_2

State to activate after powerup. Availability of “color_temperature” and “color” modes depend on the capabilities of the lamp. Colortemperature will set the colortemperature to the specified value after power up. When setting color_temperature, the color_temperature property must be included Color will set the color tot he specified value after power up. When setting color mode, the color property must be included Previous will set color to the state it was in before powering off.

**Properties**

| Name              | Type | Required | Description         |
| :---------------- | :--- | :------- | :------------------ |
| COLOR_TEMPERATURE | str  | ✅       | "color_temperature" |
| COLOR             | str  | ✅       | "color"             |
| PREVIOUS          | str  | ✅       | "previous"          |

# ColorColorTemperature_2

**Properties**

| Name  | Type  | Required | Description                                                                       |
| :---- | :---- | :------- | :-------------------------------------------------------------------------------- |
| mirek | int   | ❌       | color temperature in mirek or null when the light color is not in the ct spectrum |
| color | Color | ❌       |                                                                                   |

<!-- This file was generated by liblab | https://liblab.com/ -->

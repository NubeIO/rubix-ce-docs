---
sidebar_position: 7
---

# Payload
Set payload is used only when the user wants to send a value to wires runtime without needing to re-download the flow

The main use cause is when commissioning a program and you want to adjust for example a setpoint


:::caution
When sending a payload value to the wires runtime the payload will not be kept on restart of the device or if a new program is re-downloaded 
:::

## Supported nodes

- const-num
- const-bool
- const-string


:::tip
To remove the existing payload value **right-click** on the node and click on **Release Payload** <br/>
This will revert to the default input node value
:::

![set-payload.png](img/set-payload.png)
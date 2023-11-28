---
sidebar_position: 2
---

# Methods



## Common Methods to Rubix OS (ROS)

- Get, Edit, Delete, Add for `networks, devices and points`

```
inst.grpcMarshaller
```

### Example
```go
func (inst *Module) networkUpdateSuccess(uuid string) error {
	var network model.Network
	network.InFault = false
	network.MessageLevel = model.MessageLevel.Info
	network.MessageCode = model.CommonFaultCode.Ok
	network.Message = model.CommonFaultMessage.NetworkMessage
	network.LastOk = time.Now().UTC()
	err := inst.grpcMarshaller.UpdateNetworkErrors(uuid, &network)
	if err != nil {
		log.Error(bugs.DebugPrint(name, inst.networkUpdateSuccess, err))
	}
	return err
}
```

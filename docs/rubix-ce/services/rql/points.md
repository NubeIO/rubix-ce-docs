---
sidebar_position: 3
---


# Points

## Methods

### GetPoints

**Description:** Retrieves points from the Rubix-OS API for the given host ID name.

**Parameters:**

- `hostIDName` (string): The ID or name of the host from which to retrieve points.

**Returns:** (`any`): Returns the response containing the points if successful; otherwise, returns an error.

---

### GetNetworkByModuleName

**Description:** Fetches the network by the given module name for the specified host ID.

**Parameters:**

- `hostIDName` (string): The host ID or name.
- `moduleName` (string): The module name.

**Returns:** (`any`): Returns the response containing the network details if successful; otherwise, returns an error.

---

### GetPointsByModuleName

**Description:** Gets the points associated with a specific module name for a given host ID or name.

**Parameters:**

- `hostIDName` (string): The host ID or name.
- `moduleName` (string): The module name.

**Returns:** (`any`): Returns a slice of pointers to `model.Point` objects if successful; otherwise, returns an error.

---

### GetPointsByModuleAllHosts

**Description:** Retrieves points by module for all hosts. It constructs an output of all host data, including points, errors, and counts.

**Parameters:**

- `moduleName` (string): The module name to retrieve points for across all hosts.

**Returns:** (`any`): Returns a slice of `AllHostsPointsByModule` structs, each containing host and points data, or an error if retrieval fails.

---

### GetPointsAllHosts

**Description:** Calculates and retrieves the points for all hosts in the RQL instance.

**Returns:** (`any`): Returns a slice of `AllHostsPoints` structs containing points data for all hosts or an error if there was a problem retrieving the hosts.

---

### GetPoint

**Description:** Retrieves a point from the RQL instance using the specified host ID name and UUID.

**Parameters:**

- `hostIDName` (string): The host ID or name.
- `uuid` (string): The UUID of the point to retrieve.

**Returns:** (`any`): Returns the point data if successful; otherwise, returns an error.

---

### WritePointValue

**Description:** Writes a point value to the specified host and UUID.

**Parameters:**

- `hostIDName` (string): The host ID or name where the point is located.
- `uuid` (string): The UUID of the point to be written.
- `value` (*model.Priority): The value to write to the point.

**Returns:** (`any`): Returns the response from the write operation if successful; otherwise, returns an error.

---

### WritePointValuePriority

**Description:** Writes a point value with a specified priority to a host and UUID.

**Parameters:**

- `hostIDName` (string): The host ID or name where the point is located.
- `uuid` (string): The UUID of the point to be written.
- `pri` (int): The priority of the point value.
- `value` (float64): The value to write.

**Returns:** (`any`): Returns `true` if the write is successful; otherwise, returns an error.

---


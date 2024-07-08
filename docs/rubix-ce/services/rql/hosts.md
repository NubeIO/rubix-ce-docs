---
sidebar_position: 3
---


# Hosts

## Methods

### GetHosts

**Description:** Retrieves a list of hosts from the system, potentially filtered by specific arguments provided.

**Parameters:**

- `args` (`nargs.Args`): Arguments to filter the list of hosts. This can include filters such as host status or other attributes.

**Returns:** (`any`): Returns a list of hosts if successful; otherwise, returns an error.

---

### GetGroups

**Description:** Retrieves network groups from the system, which are collections of hosts organized by network.

**Returns:** (`any`): Returns a list of host networks if successful; otherwise, returns an error.

---

### GetAllHostsStatus

**Description:** Retrieves the status of all hosts across all groups in the system. This method first fetches all groups and then queries the status for the hosts within each group.

**Returns:** (`any`): Returns a list of updated host status for all groups if successful; otherwise, returns an error.

---

### GetHostsStatus

**Description:** Retrieves the status of hosts within a specific group identified by its UUID.

**Parameters:**

- `groupUUID` (string): The UUID of the group for which the host status is requested.

**Returns:** (`any`): Returns the host status for the specified group if successful; otherwise, returns an error.

---

These methods provide functionalities for managing and retrieving data about hosts and groups within the system, enabling detailed monitoring and management of networked resources. Each method is documented with its purpose, input parameters, and expected outcomes.
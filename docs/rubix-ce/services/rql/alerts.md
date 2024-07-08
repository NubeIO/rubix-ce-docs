---
sidebar_position: 3
---

# Alerts

[See example](examples.md/#1-alerts)

See the example script to add an alert

## Methods

### GetAlerts

**Description:** Retrieves alerts from the system that are in the states of active, acknowledged, or closed.

**Returns:** (`any`): Returns the list of alerts if successful; otherwise, returns an error.

---

### GetAlertsByHost

**Description:** Retrieves alerts for each host, categorized by status (active, acknowledged, closed), and provides a count for each category along with the total number of alerts.

**Returns:** (`any`): Returns a slice of `alertsByHost` structs, each containing alert data grouped by status for each host, or an error if the retrieval fails.

---

### AddAlert

**Description:** Adds an alert to the system for the specified host based on the details provided in the alert body.

**Parameters:**

- `hostIDName` (string): The host ID or name where the alert is to be added.
- `body` (any): The data structure containing alert details such as host UUID, entity type, alert type, status, and severity.

**Returns:** (`any`): Returns the alert creation response if successful; otherwise, returns an error.

---

### UpdateAlertStatus

**Description:** Updates the status of a specific alert for a given host and alert UUID.

**Parameters:**

- `hostIDName` (string): The host ID or name where the alert exists.
- `uuid` (string): The UUID of the alert to be updated.
- `status` (string): The new status to be set for the alert (e.g., "active", "acknowledged", "closed").

**Returns:** (`any`): Returns the alert update response if successful; otherwise, returns an error.

---

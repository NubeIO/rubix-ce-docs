---
sidebar_position: 3
---
# Numbers

## Mathematical and Utility Functions

### RandInt

**Description:** Generates a random integer within a specified range.

**Parameters:**

- `range1` (`int`): One bound of the range.
- `range2` (`int`): The other bound of the range.

**Returns:** (`int`): A random integer within the inclusive range defined by `range1` and `range2`.

---

### RandFloat

**Description:** Generates a random `float64` within a specified range, rounded to two decimal places.

**Parameters:**

- `range1` (`float64`): One bound of the range.
- `range2` (`float64`): The other bound of the range.

**Returns:** (`float64`): A random float within the range defined by `range1` and `range2`, rounded to two decimal places.

---

### LimitToRange

**Description:** Restricts a given value to lie within a specified range.

**Parameters:**

- `value` (`float64`): The value to be limited.
- `range1` (`float64`): One bound of the range.
- `range2` (`float64`): The other bound of the range.

**Returns:** (`float64`): The input value constrained within the range defined by `range1` and `range2`.

---

### RoundTo

**Description:** Rounds a given float to a specified number of decimal places.

**Parameters:**

- `value` (`float64`): The value to round.
- `decimals` (`uint32`): The number of decimal places to round to.

**Returns:** (`float64`): The rounded value.

---

### Scale

**Description:** Scales a given value from one range to another.

**Parameters:**

- `value` (`float64`): The value to scale.
- `inMin` (`float64`): The minimum of the input range.
- `inMax` (`float64`): The maximum of the input range.
- `outMin` (`float64`): The minimum of the output range.
- `outMax` (`float64`): The maximum of the output range.

**Returns:** (`float64`): The value scaled from the input range to the output range, constrained within the bounds of the output range if necessary.

---


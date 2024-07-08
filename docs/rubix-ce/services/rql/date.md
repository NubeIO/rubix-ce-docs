---
sidebar_position: 3
---
# Date/Time Helpers

## Methods

### SubtractYears

**Description:** Subtracts a specified number of years from a given time.

**Parameters:**

- `t` (`time.Time`): The original time from which to subtract years.
- `years` (`int`): The number of years to subtract.

**Returns:** (`time.Time`): The resulting time after subtracting the specified number of years.

---

### SubtractDays

**Description:** Subtracts a specified number of days from a given time.

**Parameters:**

- `t` (`time.Time`): The original time from which days are subtracted.
- `days` (`int`): The number of days to subtract.

**Returns:** (`time.Time`): The resulting time after subtracting the specified number of days.

---

### SubtractHours

**Description:** Subtracts a specified number of hours from a given time.

**Parameters:**

- `t` (`time.Time`): The original time from which hours are subtracted.
- `hours` (`int`): The number of hours to subtract.

**Returns:** (`time.Time`): The resulting time after subtracting the specified number of hours.

---

### SubtractMinutes

**Description:** Subtracts a specified number of minutes from a given time.

**Parameters:**

- `t` (`time.Time`): The original time from which minutes are subtracted.
- `minutes` (`int`): The number of minutes to subtract.

**Returns:** (`time.Time`): The resulting time after subtracting the specified number of minutes.

---

### SubtractSeconds

**Description:** Subtracts a specified number of seconds from a given time.

**Parameters:**

- `t` (`time.Time`): The original time from which seconds are subtracted.
- `seconds` (`int`): The number of seconds to subtract.

**Returns:** (`time.Time`): The resulting time after subtracting the specified number of seconds.

---

### AddYears

**Description:** Adds a specified number of years to a given time.

**Parameters:**

- `t` (`time.Time`): The original time to which years are added.
- `years` (`int`): The number of years to add.

**Returns:** (`time.Time`): The resulting time after adding the specified number of years.

---

### AddDays

**Description:** Adds a specified number of days to a given time.

**Parameters:**

- `t` (`time.Time`): The original time to which days are added.
- `days` (`int`): The number of days to add.

**Returns:** (`time.Time`): The resulting time after adding the specified number of days.

---

### AddHours

**Description:** Adds a specified number of hours to a given time.

**Parameters:**

- `t` (`time.Time`): The original time to which hours are added.
- `hours` (`int`): The number of hours to add.

**Returns:** (`time.Time`): The resulting time after adding the specified number of hours.

---

### AddMinutes

**Description:** Adds a specified number of minutes to a given time.

**Parameters:**

- `t` (`time.Time`): The original time to which minutes are added.
- `minutes` (`int`): The number of minutes to add.

**Returns:** (`time.Time`): The resulting time after adding the specified number of minutes.

---

### AddSeconds

**Description:** Adds a specified number of seconds to a given time.

**Parameters:**

- `t` (`time.Time`): The original time to which seconds are added.
- `seconds` (`int`): The number of seconds to add.

**Returns:** (`time.Time`): The resulting time after adding the specified number of seconds.

---

### TimeSince

**Description:** Calculates the time duration that has elapsed since the given time and returns it in a human-readable format.

**Parameters:**

- `t` (`time.Time`): The original time for which the duration is calculated.

**Returns:** (`string`): A human-readable representation of the elapsed time, such as "now", "x seconds ago", "x minutes ago", etc.

---

### currentTime

**Description:** Returns the current time in UTC format.

**Returns:** (`time.Time`): The current time in UTC.

---

### formattedCurrentTime

**Description:** Returns the current time formatted according to the specified format.

**Parameters:**

- `format` (`string`): The desired format string for the time representation.

**Returns:** (`string`): The current time formatted as specified.

---

### TimeUTC

**Description:** Returns the current time in UTC format.

**Returns:** (`time.Time`): The current UTC time.

---

### TimeDate

**Description:** Returns the current time formatted as "2006-01-02 15:04:05".

**Returns:** (`string`): The current time as a formatted string.

---

### TimeWithMilliseconds

**Description:** Returns the current time with milliseconds, formatted as "15:04:05.000".

**Returns:** (`string`): The current time as a formatted string including milliseconds.

---

### Time

**Description:** Returns the current time formatted as "15:04:05".

**Returns:** (`string`): The current time as a formatted string.

---

### Date

**Description:** Returns the current date formatted as "2006.01.02".

**Returns:** (`string`): The current date as a formatted string.

---

### Year

**Description:** Returns the current year formatted as "2006".

**Returns:** (`string`): The current year as a formatted string.

---

### Day

**Description:** Returns the current day of the week formatted as "Monday".

**Returns:** (`string`): The current day of the week as a formatted string.

---

### TimeDateDay

**Description:** Returns the formatted current time using the format "2006-01-02 15:04:05 Monday".

**Returns:** (`string`): The current time and day as a formatted string.

---

### ParseDateTime

**Description:** Parses the given date string and returns the corresponding `time.Time` value. Returns a zero value if the string is not in a valid format.

**Parameters:**

- `dateStr` (`string`): The date string to be parsed.

**Returns:** (`time.Time`): The time value corresponding to the parsed date string, or a zero time value if the format is invalid.

---

### GetDifference

**Description:** Calculates the time difference between two given times in various units (seconds, minutes, hours, days, years).

**Parameters:**

- `time1` (`time.Time`): The start time.
- `time2` (`time.Time`): The end time.

**Returns:** (`TimeDiff`): A struct containing the time differences in various units.

---


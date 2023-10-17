---
sidebar_position: 2
---

# JavaScript

# Methods

## Strings

### toString

```js
toString()
```

## Numbers

### parseInt

```js
parseInt()
```

### parseFloat

```js
parseFloat()
```

## Arrays

### push
The push() method of Array instances adds the specified elements to the end of an array and returns the new length of the array.

```js
push()
```

```js
let animals = ["pigs", "goats", "sheep"]
animals.push("chickens", "cats", "dogs")
RQL.Result = animals
```

### remove an item

```js
function removeItemOnce(arr, value) {
  var index = arr.indexOf(value);
  if (index > -1) {
    arr.splice(index, 1);
  }
  return arr;
}

let animals = ["pigs", "goats", "sheep"];

removeItemOnce(animals, "pigs");

RQL.Result = animals;
```

# Examples

## For Loop

```js
const array1 = [1, 2, 10];
let a = 0;

for (const element of array1) {
  a = a + element;
}

RQL.Result = a;
```




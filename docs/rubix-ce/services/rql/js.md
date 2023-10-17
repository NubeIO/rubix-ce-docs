---
sidebar_position: 2
---

# JavaScript
RQL uses javascript syntax. 

RQL is an implementation of ECMAScript 5.1.

RQL is a Synchronous blocking architecture, so the execution of each operation depends on completing the one before it. Each task requires an answer before moving on to the next iteration.

:::tip
no external npm library's can be used. <br/>
for example you cant use `momentjs` <br/>
most Global JS objects and methods are supported **[mozilla developer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects)**
:::

:::caution
setTimeout() is not support, you can use `RQL.Sleep(100)`
:::


# Methods

## Strings

**[docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)**


### toString

```js
toString()
```

## Numbers

### parseInt

**[docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)**

```js
parseInt()
```

### parseFloat

**[docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat)**


```js
parseFloat()
```

## Arrays

**[docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)**


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

## regex

```js
function isValidIP(str) {
  const octet = "(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)";
  const regex = new RegExp(`^${octet}\\.${octet}\\.${octet}\\.${octet}$`);
  return regex.test(str);
}

RQL.Result = isValidIP("192.168.15.10").toString();
```

## Function
**[docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)**


```js
function calcRectArea(width, height) {
  return width * height;
}
```


## For Loop

**[docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)**


```js
const array1 = [1, 2, 10];
let a = 0;

for (const element of array1) {
  a = a + element;
}

RQL.Result = a;
```

## if/else

**[docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)**

```js
let a = 10
let result = ""
if (a > 0) {
    result = 'positive';
} else {
    result = 'NOT positive';
}
```

## SwitchCase

**[docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)**

```js
const expr = "b";
let a = "";
switch (expr) {
  case "a":
    a = "is a";
    break;
  case "b":
    a = "is b";
    break;
  default:
    a = "nada";
}

RQL.Result = a;
```
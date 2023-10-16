---
sidebar_position: 1
---

# RQL
RQL means Rubix-Query-Language. The main use case for using RQL is to write rules and then run the rules and a set time interval. And example use case is to ping a device every 15min to see if its online

## About
Rules can be written in a javaScript like syntax and then executed in the RQL runtime

![rql.png](img/rql.png)


## Quick example

```js
let getTime = RQL.Time() // will get current time from the RQL server
RQL.Result = getTime; // any value sent to RQL.Result will be returned to view in the editor and also stored as logs
```


## Variables 

```js
let data = RQL.UpdateVariableValue("test", 11.333); // update by its name or uuid
RQL.Result = data;
```


---
sidebar_position: 1
---

# RQL
RQL means Rubix Query Language. The main use case for using RQL is to write rules and then run the rules and a set time interval. An example use case is to ping a device every 15min to see if it is online.

RQL is a `Synchronous` blocking architecture, so the execution of each operation depends on completing the one before it. Each task requires an answer before moving on to the next iteration.

:::info Important things to note before proceeding:
* Install required **[modules/plugins](../../setup/plugins.md)** **module-core-rql**
:::


## About
Rules can be written in a javaScript similar to syntax and then executed in the RQL runtime.

![rql.png](img/rql.png)


## Example

```js
function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

RQL.Result = getRandomInt(100);
```


```js
let getTime = RQL.Time() // will get current time from the RQL server
RQL.Result = getTime; // any value sent to RQL.Result will be returned to view in the editor and also stored as logs
```


## Variables 
The idea of a variable is it can be used across multiple rules/scripts rather than hard coding a variable within your rule code

### Add a variable
1. Open the `Variables` tab
2. Click on the green `+` icon and add the name and value

### Useing a Variable in Your Code

```js
let data = RQL.UpdateVariableValue("test", 11.333); // update by its name or uuid
RQL.Result = data;
```

## Running Rules on Timed Interval

To set a rule/script to run on a time interval do the following
1. Open the `Scripts` tab
2. Right-click on the rule/script that you wish to view the logs and click on `Edit`.
3. Toggle `Enable Schedule`
4. Select the time duration as a number and the time settings as `seconds, minutes, hours or days`


### View Rule Logs

1. Open the `Scripts` tab
2. Right-click on the rule/script that you wish to view the logs and click on `Scheduled Results`. 


### Call the Logs in a Rule/Script
[example to call logs](rqlFunctions.md#getrulelogs)


## Serverless Functions
A rule can be written and called from an external endpoint and a body can be passed in for data to be processed

### Usage
- Add a new script called `test` and paste in the example code below
- Call the end point below as per the curl example. (the endpoint is called by passing in the script name)

### Example RQL code
```js
let x = Input.Body.a;
let y = RQL.RandInt(10, 20);
let calc = x + y;
let out = {
  inputValue: x,
  randomNumber: y,
  calc: calc,
};

RQL.Result = out;
```

### HTTP Body
```json
{
    "body":{
        "a":100
    }
}
```

### Call the Endpoint to Execute the Rule
- method `POST`
- body `JSON`
```
curl -i -X POST -H "Content-Type: application/json" -d '{"body":{"a":100}}' http://0.0.0.0:1660/api/modules/module-core-rql/rules/run/test
```



## Example JavaScript Functions



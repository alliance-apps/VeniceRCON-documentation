Entry point of a Plugin looks like following:

```javascript
//as an entry point a function should be exported
//this will receive a single argument as object with following properteis
// config - config which can be set via webinterface
// battlefield - the battlefield rcon instance
module.exports = async ({ config, battlefield }) => {
  // will log { foo: 1, bar: 2 }
  console.log(config)
  //logs the current battlefield server infos
  console.log(await battlefield.serverInfo())
}
```
Entry point of a Plugin looks like following:

```javascript
//as an entry point a function should be exported
//this will receive a single argument as object with following properteis
// config - config which can be set via webinterface
// battlefield - the battlefield rcon instance
// logger - logger instance has methods `info`, `warn`, `error` which will be sent to frontend logging
module.exports = async ({ config, battlefield, logger }) => {
  // will log { foo: 1, bar: 2 }
  logger.info(config)
  //logs the current battlefield server infos
  logger.info(await battlefield.serverInfo())
}
```
A Plugin should export a single function which receives a single argument which consists of following parameters:


#### Config Properties

These are the keys which you receive as first argument of your function callback

name         | type
-------------|----------
config       | Object
battlefield  | [Battlefield](https://github.com/Multivit4min/vu-rcon)
dependency   | Object
logger       | [Logger](types/Logger.md)
router       | [PluginRouter](types/PluginRouter.md)
store        | [PluginStore](types/PluginStore.md)
engine       | [Engine](types/Engine.md)



```javascript
module.exports = ({ logger }) => {
  logger.info("Hello from plugin test")
  router.get("somename", ({ next }) -> next({ message: "Hello from the plugin" }))
}
```
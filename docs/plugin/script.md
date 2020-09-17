A Plugin should export a single function which receives a single argument which consists of following parameters:

```typescript
export interface PluginProps {
  /** config parameters from the webinterface */
  config: Record<string, any>
  /** the vu-rcon instance */
  battlefield: Battlefield
  /** declared dependencies from other modules */
  dependency: Record<string, any>
  /** logger instance */
  logger: Logger
  /** router instance */
  router: PluginRouter
}
```

```javascript
/**
 * @param {PluginProps} data
 */
module.exports = ({ logger }) => {
  logger.info("Hello from plugin test")
  router.get("somename", ({ next }) => next({ message: "Hello from the plugin" }))
}
```
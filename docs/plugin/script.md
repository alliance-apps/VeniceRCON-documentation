Entry point of a Plugin looks like following:

```javascript
/**
 * @typedef {Object} Logger
 * @property {(message: string) => void} info
 * @property {(message: string) => void} warn
 * @property {(message: string) => void} error
 */

/**
 * 
 * @param {object} data
 * @param {Record<string, any>} data.config configuration with the key value pairs from meta.yaml
 * @param {Battlefield} data.battlefield rcon connection to the battlefield server see https://github.com/Multivit4min/vu-rcon
 * @param {object} data.dependency optional depdendencies which has been defined in meta.yaml
 * @param {Logger} logger logger instance to log messages to frontend and database
 */
module.exports = ({ logger }) => {
  logger.info("Hello from plugin test")
}
```
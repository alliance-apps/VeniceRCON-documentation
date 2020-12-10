A Plugin should export a single function which receives a single argument which consists of following parameters:


#### Config Properties

These are the keys which you receive as first argument of your function callback

name         | type
-------------|----------
config       | Object
battlefield  | [Battlefield](https://multivit4min.github.io/vu-rcon/)
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

##### Custom Commands

Venice Unleashed might implement custom commands for rcon which are being provided by mods, in order to use non default commands you can do it with the `battlefield.createCommand` function:

```javascript
battlefield
  //sends the command "player.isAlive" with a single argument
  //consecutive arguments can be set by adding another argument to the 
  //createCommand function
  .createCommand("player.isAlive", name)
  //this function sets how the response will be formatted
  //by default this callback gets called with an array of "Words"
  //when you do not expect a response you can omit this line
  //documentation about a "Word" can be found here:
  //https://multivit4min.github.io/vu-rcon/classes/word.html
  .format(words => words[0].toBoolean())
  //this finally dispatches the command and sends it to the server
  //this function returns a promise which gets resolved and has the
  //response from the format callback
  .send()

```


##### Custom Events

All Events which are not recognized by the query will be dispatched via the catchall event named `"event"`:

```javascript
//register an eventhandler with name "event"
battlefield.on("event", ({ event, words }) => {
  /* this logs the event name which has been called */
  console.log(event)
  /** 
    * this is an array of words
    * documentation what properties a Word has can be found here: 
    * https://multivit4min.github.io/vu-rcon/classes/word.html
    */
  console.log(words)
})
```
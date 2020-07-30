### INSTANCE#ADD

```javascript
/**
 * socket got added to an instance
 * @property {object} event
 * @property {number} event.id the instance which has been changed
 * @property {object} event.state current state of the instance
 */
socket.on("INSTANCE#ADD", event => {
  console.log("got added to instance", event.id, event.state.serverinfo.name)
})
```


### INSTANCE#UPDATE

```javascript
/**
 * instance property has been changed inside the state
 * @property {object} event
 * @property {number} event.id the instance which has been changed
 * @property {[string, string|number|boolean|undefined|(number|string|boolean)[]][]>} event.changes
 */
socket.on("INSTANCE#UPDATE", event => {
  console.log(`received updates for instance with id ${event.id}`, event.changes)
})
```


### INSTANCE#REMOVE

```javascript
/**
 * removes instance, either permissions have been revoked or instance has been deleted
 * @property {object} event
 * @property {number} event.id the instance which should get removed
 */
socket.on("INSTANCE#REMOVE", event => {
  console.log(`removed from instance ${event.id}`)
})
```

### INSTANCE#CHAT

```javascript
/**
 * gets emitted when a chat event gets received from the server
 * @property {object} event see https://alliance-apps.github.io/VeniceRCON-documentation/api/#/Events/get_api_instances__instanceId__events_chat
 */
socket.on("INSTANCE#CHAT", event => {
  //do stuff here
})
```

### INSTANCE#KILL

```javascript
/**
 * gets emitted when a kill event gets received from the server
 * @property {object} event see https://alliance-apps.github.io/VeniceRCON-documentation/api/#/Events/get_api_instances__instanceId__events_kill
 */
socket.on("INSTANCE#KILL", event => {
  //do stuff here
})
```

### INSTANCE#LOG

```javascript
/**
 * gets emitted when one or more log messages gets received
 * @property {object[]} event
 */
socket.on("INSTANCE#LOG", event => {
  //do stuff here
})
```


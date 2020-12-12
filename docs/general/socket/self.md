### SELF#PERMISSION_UPDATE

```javascript
/**
 * gets fired when own permissions have been updated
 */
socket.on("SELF#PERMISSION_UPDATE", () => {
  //get new permissions via /api/auth/whoami
})
```

### SELF#CMD_FEATURE

```javascript
/**
 * this enables a specific feature for this socket connection
 */


/** this payload enables to get raw console commands to be received */
const payload = {
  //the instanceid for which console commands should be enabled
  id: 123,
  //this is a constant
  name: "raw",
  //if set to false it will disable the feature after having it set to true
  set: true
}


socket.emit("SELF#CMD_FEATURE", payload)
```
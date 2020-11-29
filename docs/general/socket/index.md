### Socket

In order to connect with the Websocket we use Socket.io.
To be able to connect to it and retrieve a list of instances you will need to send yout jwt token!

Doing this with the `Manager` would look like following:

```typescript

//insert your jwt token here
const JWT_TOKEN = ""
//insert your backend address here
const url = ""

//this creates a socket.io manager
export const manager = new Manager(url, {
  //tell the socket not to connect automatically
  //you can connect later with socket.connect()
  autoConnect: false,
  //this tells socket.io to only use websocket as transport
  //if you want to have the option for long polling you can delete this line
  transports: ["websocket"]
})

//tell the socket to connect to the main namespace
//only the default namespace under `"/"` will be used
export const socket: Socket = manager.socket("/", {
  //this sets the JWT_TOKEN with which socket.io will authenticate with
  auth: { auth_token: JWT_TOKEN }
})

```
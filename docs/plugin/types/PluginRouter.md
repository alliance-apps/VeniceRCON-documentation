## Plugin Router

The Plugin Router enables to receive data and respond http requests from the VeniceRCON API messages will be received from `/api/plugins/{instanceId}/{pluginName}/{route}`.

`instanaceId` is the id of the instance the plugin runs on\
`pluginName` is the name of the plugin which will be identified by its folder name\
`route` is the route defined in the router

!!! note
    For route parameter only `^[\w\d]+$` is allowed!

```typescript

declare type Context = {
  /** possible payload which has been sent **/
  body: any
  /** respond with data back to the frontend */
  send: (data: any) => void
}

declare type RouterCallback = (ctx: Context) => void

export interface PluginRouter {
  /** GET requests */
  get(name: string, callback: PluginRouter.RouterCallback): PluginRouter
  /** POST requests */
  post(name: string, callback: PluginRouter.RouterCallback): PluginRouter
  /** PATCH requests */
  patch(name: string, callback: PluginRouter.RouterCallback): PluginRouter
  /** DELETE requests */
  delete(name: string, callback: PluginRouter.RouterCallback): PluginRouter
}
```
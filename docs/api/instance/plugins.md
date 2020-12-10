{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/plugins",
  scopes = ["PLUGIN#ACCESS"],
  description = "retrieves a list of plugins which are startable on this instance",
  loggedIn = True,
  response = parse_schema(schemas.Plugins)
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/plugins/{id}/start",
  scopes = ["PLUGIN#MODIFY"],
  description = "enables the plugin",
  loggedIn = True
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/plugins/{id}/stop",
  scopes = ["PLUGIN#MODIFY"],
  description = "disables the plugin",
  loggedIn = True
) }}

{{ route(
  method = "PATCH",
  path = "/api/instances/{instanceId}/plugins/{id}/config",
  scopes = ["PLUGIN#MODIFY"],
  description = "modifies the configuration of the plugin",
  loggedIn = True,
  response = {},
  body = {
    "vars.key": "any"
  }
) }}

{{ route(
  method = "DELETE",
  path = "/api/instances/{instanceId}/plugins/{id}",
  scopes = ["PLUGIN#REMOVE"],
  description = "removes a plugin from the instance",
  loggedIn = True,
  response = {}
) }}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/plugins/store",
  scopes = ["PLUGIN#ACCESS"],
  description = "retrieves a list of plugins which can be downloaded from the store",
  loggedIn = True,
  response = parse_schema(schemas.StoreItems)
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/plugins/store/{uuid}",
  scopes = ["PLUGIN#CREATE"],
  description = "downloads a plugin to the instance plugin folder, this route can also be used to update a plugin",
  loggedIn = True,
  response = {}
) }}
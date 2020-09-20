{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/plugins",
  scopes = ["PLUGIN#ACCESS"],
  description = "retrieves a list of plugins which have been setup on this server",
  loggedIn = True,
  response = parse_schema(schemas.Plugins)
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/plugins",
  scopes = ["PLUGIN#MODIFY"],
  description = "adds a new plugin to the server",
  loggedIn = True,
  response = parse_schema(schemas.AddPlugin),
  body = { "id": 0 }
) }}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/plugins/available",
  scopes = ["PLUGIN#ACCESS"],
  description = "retrieves a list of plugins which can be installed",
  loggedIn = True,
  response = parse_schema(schemas.Plugins),
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/plugins/{id}/start",
  scopes = ["PLUGIN#MODIFY"],
  description = "enables the plugin",
  loggedIn = True,
  response = parse_schema(schemas.AddPlugin)
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/plugins/{id}/stop",
  scopes = ["PLUGIN#MODIFY"],
  description = "disables the plugin",
  loggedIn = True,
  response = parse_schema(schemas.AddPlugin)
) }}

{{ route(
  method = "PATCH",
  path = "/api/instances/{instanceId}/plugins/{id}/config",
  scopes = ["PLUGIN#MODIFY"],
  description = "modifies the configuration of the plugin",
  loggedIn = True,
  response = {}
) }}
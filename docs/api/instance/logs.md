{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/logs/instance",
  scopes = ["INSTANCE#LOG"],
  description = "retrieves a list of log messages for the specified instance",
  loggedIn = True,
  response = parse_schema(schemas.LogMessages)
) }}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/logs/plugins/",
  scopes = ["INSTANCE#LOG"],
  description = "retrieves a list of plugin log messages",
  loggedIn = True,
  response = parse_schema(schemas.LogMessages)
) }}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/logs/plugins/{pluginName}",
  scopes = ["INSTANCE#LOG"],
  description = "retrieves a list of plugin log messages for a specific plugin",
  loggedIn = True,
  response = parse_schema(schemas.LogMessages)
) }}
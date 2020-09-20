{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/mods",
  scopes = ["MOD#ACCESS"],
  description = "retrieves a list of available mods",
  loggedIn = True,
  response = parse_schema(schemas.Mods)
) }}

{{ route(
  method = "PATCH",
  path = "/api/instances/{instanceId}/mods/reload",
  scopes = ["MOD#UPDATE"],
  description = "reloads all extensions",
  loggedIn = True
) }}

{{ route(
  method = "PATCH",
  path = "/api/instances/{instanceId}/mods/clear",
  scopes = ["MOD#DELETE"],
  description = "clears the modlist",
  loggedIn = True,
  response = parse_schema(schemas.Mods)
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/mods/{mod}",
  scopes = ["MOD#CREATE"],
  description = "enables a mod",
  loggedIn = True
) }}

{{ route(
  method = "DELETE",
  path = "/api/instances/{instanceId}/mods/{mod}",
  scopes = ["MOD#DELETE"],
  description = "disables a mod",
  loggedIn = True
) }}
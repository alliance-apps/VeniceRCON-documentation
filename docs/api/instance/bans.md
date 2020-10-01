{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/bans",
  scopes = ["BAN#ACCESS"],
  description = "retrieves the banlist for this instance",
  loggedIn = True,
  responseText = "ban for this instance",
  response = parse_schema(schemas.Bans)
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/bans",
  scopes = ["BAN#CREATE"],
  description = "creates a new ban",
  loggedIn = True,
  body = parse_schema(schemas.CreateBan)
) }}

{{ route(
  method = "DELETE",
  path = "/api/instances/{instanceId}/bans/{subset}/{id}",
  scopes = ["BAN#DELETE"],
  description = "delete a ban from this instance",
  loggedIn = True
) }}
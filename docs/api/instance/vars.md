{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/vars",
  scopes = ["INSTANCE#ACCESS"],
  description = "retrieves a list of vip slots",
  loggedIn = True,
  response = parse_schema(schemas.Variables)
) }}

{{ route(
  method = "PATCH",
  path = "/api/instances/{instanceId}/vars",
  scopes = ["VARIABLE#MODIFY"],
  description = "updates variables in this instance",
  loggedIn = True,
  see = "/general/variables/",
  body = {
    "[variablename]": "string|number|boolean"
  },
  response = parse_schema(schemas.Variables)
) }}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/vars/options",
  scopes = ["INSTANCE#ACCESS"],
  description = "retrieves all var getters and setters for this instance",
  loggedIn = True,
  response = parse_schema(schemas.Options)
) }}
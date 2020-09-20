{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/instances",
  scopes = ["INSTANCE#ACCESS"],
  description = "retrieve a list of instances you have access to",
  loggedIn = True,
  responseText = "responds with an array of available instances",
  response = parse_schema(schemas.Instances)
) }}

{{ route(
  method = "POST",
  path = "/api/instances",
  scopes = ["INSTANCE#CREATE"],
  description = "creates a new rcon instance and tries to connect to it",
  loggedIn = True,
  responseText = "created instance",
  response = parse_schema(schemas.Instance),
  body = {
    "host": "string",
    "port": 0,
    "password": "string"
  }
) }}
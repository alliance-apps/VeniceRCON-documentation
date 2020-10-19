{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/instance/{instanceId}",
  scopes = ["INSTANCE#ACCESS"],
  description = "retrieves informations about a single instance",
  loggedIn = True,
  responseText = "single instance information",
  response = parse_schema(schemas.Instance)
) }}

{{ route(
  method = "DELETE",
  path = "/api/instance/{instanceId}",
  scopes = ["INSTANCE#DELETE"],
  description = "removes an instance",
  loggedIn = True
) }}

{{ route(
  method = "PATCH",
  path = "/api/instance/{instanceId}/start",
  scopes = ["INSTANCE#UPDATE"],
  description = "connect the instance to the battlefield server",
  loggedIn = True
) }}

{{ route(
  method = "PATCH",
  path = "/api/instance/{instanceId}/stop",
  scopes = ["INSTANCE#UPDATE"],
  description = "disconnect the instance from the battlefield server",
  loggedIn = True
) }}

{{ route(
  method = "POST",
  path = "/api/instance/{instanceId}/message",
  scopes = ["PLAYER#MESSAGE"],
  description = "sends a message to the server",
  loggedIn = True,
  body = {
    "message": "string",
    "subset": "player",
    "subsetId": "string",
    "yell": true,
    "yellDuration": 0
  }
) }}

{{ route(
  method = "POST",
  path = "/api/instance/{instanceId}/raw",
  scopes = ["INSTANCE#CONSOLE"],
  description = "sends a raw command to the instance",
  loggedIn = True,
  body = {
    "words": ["string"]
  }
) }}
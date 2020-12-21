{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/users",
  description = "gets informations about all available users",
  loggedIn = True,
  scopes = ["USER#ACCESS"],
  responseText = "responds with all users in the database",
  response = parse_schema(schemas.Users)
) }}

{{ route(
  method = "POST",
  path = "/api/users",
  description = "gets informations about all available users",
  loggedIn = True,
  scopes = ["USER#ACCESS"],
  responseText = "responds with all users in the database",
  response = parse_schema(schemas.User),
  body = {
    "username": "string",
    "password": "string"
  }
) }}
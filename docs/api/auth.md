{% from "templates/route.md.jinja" import route %}
{% from "api/schemas/Whoami.yaml" import Whoami %}

{{ route(
  method = "POST",
  path = "/api/auth/login",
  description = "tries to log you into the specified account",
  loggedIn = False,
  responseText = "responds with the jwt token",
  response = {
    "token": "string"
  },
  body = {
    "username": "string",
    "password": "string"
  }
) }}

{{ route(
  method = "GET",
  path = "/api/auth/whoami",
  description = "retrieves informations about the currently used token",
  loggedIn = True,
  responseText = "responds with informations about your token",
  response = parse_schema(Whoami)
) }}

{{ route(
  method = "POST",
  path = "/api/auth/invite",
  description = "use and consume a login token in order to gain access to an additional instance",
  loggedIn = True,
  response = {
    "token": "string"
  },
  body = {
    "username": "string",
    "password": "string",
    "token": "string"
  }
) }}

{{ route(
  method = "POST",
  path = "/api/auth/register",
  description = "creates an user with an invite token",
  loggedIn = False,
  response = {
    "token": "string"
  },
  body = {
    "username": "string",
    "password": "string",
    "token": "string"
  }
) }}
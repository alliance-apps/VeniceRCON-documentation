{% from "templates/route.md.jinja" import route %}

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
  response = parse_schema(schemas.Whoami)
) }}

{{ route(
  method = "POST",
  path = "/api/auth/invite",
  description = "use and consume a login token in order to gain access to an additional instance",
  loggedIn = True,
  body = {
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

{{ route(
  method = "POST",
  path = "/api/auth/forgot-password",
  description = "sends a new password to the provided mail address if smtp has been setup",
  loggedIn = False,
  body = {
    "email": "string"
  }
) }}

{{ route(
  method = "POST",
  path = "/api/auth/update-self",
  description = "updates the current users password and email (if newEmail is null then it will get deleted",
  loggedIn = True,
  body = {
    "currentPassword": "string",
    "password?": "string",
    "email?": "string|null",
  }
) }}

{{ route(
  method = "POST",
  path = "/api/auth/search-player",
  description = "searches for a specific player, either by guid or name, or combined",
  loggedIn = True,
  body = {
    "guid?": "string",
    "name?": "string"
  },
  responseText = "collected player from this instance",
  response = parse_schema(schemas.DatabasePlayers)
) }}


{{ route(
  method = "GET",
  path = "/api/auth/binding",
  description = "lists bound players for your current token",
  loggedIn = True,
  responseText = "retrieves all player bindings for this user",
  response = parse_schema(schemas.DatabasePlayers)
) }}

{{ route(
  method = "POST",
  path = "/api/auth/binding",
  description = "creates a binding between your token and player",
  loggedIn = True,
  body = {
    "playerId": 0
  }
) }}

{{ route(
  method = "DELETE",
  path = "/api/auth/binding/:id",
  description = "removes a binding between your token and player",
  loggedIn = True
) }}
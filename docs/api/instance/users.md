{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/users",
  scopes = ["INSTANCEUSER#ACCESS"],
  description = "retrieves a list of users with their permissions",
  loggedIn = True,
  responseText = "list of users on this instance",
  response = parse_schema(schemas.InstanceUsers)
) }}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/users/invite",
  scopes = ["INSTANCEUSER#ACCESS"],
  description = "retrieves a list of invite links for this instance",
  loggedIn = True,
  responseText = "list of users on this instance",
  response = parse_schema(schemas.Invites)
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/users/invite",
  scopes = ["INSTANCEUSER#CREATE"],
  description = "creates a new invite token for this instance",
  loggedIn = True,
  responseText = "retrieves the invite token for this instance",
  response = parse_schema(schemas.InviteToken)
) }}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/users/{userId}",
  scopes = ["INSTANCEUSER#ACCESS"],
  description = "retrieves a single user with their permissions",
  loggedIn = True,
  responseText = "user informations",
  response = parse_schema(schemas.InstanceUser)
) }}

{{ route(
  method = "DELETE",
  path = "/api/instances/{instanceId}/users/{userId}",
  scopes = ["INSTANCEUSER#REMOVE"],
  description = "revokes access for a user to the instance",
  loggedIn = True
) }}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/users/{userId}/bind",
  scopes = ["INSTANCEUSER#UPDATE"],
  description = "lists bound players for this user",
  loggedIn = True,
  responseText = "retrieves all player bindings for this user",
  response = parse_schema(schemas.DatabasePlayers)
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/users/{userId}/bind",
  scopes = ["INSTANCEUSER#UPDATE"],
  description = "creates a binding between player and user",
  loggedIn = True,
  body = {
    "playerId": 0
  }
) }}

{{ route(
  method = "DELETE",
  path = "/api/instances/{instanceId}/users/{userId}/bind",
  scopes = ["INSTANCEUSER#UPDATE"],
  description = "removes a binding between player and user",
  loggedIn = True,
  body = {
    "playerId": 0
  }
) }}

{{ route(
  method = "PATCH",
  path = "/api/instances/{instanceId}/users/{userId}/permissions",
  scopes = ["INSTANCEUSER#UPDATE"],
  description = "updates permissions from a user for this instance",
  loggedIn = True,
  body = {
    "add?": ["SCOPES"],
    "remove?": ["SCOPES"]
  }
) }}
{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/players",
  scopes = ["INSTANCE#ACCESS"],
  description = "retrieves a list of currently ingame players",
  loggedIn = True,
  responseText = "list of users on this instance",
  response = parse_schema(schemas.Players)
) }}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/players/{guid}",
  scopes = ["INSTANCEUSER#ACCESS"],
  description = "retrieves informations about a single player online",
  loggedIn = True,
  responseText = "list of users on this instance",
  response = parse_schema(schemas.Player)
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/players/{guid}/move",
  scopes = ["PLAYER#MOVE"],
  description = "moves a player to another squad/team",
  loggedIn = True,
  body = {
    "teamId": 0,
    "squadId": 0,
    "kill": True
  }
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/players/{guid}/message",
  scopes = ["PLAYER#MESSAGE"],
  description = "sends a message to the player/team/squad",
  loggedIn = True,
  body = {
    "teamId": 0,
    "squadId": 0,
    "kill": True
  }
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/players/{guid}/kill",
  scopes = ["PLAYER#KILL"],
  description = "kills the player with optional reason message",
  loggedIn = True,
  body = {
    "reason": "string"
  }
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/players/{guid}/kick",
  scopes = ["PLAYER#KICK"],
  description = "kicks the player with optional reason message",
  loggedIn = True,
  body = {
    "reason": "string"
  }
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/players/{guid}/ban",
  scopes = ["PLAYER#BAN"],
  description = "bans the player",
  loggedIn = True,
  body = parse_schema(schemas.CreateBan)
) }}
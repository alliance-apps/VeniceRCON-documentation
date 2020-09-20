{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/maps",
  scopes = ["INSTANCE#ACCESS"],
  description = "retrieves the current map rotation",
  loggedIn = True,
  response = parse_schema(schemas.Maps)
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/maps",
  scopes = ["MAPS#MANAGE"],
  description = "adds a map to the rotation",
  loggedIn = True,
  response = parse_schema(schemas.AddMap)
) }}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/maps/current",
  scopes = ["INSTANCE#ACCESS"],
  description = "retrieves the current and next map index",
  loggedIn = True,
  response = parse_schema(schemas.MapIndex)
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/maps/endRound",
  scopes = ["MAPS#SWITCH"],
  description = "ends the current round with a set winning team",
  loggedIn = True,
  body = {
    "winner": 0
  }
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/maps/nextRound",
  scopes = ["MAPS#SWITCH"],
  description = "starts the next round",
  loggedIn = True
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/maps/restartRound",
  scopes = ["MAPS#SWITCH"],
  description = "restarts the current round",
  loggedIn = True
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/maps/{index}",
  scopes = ["INSTANCE#ACCESS"],
  description = "retrieves the map data from the current index",
  loggedIn = True,
  response = parse_schema(schemas.Map)
) }}

{{ route(
  method = "DELETE",
  path = "/api/instances/{instanceId}/maps/{index}",
  scopes = ["MAPS#MANAGE"],
  description = "removes the map from the current rotation",
  loggedIn = True
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/maps/{index}/next",
  scopes = ["MAPS#SWITCH"],
  description = "sets the index of the next map to be played",
  loggedIn = True
) }}
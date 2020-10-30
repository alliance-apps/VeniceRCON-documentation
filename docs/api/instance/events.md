{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/events/kill",
  scopes = ["EVENT#KILL"],
  description = "retrieves a certain amount of kills from a specific date",
  loggedIn = True,
  query = {
    count: 0,
    from: "date"
  },
  response = parse_schema(schemas.Kills)
) }}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/events/chat",
  scopes = ["EVENT#CHAT"],
  description = "retrieves a certain amount of chat messages from a specific date",
  loggedIn = True,
  query = {
    count: 0,
    from: "date"
  },
  response = parse_schema(schemas.Messages)
) }}
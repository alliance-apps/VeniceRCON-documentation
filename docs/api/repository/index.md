{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/repository",
  description = "gets a list of created repositories",
  loggedIn = True,
  scopes = ["REPOSITORY#ACCESS"],
  responseText = "responds with all available repositores",
  response = parse_schema(schemas.Repositories)
) }}

{{ route(
  method = "POST",
  path = "/api/repository",
  description = "adds a new repository",
  loggedIn = True,
  scopes = ["REPOSITORY#CREATE"],
  response = parse_schema(schemas.Repository)
) }}
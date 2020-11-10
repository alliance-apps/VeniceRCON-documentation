{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/repository/{id}",
  description = "gets a repository with the specified id",
  loggedIn = True,
  scopes = ["REPOSITORY#ACCESS"],
  response = parse_schema(schemas.Repository)
) }}

{{ route(
  method = "DELETE",
  path = "/api/repository/{id}",
  description = "deletes the specified repository",
  loggedIn = True,
  scopes = ["REPOSITORY#REMOVE"],
) }}

{{ route(
  method = "PATCH",
  path = "/api/repository",
  description = "adds a new repository",
  loggedIn = True,
  scopes = ["REPOSITORY#CREATE"],
  response = parse_schema(schemas.Repository),
  body = {
    "url?": "string",
    "branch?": "string",
    "headers?": "string",
    "enabled?": True
  }
) }}
{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/users/:id",
  description = "gets informations about a single user",
  loggedIn = True,
  scopes = ["USER#ACCESS"],
  responseText = "responds with all users in the database",
  response = parse_schema(schemas.User)
) }}

{{ route(
  method = "PATCH",
  path = "/api/users/:id",
  description = "modifies certain properties of a user",
  loggedIn = True,
  scopes = ["USER#MODIFY"],
  body = {
    "password?": "string",
    "email?": "string|null"
  }
) }}

{{ route(
  method = "DELETE",
  path = "/api/users/:id",
  description = "removes a user",
  loggedIn = True,
  scopes = ["USER#DELETE"]
) }}

{{ route(
  method = "POST",
  path = "/api/users/:id/permissions",
  description = "adds a new permission to this user",
  loggedIn = True,
  scopes = ["USER#MODIFY"],
  body = {
    "root?": "boolean",
    "instanceId?": 0,
    "scopes": ["PERMISSION#SCOPES"]
  }
) }}

{{ route(
  method = "DELETE",
  path = "/api/users/:id/permissions/:permissionId",
  description = "removes a permissionid from the user",
  loggedIn = True,
  scopes = ["USER#MODIFY"]
) }}

{{ route(
  method = "PATCH",
  path = "/api/users/:id/permissions/:permissionId",
  description = "removes a permissionid from the user",
  loggedIn = True,
  scopes = ["USER#MODIFY"],
  body = {
    "scopes": ["PERMISSION#SCOPES"]
  }
) }}
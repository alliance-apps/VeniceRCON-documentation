{% from "templates/route.md.jinja" import route %}

{{ route(
  method = "GET",
  path = "/api/instances/{instanceId}/reservedslot",
  scopes = ["RESERVEDSLOT#ACCESS"],
  description = "retrieves a list of vip slots",
  loggedIn = True,
  response = ["string"]
) }}

{{ route(
  method = "POST",
  path = "/api/instances/{instanceId}/reservedslot",
  scopes = ["RESERVEDSLOT#CREATE"],
  description = "adds a map to the rotation",
  loggedIn = True,
  body = {
    "name": "string"
  }
) }}

{{ route(
  method = "DELETE",
  path = "/api/instances/{instanceId}/reservedslot/{slot}",
  scopes = ["RESERVEDSLOT#DELETE"],
  description = "deletes a vip slot",
  loggedIn = True
) }}
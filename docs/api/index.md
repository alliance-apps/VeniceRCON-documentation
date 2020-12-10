This API uses JWT Tokens for authentication!

In order to send the Authentication Header please consider using following format:

```http
### gets information about the token
GET http://127.0.0.1:8000/api/auth/whoami
Authorization: Bearer JWT_TOKEN_HERE
```

All responses bodies are either empty or use JSON as response text, response body varies depending on route

#### JWT Refresh Token

The API will occasionally send as response header a new JWT Token before the old one runs out!
This will be sent via the `Authorization: Bearer ...JWT TOKEN...`, when you receive this header you should take this token and use the new one provided by the api!
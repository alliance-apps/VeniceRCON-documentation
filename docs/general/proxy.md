## NGINX

for NGINX the recommended configuration would look like

```nginx

server {
  listen 443;
  server_name vurcon.example.com;

  ssl on;
  ssl_certificate /path/to/your/certfile/fullchain.pen;
  ssl_certificate_key /path/to/your/certfile/privkey.pem;  

  location / {
                      #set the correct ip + port to your application
    proxy_pass        http://127.0.0.1:8000;
    proxy_set_header  Host              $host;
    proxy_set_header  X-Forwarded-For   $remote_addr;
                      #set to http if no ssl is used
                      #altough SSL is strongly recommended
    proxy_set_header  X-Forwarded-Proto https
    proxy_set_header  Upgrade           $http_upgrade;
    proxy_set_header  Connection        upgrade;
  }

}

```
The base configuration for your current release can always be seen inside `config.default.yaml`.
You should copy this file to `config.yaml` after installation

#### config.yaml

````yaml
database:
  #this is a string and can either be "sqlite", "mariadb", "postgres"
  use: "sqlite"
  #see https://github.com/typeorm/typeorm/blob/master/docs/connection-options.md for details
  #depending on what database you are using you can choose between those 3 presets
  #for performance reasons sqlite is only recommended if you intend to run maximum of 5 instances
  sqlite:
    database: "./rcon.db"
  mariadb:
    host: "127.0.0.1"
    port: 3306
    username: ""
    password: ""
    database: "battlefield"
  postgres:
    host: "127.0.0.1"
    port: 5432
    username: ""
    password: ""
    database: ""
logging:
  #enable logging of query messages normally not needed for end users
  orm: false
  #loglevel to use available options are "verbose"|"info"|"warn"|"error"
  #"verbose": debug mode, logs everything
  #"info": all informational messages and above
  #"warn": warning messages and above (which are not that bad)
  #"error": only critical errors will be logged
  level: info
webserver:
  #port which the webserver listens to dont set any lower than 1024!
  listenport: 8000
  #set this to true when application runs behind a proxy
  #this will tell the webserver to use the "X-Forwarded-For", "X-Forwarded-Proto", ... headers
  proxy: false
  #enable pretty json output for development purposes
  prettyJson: false
  jwt:
    #maxmimum token age in days
    maxAge: 7
    #time in days after a new token gets issued
    sendRefresh: 5
  #set cors when requests comes from one of those domains
  #can be helpful if you run the backend on a different domain than the frontend
  cors:
    - "https://alliance-apps.github.io"
instance:
  #default time in ms of how many updates get sent to the rcon server
  #lower number means more messages will be sent to the battlefield/vu server and socket updates will be faster
  syncInterval: 5000
  plugins:
    #location of the directory to read plugins from
    baseDir: "./plugins"
#smtp settings in order to send forgot-password requests
smtp:
  #enable this feature?
  enable: false
  #email address to send mails from
  senderAddress: "foo@example.com"
  #connection options, for more informations see https://nodemailer.com/smtp/
  options:
    host: "smpt.example.com"
    port: 587
    auth:
      user: ""
      pass: ""
  content:
    #you can use wildcards  %username% and %password% for subject and text
    subject: "Forgot Password request"
    text: "Hello %username%, your new password is %password%"

````
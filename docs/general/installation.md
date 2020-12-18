### Prerequisites

* minimum NodeJS v14 installed
* npm installed

### Database Support

Currently supported is:

  * MariaDB
  * PostgreSQL
  * Sqlite (default)

### Installation

In order to install VeniceRCON you will need to have NodeJS (version >= 12) and npm preinstalled on your server.

It is recommended to use this tool with a process manager like (PM2)[https://pm2.keymetrics.io/]

```bash
# download your release
curl -OL https://github.com/alliance-apps/VeniceRCON/releases/latest/download/venicercon.tar.gz

# unpack the files
tar -xvf venicercon.tar.gz

# switch into the downloaded folder
cd venicercon

# install dependencies via npm
npm ci --only=prod

# copy the default config.default.yaml to config.yaml
# by default this config can be used as is
# and does not require further editing
cp config.default.yaml config.yaml

#start the tool
npm start
```


### Development

If you want to make changes or use the current repository from github you can simply clone the repository from github:

`git clone https://github.com/alliance-apps/VeniceRCON-backend`

Then install the required dependencies from the `package-lock.json` with following command (this should also be done after every `git pull`):

`npm ci`

Finally in order to be able to run it use:

`npm run start-dev`

This command will first build the JS files from the TypeScript files and after will start the VeniceRCON!
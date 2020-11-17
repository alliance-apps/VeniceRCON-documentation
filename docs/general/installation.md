### Prerequisites

* minimum NodeJS v14 installed
* npm installed

### Database Support

Currently supported is:

  * MariaDB
  * PostgreSQL
  * Sqlite

### Installation

In order to install VeniceRCON you will need to have NodeJS and npm preinstalled on your server

```bash
#clone the repository
git clone {{backend_repo_url}}

#switch into the cloned repo
cd VeniceRCON-backend

#install dependencies
npm install

#copy the default config.default.yaml to config.yaml
cp config.default.yaml config.yaml

#edit the configuration to your needs
nano config.yaml

#build the compiled typescript files
npm run build

#start the tool with
npm start
```
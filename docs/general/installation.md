### Prerequisites

* minimum NodeJS v14 installed
* npm installed

### Database Support

Currently supported is:

  * MariaDB
  * PostgreSQL
  * Sqlite

### Installation

In order to install VeniceRCON you will need to have NodeJS and npm preinstalled on your server.
If you use sqlite as database then the node version matters otherwise it does not. You can find out your installed node version with `node -v`

{% for version in supported_node_versions %}
=== "Node v{{version}}"

    ```bash
    # download your release
    curl -OL https://github.com/alliance-apps/VeniceRCON-backend/releases/download/{{current_release_version}}/venicercon-node-{{version}}-{{current_release_version}}.tar.gz

    # unpack the files
    tar -xvf venicercon-node-{{version}}-{{current_release_version}}.tar.gz
    
    # rename the folder
    mv venicercon-{{current_release_version}} venicercon

    # switch into the downloaded folder
    cd venicercon

    # copy the default config.default.yaml to config.yaml
    cp config.default.yaml config.yaml

    # edit the configuration to your needs
    nano config.yaml

    #start the tool
    npm start
    ```

{% endfor %}


### Development

If you want to make changes or use the current repository from github you can simply clone the repository from github:

`git clone https://github.com/alliance-apps/VeniceRCON-backend`

Then install the required dependencies from the `package-lock.json` with following command (this should also be done after every `git pull`):

`npm ci`


Finally in order to be able to run it use:

`npm run start-dev`

This command will first build the JS files from the TypeScript files and after will start the VeniceRCON!
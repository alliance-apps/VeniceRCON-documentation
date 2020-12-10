# Plugin Concept

Each Battlefield Instance gets its own worker assigned where it can run their Plugin inside, this allows to run possible blocking Plugins not affecting other instances because the NodeJS main event loop gets blocked.

# Plugin Installation

There is a dedicated Folder for Plugins, in order to create a new Plugin simply create an additional sub folder and create 2 files with following structure

```
| root
|-- plugins
|---- dev //here you can put all plugins you want to install manually
|---- :instanceid: //the instance id of your server where you want to test plugins
|------ :uuid: //a generated uuid for your plugin
|-------- meta.yaml
|-------- index.js
```

!!! info "meta.yaml"
    meta.yaml will hold the basic configurations of your plugin

    More details about the file layoout can be found [here](./meta.md)

!!! info "index.js"
    this is the entry point for your plugin and should export a single function

    More details about the file layoout can be found [here](./script.md)

# Developing Plugins

In order to develop Plugins you can create a folder inside your `plugins` folder and call it `dev` inside this folder you can create a new folder in which your plugin resides

You then can download the plugin normally via your Instances Plugin page!
(You might need to do a reload after creating your new plugin)

In order to update the plugin to your instance you just "redownload" it



# Publishing

If you want other people to be able to use your rcon plugin you can let them install it via a repository, for this you will need to put your plugin into a github repository and provide the commit string and github repository url to a repository provider like [this one](https://github.com/Multivit4min/vu-plugin-repo)

## Limitations

If you use dependencies from yarn or npm then you will need to have those in your repository predownloaded aswell since vurcon does not automatically `npm install` these!
# Plugin Concept

Each Battlefield Instance gets its own worker assigned where it can run their Plugin inside, this allows to run possible blocking Plugins not affecting other instances because the NodeJS main event loop gets blocked.

# Plugin Installation

There is a dedicated Folder for Plugins, in order to create a new Plugin simply create an additional sub folder and create 2 files with following structure

```
| root
|-- plugins
|---- 2 //the instance id of your server where you want to test plugins
|------ your_plugin_name
|-------- meta.yaml
|-------- index.js
```

!!! info "meta.yaml"
    meta.yaml will hold the basic configurations of your plugin

!!! info "index.js"
    this is the entry point for your plugin and should export a single function

# Publishing

If you want other people to be able to use your rcon plugin you can let them install it via a repository, for this you will need to put your plugin into a github repository and provide the commit string and github repository url to a repository provider like [this one](https://github.com/Multivit4min/vu-plugin-repo)

## Limitations

If you use dependencies from yarn or npm then you will need to have those in your repository aswell, as those wont be automatically downloaded, in order to require those modules you will need to use reltive paths to those modules 
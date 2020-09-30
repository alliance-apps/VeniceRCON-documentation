# Plugin Concept

Each Battlefield Instance gets its own worker assigned where it can run their Plugin inside, this allows to run possible blocking Plugins not affecting other instances because the NodeJS main event loop gets blocked.

# Plugin Installation

There is a dedicated Folder for Plugins, in order to create a new Plugin simply create an additional sub folder and create 2 files with following structure

```
| root
|- plugins
|-- your_plugin
|--- meta.yaml
|--- index.js

```

!!! info "meta.yaml"
    meta.yaml will hold the basic configurations of your plugin

!!! info "index.js"
    this is the entry point for your plugin and should export a single function
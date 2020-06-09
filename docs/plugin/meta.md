## Plugin meta.yaml

The plugins `meta.yaml` describes multiple properties of a plugin, currently it should looke like this:

```yaml
#name of the plugin
name: "Test Plugin"
#description of the plugin
description: "plugin to test the rcon plugin interface"
#the version string for the plugin
version: "1.0.0"
#plugin language type currently only "JS" is supported
backend: "JS"
#plugin entry point
entry: "index.js"
vars:
    #arbitary key to identify the config entry in the config object
  - name: "foo"
    #meaningful description which can describe a key on the webinterface
    description: "set a value for foo"
    #type of the value which gets used, available types are:
    #string, boolean, number
    type: "string"
    #default value which will be set if there is a null value
    default: "baz"
  - name: "bar"
    description: "set a value for bar"
    type: "number"
    default: 0
```
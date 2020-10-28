About this Repository
=====================

Plugin Repositories provide a place to collect and share VeniceRCON Plugins, it is a central place to download VeniceRCON plugins. If you want to create your own repository you can clone [this](https://github.com/Multivit4min/vu-plugin-repo) repository and add it in your VeniceRCON's `config.yaml`!

## repository.yaml

This is the main file from where VeniceRCON will get plugin informations from.
At the moment there is a single key named `plugins` which is an array with following fields:

field       | type   | description
------------|--------|-------------------------------------------------------------
name        | string | arbitary plugin name under which the plugin gets identified
description | string | a brief description of what the plugin does
version     | string | a semantic version string of the plugin version
repository  | string | a github url to the repository of the plugins source code
commit      | string | the commit which should be downloaded

An example would look like:
```yaml
plugins:
  - name: "showcase"
    description: "simple showcase plugin"
    version: "1.0.0"
    repository: "https://github.com/Multivit4min/VeniceRCON-showcase-plugin"
    commit: "57edeb66196e0c4fdf9c1e475965a9c8404219cc"
  - name: "other_arbitary_plugin"
    description: "arbitary non existing plugin"
    version: "2.5.1"
    repository: "https://github.com/doesnotexist/thisneither"
    commit: "123456789abcdefghijklmnopqrstuvwxyz123456"
```

Inside your VENICERCON config you add this repository to the path: `instance.plugins.repos`

This should look like following: 
```yaml
instance:
  plugins:
    repos:
      - name: "main"
        repository: "https://github.com/Multivit4min/vu-plugin-repo/"
```

**name** this is the arbitary name to identify your plugin provider repository so it is possible to identify where to get updates for a specific plugin from

**repository** this is the general to the repository which should contain the repository.yaml
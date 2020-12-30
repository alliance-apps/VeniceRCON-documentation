About this Repository
=====================

Plugin Repositories provide a place to collect and share VeniceRCON Plugins, it is a central place to download VeniceRCON plugins. If you want to create your own repository you can clone [this](https://github.com/Multivit4min/vu-plugin-repo) repository and add it in your VeniceRCON's `config.yaml`!

## repository.yaml

This is the main file from where VeniceRCON will get plugin informations from.
At the moment there is a single key named `plugins` which is an array with following fields:

field       | type   | description
------------|--------|-------------------------------------------------------------
username    | string | github username
repository  | string | repository of the user
commit      | string | the commit which should be downloaded

An example would look like:
```yaml
plugins:
  - username: "Multivit4min"
    repository: "VeniceRCON-showcase-plugin"
    commit: "476b6fdadfaf35431fcdeec0bc4cba73e0135328"
  - username: "Multivit4min"
    repository: "VeniceRCON-metrics-plugin"
    commit: "476b6fdadfaf35431fcdeec0bc4cba73e0135328"
```

You can add this repository via webinterface to your instance
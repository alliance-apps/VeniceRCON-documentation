## Plugin meta.yaml

The plugins `meta.yaml` describes multiple properties of a plugin, currently it should looke like this:

```yaml
#name of the plugin
name: "Test Plugin"
#description of the plugin
description: "plugin to test the rcon plugin interface"
#author name
author: "Multivitamin <david.kartnaller@gmail.com>"
#the version string for the plugin
version: "1.0.0"
#plugin backend (options: "BF3", "VU"), when "BF3" is chosen then it will run on Venice Unleashed Servers and Vanilla BF3 Servers
backend: "BF3"
#plugin entry point
entry: "index.js"
#dependencies which are mandatory for this plugin
dependencies: []
#require other dependencies
optionalDependencies:
  - Other Plugin
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

## General Variable Schema

field        | optional | type             | description
-------------|----------|------------------|------
name         | NO       | string           | the field key identifier
description  | NO       | string           | the field descriptor
type         | NO       | string           | type of the field
multiline    | YES      | boolean          | only used with `string` type
vars         | YES      | array of objects | only used with `array` type
conditions   | YES      | array of objects | conditionals in order to hide / display field in frontend

### Allowed Field Types and optional fields

- **string** displays a textfield
- **number** displays a number input
- **boolean** displays a checkbox
- **strings** allows array of strings
- **select** displays a select field with multiple input types
- **array** allows nested variable configuration

## Conditions type

This allows for a more dynamic configuration approach.
It enables fields based on certain conditions

Example Configuration:
```yaml
vars:
  # bar is a boolean
  - name: "bar"
    description: "..."
    type: "boolean"
  # baz is a select field with 2 options "optionA" and "optionB"
  - name: "baz"
    description: "..."
    type: "select"
    options:
      optionA: descriptor for optionA
      optionB: descriptor for optionB
  - name: "foo"
    description: "..."
    type: "string"
    conditions:
      - baz: "optionA"
        bar: true
      - baz: "optionB
```

Field `foo` will only be displayed when:

`baz` equals `"optionA"` **AND** `bar` equals `true`

**OR**

`baz` equals `"optionB"`

## Dependencies

Plugins can have **dependencies**  and **optionalDependencies** those can be defined in the top section of the plugin config, these dependencies must be installed beforehand.

Those dependencies are identified by the plugin meta.yaml name. The difference between **dependencies**  and **optionalDependencies** is that if a dependency defined under **dependencies** has not been found the plugin itself then wont start, where a dependency under **optionalDependencies** will start regardless
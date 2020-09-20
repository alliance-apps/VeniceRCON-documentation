from json import dumps
from types import FunctionType
from os import listdir
from os.path import isfile, join
from yaml import safe_load

def define_env(env):

  # load all schemas for the api
  env.variables.schemas = {}
  schema_path = env.variables.extra["api"]["schema_path"]
  schema_files = [f for f in listdir(schema_path) if f.endswith(".yaml") and isfile(join(schema_path, f))]
  for file in schema_files:
    with open(join(schema_path, file)) as f:
      env.variables.schemas.update(**safe_load(f.read()))
  print(env.variables.schemas)

  @env.filter
  def jsonify(value, indent=4, offset=0, offsetFirst=False):
    list = []
    lines = dumps(value, indent=indent, separators=(',', ': ')).splitlines()
    for i in range(len(lines)):
      if offsetFirst or i > 0:
        list.append(" " * offset + lines[i])
      else:
        list.append(lines[i])
    return "\n".join(list)

  def add_offset():
    return 0

  def length(value):
    return len(value)

  env.filter(length, "len")

  @env.filter
  def method_content_tab(value):
    switcher = {
      "GET": "info",
      "POST": "done",
      "PATCH": "warning",
      "DELETE": "error"
    }
    return switcher.get(value.upper(), "info")

  @env.filter
  def lowercase(value):
    return value.lower()

  @env.filter
  def append_if(value = [], trigger = False, data = False):
    if trigger:
      if isinstance(value, list):
        value.append(data)
      elif isinstance(value, dict):
        value.update(data)
    return value

  @env.macro
  def parse_schema(schema):
    switcher = {
      "object": parse_schema_object,
      "array": parse_schema_array,
      "string": parse_schema_string,
      "number": parse_schema_number,
      "boolean": parse_schema_boolean
    }
    if (is_ref(schema)):
      schema = resolve_ref(schema["$ref"])
    if ("type" in schema):
      res = switcher.get(schema["type"])
    else:
      res = False
    if (isinstance(res, FunctionType)):
      return res(schema)
    else:
      return "_UNKNOWN_"

  def parse_schema_string(schema):
    if "enum" in schema:
      return "|".join(schema["enum"])
    else:
      return "string"

  def parse_schema_number(schema):
    return 0

  def parse_schema_boolean(schema):
    return False

  def parse_schema_array(schema):
    return [parse_schema(schema["items"])]

  def parse_schema_object(schema):
    result = {}
    if "additionalProperties" in schema:
      key = schema["additionalProperties"].get("identifiedBy", "_UNKNOWN_")
      schema["properties"] = {}
      if is_ref(schema["additionalProperties"]):
        props = parse_schema(resolve_ref(schema["additionalProperties"]["$ref"]))
      else:
        props = parse_schema(props)
      schema["properties"][key] = schema["additionalProperties"]
    elif "properties" in schema:
      for key in schema["properties"]:
        if schema["properties"][key].get("nullable", False):
          k = key + "?"
        else:
          k = key
        result[k] = parse_schema(schema["properties"][key])
      return result
    else:
      return {}

  def is_ref(schema):
    return "$ref" in schema

  def resolve_ref(ref):
    if (not ref.startswith("#/")):
      raise("Invalid ref provided ({})".format(ref))
    name = ref[2:]
    if (name in env.variables.schemas):
      return env.variables.schemas[name]
    else:
      return "_UNKNOWN_"
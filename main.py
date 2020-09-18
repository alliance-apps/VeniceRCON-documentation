from json import dumps
from types import FunctionType
from os import listdir
from os.path import isfile, join

def define_env(env):

  # load all schemas for the api
  env.variables.schemas = {}
  schema_path = env.variables.extra["api"]["schema_path"]
  schema_files = [f for f in listdir(schema_path) if f.endswith(".yaml") and isfile(join(schema_path, f))]
  for file in schema_files:
    with open(join(schema_path, file)) as f:
      env.variables.schemas[file[:-5]] = f.read()


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

  @env.filter
  def dictionaryfy(value, indent=4, offset=0, offsetFirst=False):
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

  @env.macro
  def parse_schema(schema):
    switcher = {
      "object": parse_schema_object,
      "array": parse_schema_array,
      "string": parse_schema_string,
      "number": parse_schema_number,
      "boolean": parse_schema_boolean
    }
    res = switcher.get(schema.type)
    if (isinstance(res, FunctionType)):
      return res(schema)
    else:
      return

  def parse_schema_string(schema):
    return "string"

  def parse_schema_number(schema):
    return "number"

  def parse_schema_boolean(schema):
    return "boolean"

  def parse_schema_array(schema):
    return 

  def parse_schema_object(schema):
    result = {}
    for key, value in schema.properties:
      if value.nullable:
        key = key + "?"
      result[key] = parse_schema(value)
    return result

  @env.filter
  def append_if(value = [], trigger = False, data = False):
    if trigger:
      if isinstance(value, list):
        value.append(data)
      elif isinstance(value, dict):
        value.update(data)
    return value
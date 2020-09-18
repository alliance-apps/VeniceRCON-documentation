from json import dumps

def define_env(env):

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
    return "NOT_IMPLEMENTED"

  @env.filter
  def append_if(value = [], trigger = False, data = False):
    if trigger:
      if isinstance(value, list):
        value.append(data)
      elif isinstance(value, dict):
        value.update(data)
    return value
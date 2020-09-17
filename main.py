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
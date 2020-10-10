import json

config_path = '/home/pi/ro/config.json'
f = open(config_path, 'r')
config = f.read()
f.close()
try:
  config = json.loads(config)
  print('File correct')
except:
  print('File not correct')
#

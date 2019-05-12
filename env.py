import urllib.request
import json

url = 'http://mdc2vr4074:8181/ActivitiUI/getDeploymentDetails?processInstanceId=3942121'

json_obj = urllib.request.urlopen(url)

data = json.load(json_obj)

for i, entry in enumerate(data):
    try:
      print(entry['applicationName'], ':', entry['version'])
    except:
      continue

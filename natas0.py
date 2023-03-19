#view source
import requests
import re

user="natas0"
password=user
url='http://%s.natas.labs.overthewire.org' % user

response=requests.get(url,auth=(user,password))
content=response.text
print (re.findall('The password for natas1 is (.*) -->',content)[0])
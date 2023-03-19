#view source
import requests
import re

user="natas1"
password="g9D9cREhslqBKtcA2uocGHPfMZVzeFK6"
url='http://%s.natas.labs.overthewire.org' % user

response=requests.get(url,auth=(user,password))
content=response.text

print (re.findall('The password for natas2 is (.*) -->',content)[0])
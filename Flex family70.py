import requests
import time
import os
import random
from time import sleep
import pyfiglet
import base64
from bs4 import BeautifulSoup
Z = '\033[1;31m' #احمر
lll = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
os=pyfiglet.figlet_format       ( "     __ F L E X __")
print(Z+os)

print('_'*65)

os=("by: MR ALAA")

number='01097644586'
print()
password="Kings123@1"
print()
number2=input(" \033[2;32mEnter Your Number :")
print()
password2='Kings123@1'
print()

gcv=input("\033[2;36mThe Number Of Flex :")
print()

qwe=3000
zxc=100
jt=int(gcv)
k=(qwe*jt/zxc)
oopl=str(k)
print()
lokae=('              '+(lll+oopl))
print(lokae)
print('\033[2;31mThe Flex')
print()
y=input('Can t go back  (y/n) : ')

if str('y') == str(y):
   	print('ok')
        
else:
	print('\033[2;35mThe order has been cancelled ')
	print('\033[2;31m_'*65)
	hhhhgg
	hhhyo
	jfkfifjfj

vpn="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"



vpn2={
    "Accept":"application/json, text/plain, */*",
    "Connection":"keep-alive",
    "x-dynatrace":"MT_3_17_998679495_45-0_a556db1b-4506-43f3-854a-1d2527767923_0_18957_273",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "x-agent-device":"RMX1911",
    "x-agent-version":"2021.12.2",
    "x-agent-build":"493",
    "Content-Type":"application/x-www-form-urlencoded",
    "Content-Length":"143",
    "Host":"mobile.vodafone.com.eg",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
    }
    
    
vpn3={
"username":number2,

"password":password2,

"grant_type":"password",

"client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",

"client_id":"my-vodafone-app"
    }    
    
    
z=requests.post(vpn, headers=vpn2, data=vpn3)

lok=z.json()["access_token"]

print("="*40)





print("=" * 40)
url="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"



headers={
    "Accept":"application/json, text/plain, */*",
    "Connection":"keep-alive",
    "x-dynatrace":"MT_3_17_998679495_45-0_a556db1b-4506-43f3-854a-1d2527767923_0_18957_273",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "x-agent-device":"RMX1911",
    "x-agent-version":"2021.12.2",
    "x-agent-build":"493",
    "Content-Type":"application/x-www-form-urlencoded",
    "Content-Length":"143",
    "Host":"mobile.vodafone.com.eg",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
    }
    
    
data={
"username":number,

"password":password,

"grant_type":"password",

"client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",

"client_id":"my-vodafone-app"
    }    
    
    
Ahmed=requests.post(url, headers=headers, data=data)

jwt=Ahmed.json()["access_token"]


print("\033[1;33m=" * 40)


url2="https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"

hd={
    
    "Host": "mobile.vodafone.com.eg",
    "msisdn": number,
    "api-version":"v2",
    "x-agent-operatingsystem":"A225FXXU3BVF1",
    "clientId":"AnaVodafoneAndroid",
    "Authorization": "Bearer "+(jwt)+"",
    "x-agent-device":"a22",
    "Accept": "application/json",
    "x-agent-version":"2022.2.1.2",
    "x-agent-build":"503",
    "Accept-Language":"ar",
    "Content-Type":"application/json; charset=UTF-8",
    "Content-Length":"532",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
}
json={"category": [{"listHierarchyId": "PackageID", "value": "515"}, {"listHierarchyId": "TemplateID", "value": "47"}, {"listHierarchyId": "TierID", "value": "515"}, {"listHierarchyId": "familybehavior", "value": "percentage"}], "name": "FlexFamily", "parts": {"characteristicsValue": {"characteristicsValue": [{"characteristicName": "quotaDist1", "type": "percentage", "value": gcv,}]}, "member": [{"id": [{"schemeName": "MSISDN", "value":number,}], "type": "Owner"}, {"id": [{"schemeName": "MSISDN", "value":number2}], "type": "Member"}]}, "type": "SendInvitation"}


loka=requests.patch(url2, headers=hd, json=json).text
url3="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
headers3={
    "Accept":"application/json, text/plain, */*",
    "Connection":"keep-alive",
    "x-dynatrace":"MT_3_17_998679495_45-0_a556db1b-4506-43f3-854a-1d2527767923_0_18957_273",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "x-agent-device":"RMX1911",
    "x-agent-version":"2021.12.2",
    "x-agent-build":"493",
    "Content-Type":"application/x-www-form-urlencoded",
    "Content-Length":"143",
    "Host":"mobile.vodafone.com.eg",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
    }
    
    
data3={
"username":number2,

"password":password2,

"grant_type":"password",

"client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",

"client_id":"my-vodafone-app"
    }    
    
    
z=requests.post(url3, headers=headers3, data=data3)

lok=z.json()["access_token"]


print("=" * 40)


url4="https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"


hd4={
    
    "Host": "mobile.vodafone.com.eg",
    "x-dynatrace":"MT_3_13_2611661057_68-0_a556db1b-4506-43f3-854a-1d2527767923_0_77308_312",
    "msisdn": number2,
    "api-version":"v2",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "Authorization": "Bearer "+(lok)+"",
    "x-agent-device":"RMX1911",
    "Accept": "application/json",
    "x-agent-version":"2022.2.1.2",
    "x-agent-build":"503",
    "Accept-Language":"ar",
    "Content-Type":"application/json; charset=UTF-8",
    "Content-Length":"302",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
}

json4={"category": [{"listHierarchyId": "TemplateID", "value": "47"}], "name": "FlexFamily", "parts": {"member": [{"id": [{"schemeName": "MSISDN", "value":number}], "type": "Owner"}, {"id": [{"schemeName": "MSISDN", "value":number2}], "type": "Member"}]}, "type": "AcceptInvitation"}
    
    
rreq4=requests.patch(url4, headers=hd4, json=json4).text

if str('{}') in str(rreq4):
	il=pyfiglet.figlet_format(" Added successfully ")
	print(il)
else:
	ju=pyfiglet.figlet_format('erorr')
	print(Z+ju)
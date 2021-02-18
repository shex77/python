try:
import uuid
import time
except Exception as e:
print(e)

logo = ("""

("--------------------------")

("Instagram ib2_n)

("--------------------------")

""")

print(logo)

user = input(': ')

password = input(': ')

target = str(input((":")))

sle = int(input(": "))

def login():

global target

r = requests.Session()

uid = str(uuid.uuid4())

url = "https://i.instagram.com/api/v1/accounts/login/"

headers = {

'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',

"Accept": "*/*",

"Accept-Encoding": "gzip, deflate",

"Accept-Language": "en-US",

"X-IG-Capabilities": "3brTvw==",

"X-IG-Connection-Type": "WIFI",

"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",

'Host': 'i.instagram.com'

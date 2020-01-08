import json

import requests

token_url = r'https://openapi.italent.cn/OAuth/Token'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {"app_id": 909, "tenant_id": 108462,
        "secret": "333cba033e7a4f189a849110bbfd41bb", "grant_type": "client_credentials"}

res = requests.post(token_url, headers=headers, data=data)
print(res.headers)
print(res.json())
token = res.json()['access_token']
print(token)
new_headers = {
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+token
}
new_data = {"Year": 2019, "AttendanceOrg": 0,
            "PageIndex": 1, "PageSize": 100, "TenantId": 108462}
# print('New Headers:', new_headers)
request_url = r'https://openapi.italent.cn/attendance/v1/108462/WorkCalendar/GetWorkCalendars'
print(json.dumps(new_data))
res = requests.post(request_url, headers=new_headers,
                    data=json.dumps(new_data))
# print(res)
print(res.json())

from pyicloud import PyiCloudService


api = PyiCloudService('rd8893g7sb@icloud.com', 'Aa112211')

list = api.reminders.lists

for item in list:
    print(item)
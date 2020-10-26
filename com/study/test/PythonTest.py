from pyicloud import PyiCloudService

api = PyiCloudService('rd8893g7sb@icloud.com', 'Aa112211')

reminder = api.reminders

list = reminder.lists

for item in list:
    print(item)

guid = reminder.postReminder('test-new-reminder-4', description="")
reminder.postShareEmail(guid, emails=['826179140@qq.com', '1028859195@qq.com'])

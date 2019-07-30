from validate_email import validate_email

emails = ['chenxunkun@meorient.com', 'info@epco.net', 'chingpeplo@sina.com', '1028859195@qq.com',
          'info@sanatekhodro.com']

for email in emails:
    is_valid = validate_email(email, verify=True)
    print(email, is_valid)

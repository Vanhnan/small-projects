import re

with open("nums_emails.txt") as f:
    text = f.read()

phone_mo = re.findall(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)", text)
lis_phone = ""
for i in phone_mo:
    lis_phone+=str(i[0])+str(i[1])+"\n"
print(lis_phone)

email_mo = re.findall(r"\S+@\S+", text)
lis_email = ""
for i in email_mo:
    lis_email+=i+"\n"
print(lis_email)

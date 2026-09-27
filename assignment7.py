import re


def find_emails(text):
    pattern = r'[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,4}'
    emails = re.findall(pattern, text)
    return emails


text = input("Enter the text: ")

result = find_emails(text)

print("\nEmail addresses found:")

if len(result) == 0:
    print("No email addresses found.")
else:
    for email in result:
        print(email)
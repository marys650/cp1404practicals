"""
Emails
Estimate: 30 minutes
Actual:   50 minutes
"""
email_dict = {}


def email_split(email):
    username = email.split('@')[0]
    split_name = username.split('.')
    name = ' '.join(split_name).title()
    return name


email = input("Email: ")
while email != "":
    name = email_split(email)
    response = input(f"Is your name {name}? (Y/N) ").upper()
    if response == "" or response == "Y":
        email_dict[email] = name
    else:
        name = input("Name: ").title()
        email_dict[email] = name
    email = input("Email: ")
print("\nEmail dictionary:")
for email, name in email_dict.items():
    print(f"{name} ({email})")

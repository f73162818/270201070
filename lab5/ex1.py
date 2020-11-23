email = input("Enter an email:")
valid_email = "ceng113@example.com"
email = email.lower()
email_parts = email.split("@")
first_half = email_parts[0].replace(".","")
new_email = first_half + "@" + email_parts[1]
print(new_email == valid_email)
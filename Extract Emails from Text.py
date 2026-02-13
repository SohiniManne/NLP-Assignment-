import re

text = """
Contact us at support@example.com or sales123@company.org.
You can also reach admin@test.co.in for more info.
"""

# Regex pattern for emails
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

emails = re.findall(pattern, text)

print("Extracted Emails:")
for email in emails:
    print(email)

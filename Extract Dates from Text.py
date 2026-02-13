import re

text = "Important dates are 12/05/2023, 01-01-2024 and 2025-12-31."

# Pattern for multiple date formats
pattern = r'\b(\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2})\b'

dates = re.findall(pattern, text)

print("Extracted Dates:")
for date in dates:
    print(date)

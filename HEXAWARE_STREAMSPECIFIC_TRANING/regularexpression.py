import re

def is_valid_phone(number):
    pattern = r'^\d{10}$'
    return re.match(pattern, number) is not None

print(is_valid_phone("9876543210"))  
print(is_valid_phone("12345"))       




text = "Contact us at support@site.com or sales@company.org"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(emails) 



date = "Order placed on 23-04-2025"
match = re.search(r'(\d{2})-(\d{2})-(\d{4})', date)
if match:
    day, month, year = match.groups()
    print(f"Day: {day}, Month: {month}, Year: {year}")




def detect_choice(response):
    match = re.search(r'yes|no', response.lower())
    return match.group() if match else "No match"

print(detect_choice("Yes, I agree."))  
print(detect_choice("No problem."))    



text = "That was so funny hahaha!"
match = re.search(r'(ha)*', text)
print(match.group())  
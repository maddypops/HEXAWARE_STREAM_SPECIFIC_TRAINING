import re

text = "That was so funny hahaha!"
match = re.search(r'(ha)*', text)
print(match.group()) 

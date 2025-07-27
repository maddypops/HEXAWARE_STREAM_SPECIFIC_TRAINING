import os
print("Current Directory:", os.getcwd())
print("Files:", os.listdir('.'))


import math
print("Square Root:", math.sqrt(25))
print("Power:", math.pow(2, 3))


from datetime import datetime
now = datetime.now()
print("Current Time:", now.strftime('%H:%M:%S'))


import random
print("Random Number:", random.randint(1, 100))


import json
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)
print("JSON:", json_str)


import statistics
print("Mean:", statistics.mean([10, 20, 30]))


import re
text = "My number is 123-456-7890"
match = re.search(r'\d{3}-\d{3}-\d{4}', text)
print("Phone:", match.group())
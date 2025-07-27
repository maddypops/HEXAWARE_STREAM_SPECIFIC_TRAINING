marks = [45, 67, 89, 32, 76]
passed = list(filter(lambda x: x >= 50, marks))
print(passed)  

prices_usd = [10, 20, 30]
prices_inr = list(map(lambda x: x * 83.2, prices_usd))
print(prices_inr) 

from functools import reduce
cart = [200, 150, 350]
total = reduce(lambda x, y: x + y, cart)
print(total)  

names = ["Alice", "Bob", "Charlie"]
scores = [82, 76, 91]
result = list(zip(names, scores))
print(result)  

questions = ["What is Python?", "What is List?"]
for i, q in enumerate(questions, start=1):
    print(f"Q{i}: {q}")


students = [("Alice", 90), ("Bob", 70), ("Charlie", 85)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)


access_rights = [True, False, True]
print(any(access_rights))  
print(all(access_rights)) 


salaries = [35000, 47000, 29000]
print(sum(salaries))  
print(max(salaries))  
print(min(salaries))  


names = ["Alice", "Bob", "Charlie"]
print(list(reversed(names)))  
age = int(input("Hi there! Please enter your age: "))

totals = 0

for i in range(1, age + 1):
    totals = totals + i
    
print(f"The sum of all numbers from 1 to {age} is: {totals}")


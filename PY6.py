
# Program to demonstrate dictionary functions

# Create a dictionary
employee = {
    "name": "Shylaja",
    "id": 242,
    "dept": "IT",
    "sal": 150000
}

print("The dictionary is:", employee)

# Access values using keys
print("Name:", employee["name"])
print("ID:", employee["id"])
print("Department:", employee["dept"])
print("Salary:", employee["sal"])

# Demonstrate dictionary methods
print("Using get():", employee.get("name"))
print("Keys:", employee.keys())
print("Values:", employee.values())
print("Items:", employee.items())

# Add, update and delete
employee["age"] = 20
employee["sal"] = 18000
del employee["age"]

print("Updated dictionary:", employee)

# Count the frequency of each character in a string
text = input("Enter string: ")
frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

print("Character frequency:")

for ch, count in frequency.items():
    print(ch, ":", count)

# DICTIONARY-FUNCTIONS-IN-PYTHON
Aim

   To write a Python program to demonstrate dictionary-related functions, including creating a dictionary, accessing values using keys, adding, updating, deleting elements, and counting the frequency of each character in a string.
   
Algorithm

1.Start the program.

2.Create an employee dictionary with the keys name, id, dept, and sal.

3.Display the dictionary and access its values using keys.

4.Demonstrate dictionary methods such as get(), keys(), values(), items(), and update().

5.Add a new key-value pair, update an existing value, and delete a key.

6.Accept a string from the user.

7.Create an empty dictionary named frequency.

8.Traverse each character in the string.

9.If the character already exists in the dictionary, increment its count; otherwise, initialize its count to 1.

10.Display the frequency of each character.

11.Stop the program.

Source Code


# Program to demonstrate dictionary functions

# Create a dictionary

employee = {
    "name": "Shylajal",
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

Output
<img width="1920" height="1200" alt="Screenshot 2026-10-24 193650" src="https://github.com/user-attachments/assets/12653aca-1a70-4f4a-a345-a5568c7ebdfe" />

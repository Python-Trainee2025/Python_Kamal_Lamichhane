# Create a dictionary with a person's name and contact info for a small company,
# take the input from a user to search for a user using their name,
# return the number (example user will search for 'Ram' and if user exists,
# their phone number is returned)

employees = [
    {
        "name": "Ram",
        "contact": 9849000001
    },
    {
        "name": "Shyam",
        "contact": 9802398765
    },
    {
        "name": "Sita",
        "contact": 9841424344
    },
    {
        "name": "Gita",
        "contact": 9818192921
    },
]

nameToSearch = input("Enter the name to search: ")

found = 0
for employee in employees:
    # print(employee["name"], nameToSearch, employee["contact"])
    if employee["name"].upper() == nameToSearch.upper():
        print(f'Phone number of {nameToSearch} is: {employee["contact"]}')
        found = 1
        break

if not found:
    print(f'{nameToSearch} not found.')
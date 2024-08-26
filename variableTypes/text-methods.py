# Declaration
full_name = "Arthur Pereira Machado"
altered_name = "xArthur Pereira Machadox"

name = "Arthur"
surname = "Pereira Machado"

phone = "(19) 97325-0502"

# Methods
print("Upper method: ", full_name.upper())
print("Lower method: ", full_name.lower())
print("Get letter: ", full_name[0])
print("Count method: ", full_name.count("h"))
print("Find method: ", full_name.find("h"))
print("Encode method: ", full_name.encode())
print("Decode method: ", full_name.encode().decode())
print("Replace method: ", full_name.replace("a", "b"))
print("Replace sanitizing data: ", phone.replace("(", "").replace(")", "").replace(" ", "").replace("-", ""))
print("Join method: ", '-'.join(name))
print("Split method: ", full_name.split())
print("Strip method: ", altered_name.strip("x"))
print("Right Strip method: ", altered_name.rstrip("x"))
print("Left Strip method: ", altered_name.lstrip("x"))
print("Starts with method true: ", full_name.startswith("Art"))
print("Starts with method false: ", full_name.startswith("Rob"))
print("In method: ", "reir" in full_name)
print("Not In method false: ", "Art" not in full_name)
print("Not In method true: ", "art" not in full_name)
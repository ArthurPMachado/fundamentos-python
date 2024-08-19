# Declaration
full_name = "Arthur Pereira Machado"

full_name_quotes = """Arthur 
Pereira Machado"""

full_name_bar = "Arthur \
Pereira Machado"

name = "Arthur"
surname = "Pereira Machado"

# Formatiing
print("Full name (first form):", full_name)
print("Full name (second form):" + full_name)
print("Full name (third form):" + "Arthur" + "Pereira Machado")
print("Full name (forth form):" + "Arthur", "Pereira Machado")
print("Full name (fifth form):", full_name_quotes)
print("Full name (sixth form):", full_name_bar)
print("Full name (seventh form): %s" % full_name)
print("Full name (eighth form): %s %s" % (name, surname))
print(f"Full name (ninth form): {name} {surname}")
print("Full name (tenth form): {} {}".format(name, surname))

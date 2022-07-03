name = "ada lovelace"
print(name.title())
#the method title() makes each work begin with a capital letter. The . after name means that the title is affecting the variable

print (name.upper())
print (name.lower())

first_name = "aDa"
last_name = "lovElace"
full_name = f"{first_name} {last_name}"
print(full_name)

#the f is for format, meaning it keeps the original format placed on the values.

message = (f"Hello, {full_name.title()}!")
print(message)
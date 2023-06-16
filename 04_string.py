name = "Nora"
last_name = "Azua Campos"
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Nora"
print(quote)

quote2 = 'She said "Hello" '
print(quote2)

# format es para manipular su formato o estructura del texto
template = "Hola, mi nombre es " + name + " y mi a pellido es " + last_name
print('v1', template)

template = "Hola mi nombre es {} y mi apellido es {}".format(name,last_name)
print('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)

my_age = 39
template = f"Hola, mi nombre es {name} {last_name} y mi edad es {my_age} años"
print('v4', template)
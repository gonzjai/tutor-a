text = 'hola2 alumnos2'
print('2' in text)
print(text.count('2'))
print(text.index('2'))
print(text.index('9'))
text = text.replace(text[0:4],'')
print(text) 
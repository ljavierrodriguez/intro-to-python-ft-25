# Loops

""" 

for element in secuence:
    sentences


while condition:
    sentences

range(start = 0, stop = x, step = 1)

"""

for num in range(1, 11):
    print(num) # 1 2 3 4 5 6 7 ...


nombres = ["Hugo", "Paco", "Luis"]

for i in range(len(nombres)):
    print(nombres[i])

for nombre in nombres:
    print(nombre)

i = 0
while i < len(nombres):
    print(nombres[i])
    # i = i + 1
    i += 1

i = 1
while i <= 10:
    print(i)
    i+=1
print ("Hola, Mundoo")

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

frutas = ["manzana", "banana", "messi"]
print(frutas)
frutas.remove("messi")
print(frutas)
frutas_eliminada = frutas.pop("banana")
print(frutas)
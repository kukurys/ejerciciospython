
compra=float(input("digite valor de la compra"))
balota=(input("elija color de la balota,(rojo,amarillo,negra,azul)"))
# valor_compra= input ("digite el valor de la variable valor_compra: ")

while compra >= 50000:
    if balota=="rojo":
        descuento=compra*0.10
        print(descuento)
    
    elif balota=="azul":
        descuento=compra*0.15


    elif balota=="amarillo":
        descuento=compra*0.5

    
    elif balota=="negra":
        descuento=valor_compra-(valor_compra)

    question = input('Desea continuar: ')

    if question == 'no':
        break
















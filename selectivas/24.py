# estrategia de descuento , segun valor de la compra 
valor_compra=0
descuento=0
balota=0
valor_compra=int (input ("digite el valor de la variable valor_compra: "))
color_balota=input("ingrese el color de la balota: ")
if valor_compra>=50000 and color_balota=="roja":
    
    descuento=valor_compra-(valor_compra*0.1)
    print(f"sacaste la balota roja el valor de la compra es {valor_compra} y el total a pagar: {descuento}")
elif valor_compra>=50000 and color_balota=="verde":
    descuento=valor_compra-(valor_compra*0.015)
    print(f"sacaste la balota verde el valor de la compra es {valor_compra} y el total a pagar: {descuento}")
elif valor_compra>=50000 and color_balota=="azul":
    descuento=valor_compra-(valor_compra*0.2)
    print(f"sacaste la balota azul el valor de la compra es {valor_compra} y el total a pagar: {descuento}")
elif valor_compra>=50000 and color_balota=="amarilla":
    descuento=valor_compra-(valor_compra*0.5)
    print(f"sacaste la balota amarilla el valor de la compra es {valor_compra} y el total a pagar: {descuento}")
elif valor_compra>=50000 and color_balota=="negra":
    descuento=valor_compra-(valor_compra)
    print(f"sacaste la balota negra el valor de la compra es {valor_compra} y el total a pagar: {descuento}")
elif valor_compra<50000:
    print(f"no participas en el sorteo y en total a pagas: {valor_compra}")



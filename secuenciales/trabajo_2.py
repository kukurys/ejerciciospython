
#valor compra con descuento

valor_compra=0
descuento=0
if valor_compra==0:
    print("no tendra descuento")
elif valor_compra<50000:
    descuento=valor_compra-(valor_compra*0.1)
    print(f"el valor de la compra es {valor_compra} total a pagar {descuento}")
elif valor_compra>50000:

    descuento=valor_compra-(valor_compra*0.05)
    print(f"el valor de la compra es {valor_compra} total a pagar {descuento}")
elif valor_compra==50000:

    descuento=valor_compra-(valor_compra*0.07)
    print(f"el valor de la compra es {valor_compra} total a pagar {descuento}")

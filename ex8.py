lista = ['Intel Core i9-9900KF.','Gigabyte B360M-Gaming 3','32GB DDR4 GDDR6','GeForce RTX 2080Ti','1TB de HD + 480GB de SSD','80PLUS 600W','Noctua NH-D15']
print('lista de todas as suas compras :', (lista))
print('Notamos que o preço da compra ultrapassou o orçamento limite definido pelo cliente, por isso, tomamos a liberdade de retirar a placa de vídeo e o cooler master da sua lista de compras.')
del lista[3]
del lista[5]
print('Nova lista :',(lista))
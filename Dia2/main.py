from Produto import Produto
from Pedidos import Pedido, PedidoViewer


banana = Produto(nome="Banana", preco=2.5, id=1)
laranja = Produto(nome="Laranja", preco=3.5, id=2)
mamao = Produto(nome="Mamão", preco=4.5, id=3)

pedido = Pedido(lista_de_produtos=[banana, laranja, mamao])
nota_fiscal = PedidoViewer().exibe_pedido(pedido=pedido)
print("Quantidade de produtos:", PedidoViewer(
).quantidade_de_produtos(pedido=pedido))

# SOLID

# S - Single Responsability Principle

from typing import List
from Produto import Produto


class Pedido:
    def __init__(self, lista_de_produtos: List[Produto]):
        self.lista_de_produtos = lista_de_produtos

    def adicionar_produto(self, produto: Produto):
        self.lista_de_produtos.append(produto)

    def remover_produto(self, produto: Produto):
        self.lista_de_produtos.remove(produto)

    def exibir_produtos(self):
        for produto in self.lista_de_produtos:
            print(produto.nome)

    def cadastrar_produto(self):
        pass

    def adiciona_desconto_ao_produto_do_pedido(self, indice_do_produto_a_ser_modificado):
        produto_modificado: Produto = self.lista_de_produtos[indice_do_produto_a_ser_modificado]
        desconto = produto_modificado.preco * 0.15
        produto_modificado.preco = produto_modificado.preco - desconto
        self.lista_de_produtos[indice_do_produto_a_ser_modificado] = produto_modificado

        return produto_modificado


class PedidoViewer:
    def exibe_pedido(self, pedido: Pedido):
        for produto in pedido.lista_de_produtos:
            print(produto.id)
            print(produto.nome)
            print(produto.preco)

    def quantidade_de_produtos(self, pedido: Pedido):
        return len(pedido.lista_de_produtos)


class PedidoRepository:
    def salvar_pedido(self, pedido: Pedido):
        pass

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f'Nome: {self.nome}, Preço: R$ {self.preco:.2f}, Quantidade: {self.quantidade}'


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto)

    def atualizar_quantidade(self, produto, nova_quantidade):
        produto.quantidade = nova_quantidade

class Interface:
    def __init__(self):
        self.estoque = Estoque()

    def menu(self):
        print('1 - Adicionar produto')
        print('2 - Remover produto')
        print('3 - Atualizar quantidade de produto')
        print('4 - Listar produtos')
        print('0 - Sair')

    def adicionar_produto(self):
        nome = input('Nome do produto: ')
        preco = float(input('Preço do produto: '))
        quantidade = int(input('Quantidade do produto: '))
        produto = Produto(nome, preco, quantidade)
        self.estoque.adicionar_produto(produto)

    def remover_produto(self):
        nome = input('Nome do produto: ')
        produto = next((p for p in self.estoque.produtos if p.nome == nome), None)
        if produto:
            self.estoque.remover_produto(produto)
            print(f'{nome} removido do estoque')
        else:
            print(f'{nome} não encontrado no estoque')

    def atualizar_quantidade(self):
        nome = input('Nome do produto: ')
        produto = next((p for p in self.estoque.produtos if p.nome == nome), None)
        if produto:
            nova_quantidade = int(input('Nova quantidade do produto: '))
            self.estoque.atualizar_quantidade(produto, nova_quantidade)
            print(f'Quantidade de {nome} atualizada para {nova_quantidade}')
        else:
            print(f'{nome} não encontrado no estoque')

    def listar_produtos(self):
        self.estoque.listar_produtos()

    def executar(self):
        while True:
            self.menu()
            opcao = input('Digite uma opção: ')
            if opcao == '1':
                self.adicionar_produto()
            elif opcao == '2':
                self.remover_produto()
            elif opcao == '3':
                self.atualizar_quantidade()
            elif opcao == '4':
                pass

if __name__ == '__main__':
    interface = Interface()
    interface.executar()

lista_telefonica = {}


def menu():
    print("\n==============================")
    print("       LISTA TELEFONICA")
    print("==============================")
    try:
        escolha = int(
            input(
                "\n1 - Listar contatos"
                "\n2 - Adicionar contato"
                "\n3 - Buscar contato"
                "\n4 - Remover contato"
                "\n0 - Sair"
                "\n\nEscolha: "
            )
        )
    except ValueError:
        print("\nDigite um numero valido.")
        escolha = -1
    return escolha


def adicionar(nome, num):
    lista_telefonica[nome] = num
    print(f"\n{nome} adicionado!")


def buscar():
    nome = input("\nDigite o nome: ")
    if nome in lista_telefonica:
        print(f"\n{nome}: {lista_telefonica[nome]}")
    else:
        print("\nContato não encontrado.")


def listar():
    print("\n==============================")
    if not lista_telefonica:
        print("        LISTA VAZIA!")
    else:
        print("        Seus contatos:")
        print("==============================")
        for i, (nome, num) in enumerate(lista_telefonica.items(), start=1):
            print(f"  {i}.) {nome} - {num}")
    print("==============================")


def remover():
    nome = input("\nDigite o nome: ")
    if nome in lista_telefonica:
        del lista_telefonica[nome]
        print(f"\n{nome} removido.")
    else:
        print("\nContato nao encontrado.")


escolha = menu()
while escolha != 0:
    if escolha == 1:
        listar()
    elif escolha == 2:
        nome = input("\nDigite o nome: ")
        if nome in lista_telefonica:
            print("\nNome já existe.")
        else:
            num = input("Digite o numero: ")
            adicionar(nome, num)

    elif escolha == 3:
        buscar()
    elif escolha == 4:
        remover()

    input("\nPressione Enter para continuar...")
    escolha = menu()

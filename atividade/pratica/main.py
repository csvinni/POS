import requests

URL = "http://127.0.0.1:8000"

def menu():
    print("\nMENU:")
    print("1 - Listar veículos")
    print("2 - Buscar veículo por placa")
    print("3 - Cadastrar veículo")
    print("4 - Editar veículo")
    print("5 - Deletar veículo")
    print("6 - Sair")
    return input("Escolha a opção: ")

while True:
    opcao = menu()

    if opcao == "1":
        r = requests.get(f"{URL}/veiculos")
        print("Veículos cadastrados:", r.json())

    elif opcao == "2":
        placa = input("Informe a placa do veículo: ")
        r = requests.get(f"{URL}/veiculos/{placa}")
        if r.status_code == 200:
            print("Veículo encontrado:", r.json())
        else:
            print("Veículo não encontrado.")

    elif opcao == "3":
        dados = {
            "nome": input("Nome: "),
            "marca": input("Marca: "),
            "modelo": input("Modelo: "),
            "placa": input("Placa: ")
        }
        r = requests.post(f"{URL}/veiculos", json=dados)
        if r.status_code == 200:
            print("Veículo cadastrado:", r.json())
        else:
            print("Erro:", r.json()["detail"])

    elif opcao == "4":
        placa = input("Placa do veículo a editar: ")
        novos_dados = {
            "nome": input("Novo nome: "),
            "marca": input("Nova marca: "),
            "modelo": input("Novo modelo: "),
            "placa": input("Nova placa: ")
        }
        r = requests.put(f"{URL}/veiculos/{placa}", json=novos_dados)
        if r.status_code == 200:
            print("Veículo atualizado:", r.json())
        else:
            print("Erro:", r.json()["detail"])

    elif opcao == "5":
        placa = input("Placa do veículo a remover: ")
        r = requests.delete(f"{URL}/veiculos/{placa}")
        if r.status_code == 200:
            print("Veículo removido:", r.json())
        else:
            print("Erro:", r.json()["detail"])

    elif opcao == "6":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")

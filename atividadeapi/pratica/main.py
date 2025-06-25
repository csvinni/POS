import requests

def menu():
    print("Menu- escolhe a opção")
    print("1 - Listar todos os livros")
    print("2 - Pesquisar livro por título")
    print("3 - Cadastrar um livro")
    print("4 - Deletar um livro")
    print("5 - Sair")
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    url = "http://127.0.0.1:8000"

    while True:
        opcao = menu()
        # Listar todos os livros
        if opcao == "1":
            
            r = requests.get(f"{url}/livros")
            if r.status_code == 200:
                print("\ lista de livros:")
                print(r.json())

        
        elif opcao == "2":
            # Pesquisar livro por título
            
            titulo = input("Digite o título do livro que deseja pesquisar: ")
            r = requests.get(f"{url}/livros/{titulo}")
            if r.status_code == 200:
                print("\livro encontrado:")
                print(r.json())
            else:
                print("livro não encontrado!")

        elif opcao == "3":
            # Cadastrar um livro
            titulo = input("Digite o título do livro: ")
            ano = int(input("Digite o ano do livro: "))
            edicao = int(input("Digite a edição do livro: "))
            livro = {
                "titulo": titulo,
                "ano": ano,
                "edicao": edicao
            }
            r = requests.post(f"{url}/livros", json=livro)
            if r.status_code == 200 or r.status_code == 201:
                print("\livro cadastrado com sucesso!")
                print(r.json())

        elif opcao == "4":
            # Deletar um livro
            titulo = input("Digite o título do livro que deseja deletar: ")
            r = requests.delete(f"{url}/livros/{titulo}")
            if r.status_code == 200:
                print("\n Livro deletado com sucesso!")
                print(r.json())
            else:
                print("livro não encontrado para deletar!")

        elif opcao == "5":
            # Sair
            print("sair")
            break
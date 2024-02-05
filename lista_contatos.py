

def adicionar_contato(contatos):
  print("\nAdicionando contato")
  nome = input("Nome: ")
  telefone = input("Telefone: ")
  email = input("Email: ")
  contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
  contatos.append(contato)
  print("\nContato adicionado com sucesso")
  return contatos

def ver_contatos(contatos):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    nome = contato["nome"]
    telefone = contato["telefone"]
    email = contato["email"]
    favorito = "♡" if contato["favorito"] else ""
    print(f"{indice}. {nome} - {telefone} - {email} - Favorito: {favorito}")
  return

def editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["nome"] = novo_nome
    contatos[indice_contato_ajustado]["telefone"] = novo_telefone
    contatos[indice_contato_ajustado]["email"] = novo_email
    print(f"Contato {indice_contato} atualizado para {novo_nome} - {novo_telefone} - {novo_email}")
  else:
    print("Contato não encontrado")
  return

def favoritar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"Contato {indice_contato} favoritado")
  else:
    print("Contato não encontrado")
  return

def exibir_contato_favorito(contatos):
  print("\nLista de contatos favoritos:")
  for indice, contato in enumerate(contatos, start=1):
    if contato["favorito"]:
      nome = contato["nome"]
      telefone = contato["telefone"]
      email = contato["email"]
      favorito = contato["favorito"]
      print(f"{indice}. {nome} - {telefone} - {email} - Favorito: {favorito}")
  return

def excluir_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos.pop(indice_contato_ajustado)
    print(f"Contato {indice_contato} excluído")
  else:
    print("Contato não encontrado")
  return

contatos = []
contatos_favoritos = []


while True:
  print("\nMenu da lista de contatos")
  print("\n1 - Adicionar Contato")
  print("2 - Ver contatos")
  print("3 - Editar contato")
  print("4 - Favoritar contato")
  print("5 - Exibir contatos favoritos")
  print("6 - Excluir contato")
  print("7 - Sair")

  escolha = input("\nEscolha uma opção: ")

  if escolha == "1":
    contatos = adicionar_contato(contatos)
  
  elif escolha == "2":
    ver_contatos(contatos)

  elif escolha == "3":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja editar: ")
    novo_nome = input("Digite o novo nome do contato: ")
    novo_telefone = input("Digite o novo telefone do contato: ")
    novo_email = input("Digite o novo email do contato: ")
    editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)

  elif escolha == "4":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja favoritar: ")
    favoritar_contato(contatos, indice_contato)

  elif escolha == "5":
    exibir_contato_favorito(contatos)

  elif escolha == "6":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja excluir: ")
    excluir_contato(contatos, indice_contato)
     
  elif escolha == "7":
   break

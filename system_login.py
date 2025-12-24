import json
import os
import random

ARQUIVO = "banco.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def salvar_dados(usuarios):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)
        
def gerar_codigo():
    return str(random.randint(100000, 999999))

usuarios = carregar_dados()
dominios_permitidos = ["gmail.com", "outlook.com", "hotmail.com", "yahoo.com", "icloud.com"]

def perfil_usuario():
    ()

def trocar_senha():

    while True:

        print("""
┌──────────────────────────────────────┐
│            RECUPERAR SENHA           │
│──────────────────────────────────────│
│                                      │
│  E-mail/Usuario:                     │
│  0 ➜  Voltar                         │
│                                      │
└──────────────────────────────────────┘
""")
        while True:
            recuperar_senha = input("Digite seu e-mail ou usuário: ")

            if recuperar_senha == "0":
                return
        
            usuario_encontrado = next((u for u in usuarios if u["email"] or u["usuario"] == recuperar_senha), None)

            if usuario_encontrado:
                codigo_gerado = gerar_codigo()
                print(f"\nCódigo enviado para o e-mail: {recuperar_senha}")
                print(f"(DEBUG TEMPORÁRIO) Código gerado: {codigo_gerado}\n")
                break

            else:
                print(f"O e-mail {recuperar_senha}, não existe!\n")
                continue

        while True:
            print("""
┌──────────────────────────────────────┐
│            RECUPERAR SENHA           │
│──────────────────────────────────────│
│                                      │
│  Codigo:                             │
│                                      │
│  Codigo enviado pelo e-mail          │
│  0 ➜  Voltar                         │
│                                      │
└──────────────────────────────────────┘
""")
        
            codigo_email = input("Digite o codigo: ")

            if codigo_email == "0":
                return

            if codigo_email == codigo_gerado:
                print("\nCódigo correto! Agora você pode redefinir sua senha.")
                break

            else:
                print("\nCódigo incorreto! Tente novamente.\n")
                continue

        while True:

            print("""
┌──────────────────────────────────────┐
│             TROCAR SENHA             │
│──────────────────────────────────────│
│                                      │
│  Nova senha:                         │
│  Confirmar senha:                    │
│  0 ➜  Voltar                         │
│                                      │
└──────────────────────────────────────┘
""")

            nova_senha = input("Digite a nova senha: ")
            confirmar_senha = input("Confirme a nova senha: ")

            if nova_senha == confirmar_senha:
                usuario_encontrado["senha"] = nova_senha
                print(f"""
┌──────────────────────────────────────┐
│             TROCAR SENHA             │
│──────────────────────────────────────│
│                                      │
│  Nova senha:  {nova_senha}           
│  Confirmar senha:  {confirmar_senha} 
│  0 ➜  Voltar                         │
│                                      │
└──────────────────────────────────────┘
""")
                print("\nSenha alterada com sucesso!\n")
                return
            
            else:
                print("\nAs senhas não coincidem. Tente novamente.\n")

def fazer_cadastro():
    
    while True:

        print("""
┌──────────────────────────────────────┐
│                REGISTRO              │
│──────────────────────────────────────│
│                                      │
│  E-mail:                             │
│  Confirmar E-mail:                   │
│  Usuario:                            │
│  Senha:                              │
│  Confirmar Senha:                    │
│  0 ➜  Voltar                         │
│                                      │
└──────────────────────────────────────┘
""")
        while True:
            email = input("Digite o e-mail: ").strip()

            if email == "0":
                return

            if "@" not in email or email.startswith("@") or email.endswith("@"):
                print("O e-mail precisa ter um domínio válido. Ex: usuario@gmail.com.")
                continue

            dominio = email.split("@", 1)[1]

            if dominio not in dominios_permitidos:
                print("Domínio inválido! Utilize um dos seguintes:")
                print(", ".join(dominios_permitidos))
                continue

            break


        print(f"""
┌──────────────────────────────────────┐
│                REGISTRO              │
│──────────────────────────────────────│
│                                      │
│  E-mail:  {email}                    
│  Confirmar E-mail:                   │
│  Usuario:                            │
│  Senha:                              │
│  Confirmar Senha:                    │
│  0 ➜  Voltar                         │
│                                      │
└──────────────────────────────────────┘
""")
        while True:

            confirm_email = input("Confirme o e-mail: ")

            if confirm_email == "0":
                return

            if email != confirm_email:
                print("Os e-mails não coincidem. Tente novamente.")
                continue

            if any(u["email"] == email for u in usuarios):
                print("Este e-mail já está cadastrado.\n")
                continue
            break

        print(f"""
┌──────────────────────────────────────┐
│                REGISTRO              │
│──────────────────────────────────────│
│                                      │
│  E-mail:  {email}                    
│  Confirmar E-mail:  {confirm_email}  
│  Usuario:                            │
│  Senha:                              │
│  Confirmar Senha:                    │
│  0 ➜  Voltar                         │
│                                      │
└──────────────────────────────────────┘
""")
        while True:
            usuario = input("Digite o usuário: ").strip()

            if usuario == "0":
                return
            
            if len(usuario) < 5:
                print("O usuário deve ter no mínimo 5 caracteres!")
                continue

            if any(u["usuario"] == usuario for u in usuarios):
                print("Usuário já existe.\n")
                continue
            break

        print(f"""
┌──────────────────────────────────────┐
│                REGISTRO              │
│──────────────────────────────────────│
│                                      │
│  E-mail:  {email}                    
│  Confirmar E-mail:  {confirm_email}  
│  Usuario:  {usuario}                 
│  Senha:                              │
│  Confirmar Senha:                    │
│  0 ➜  Voltar                         │
│                                      │
└──────────────────────────────────────┘
""")
        while True:
            senha = input("Digite a senha (mínimo 5 caracteres): ").strip()

            if senha == "0":
                return

            if len(senha) < 5:
                print("A senha deve ter no mínimo 5 caracteres!")
                continue

            senha_confirm = input("Confirme a senha: ")

            if senha_confirm == "0":
                return

            if senha != senha_confirm:
                print("As senhas não coincidem!")
                continue
            break
            
        senha_mascarada = "*" * len(senha)

        print(f"""
┌──────────────────────────────────────┐
│                REGISTRO              │
│──────────────────────────────────────│
│                                      │
│  E-mail:  {email}                    
│  Confirmar E-mail:  {confirm_email}  
│  Usuario:  {usuario}                 
│  Senha:  {senha_mascarada}           
│  Confirmar Senha:  {senha_mascarada} 
│                                      │
└──────────────────────────────────────┘
""")
    
        usuarios.append({
            "usuario": usuario,
            "email": email,
            "senha": senha
        })

        salvar_dados(usuarios)

        print("\n✔ Cadastro realizado com sucesso!")
        break

def fazer_login():

    while True:

        print("""
┌──────────────────────────────────────┐
│                 LOGIN                │
│──────────────────────────────────────│
│                                      │
│  Usuario:                            │
│  Senha:                              │
│  0 ➜  Voltar                         │
│                                      │
└──────────────────────────────────────┘
""")
        while True:
            usuario_digitado = input("Digite o seu Usuario: ")

            if usuario_digitado == "0":
                return

            usuario_encontrado = next((u for u in usuarios if u["usuario"] == usuario_digitado), None)

            if usuario_encontrado is None:
                print("\nUsuário inexistete, tente novamente.")
                continue

            print("\n✔ Usuário encontrado!\n")

            while True:

                print(f"""
┌──────────────────────────────────────┐
│                 LOGIN                │
│──────────────────────────────────────│
│                                      │
│  Usuario:  {usuario_digitado}        
│  Senha:                              │
│  0 ➜  Voltar                         │
│                                      │
└──────────────────────────────────────┘
""")

                senha_digitada = input("Digite a sua senha: ")

                if senha_digitada == "0":
                    return
            
                if senha_digitada == usuario_encontrado["senha"]:
                    senha_mascarada = "*" * len(senha_digitada)

                    print(f"""
┌──────────────────────────────────────┐
│                 LOGIN                │
│──────────────────────────────────────│
│                                      │
│  Usuario:  {usuario_digitado}        
│  Senha:  {senha_mascarada}           
│                                      │
└──────────────────────────────────────┘

Login realizado com sucesso!
""")
                    return
                else:
                    print("Senha incorreta! Tente novamente.")

def menu():
    print("""
Olá! Seja Bem-Vindo(a) ao nosso painel de login!
""")

    while True:
        print("""
┌──────────────────────────────────────┐
│           PAINEL DE LOGIN            │
│──────────────────────────────────────│
│                                      │
│  1 ➜  Fazer Login                    │
│  2 ➜  Fazer Cadastro                 │
│  3 ➜  Esqueci a Senha                │
│  0 ➜  Sair                           │
│                                      │
└──────────────────────────────────────┘
""")

        opcao = input("Digite o número da opção desejada: ").strip()

        if opcao == "1":
            fazer_login()
        elif opcao == "2":
            fazer_cadastro()
        elif opcao == "3":
            trocar_senha()
        elif opcao == "0":
            print("\nObrigada por usar nosso sistema!\nAté a próxima!\n")
            break
        else:
            print("Opção inválida! Tente novamente.\n")
menu()
import re

print("====== SISTEMA DE INGRESSOS =======\n")
print("===================================\n")
print("Bem vindo ao nosso espetáculo! Vambora que hoje vai ser muito legal!\n")

# Etapa 0 – NOME (com validação)
while True:
    nome = input("======= Digite o seu nome: ").strip()
    # Regex: ^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$ → aceita letras maiúsculas, minúsculas, acentos e espaços
    if re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", nome):
        break
    else:
        print("❌ Nome inválido. Digite apenas letras (pode incluir espaços).")

print(f"\nQue legal ter você por aqui, {nome}! Desejamos um ótimo espetáculo!\n")
print("===================================\n")

# Etapa 1 – ATRAÇÃO
print("Vamos às atrações da noite!\n")
print("===================================")
print("1- Whindersson Nunes")
print("2- Tiago Ventura")
print("3- Rafael Portugal")
print("4- Afonso Padilha")
print("===================================\n")

while True:
    comediante = input("======= Digite o número da atração: ")
    if comediante == "1":
        comediante_nome = "Whindersson Nunes"
        break
    elif comediante == "2":
        comediante_nome = "Tiago Ventura"
        break
    elif comediante == "3":
        comediante_nome = "Rafael Portugal"
        break
    elif comediante == "4":
        comediante_nome = "Afonso Padilha"
        break
    else:
        print("❌ Opção inválida. Por favor, escolha de 1 a 4.")

# Etapa 2 – INGRESSO
print("\nAgora vamos ao tipo de ingresso!\n")
print("===================================")
print("1- Básico (R$80)")
print("2- Normal (R$100)")
print("3- VIP (R$180)")
print("===================================\n")

while True:
    ingresso = input("======= Digite o tipo de ingresso: ")
    if ingresso == "1":
        ingresso_nome = "Básico"
        preco = 80
        break
    elif ingresso == "2":
        ingresso_nome = "Normal"
        preco = 100
        break
    elif ingresso == "3":
        ingresso_nome = "VIP"
        preco = 180
        break
    else:
        print("❌ Opção inválida. Escolha 1, 2 ou 3.")

# Etapa 3 – PAGAMENTO
print("\nAgora vamos ao pagamento!\n")
print("===================================")
print("1- Dinheiro (5% de desconto)")
print("2- Cartão (8% de juros)")
print("3- Pix (10% de desconto)")
print("===================================\n")

desconto = 0
juros = 0

while True:
    pagamento = input("======= Digite o número do pagamento: ")
    if pagamento == "1":
        pagamento_nome = "Dinheiro"
        desconto = 0.05
        break
    elif pagamento == "2":
        pagamento_nome = "Cartão"
        juros = 0.08
        break
    elif pagamento == "3":
        pagamento_nome = "Pix"
        desconto = 0.10
        break
    else:
        print("❌ Forma de pagamento inválida. Escolha 1, 2 ou 3.")

# CUPOM
print("\nVocê tem um cupom de desconto? Digite ou pressione ENTER para ignorar:")
cupom = input("Cupom: ")

cupom_desconto = 0
if cupom.upper() == "SHOW10":
    cupom_desconto = 0.10
    print("🎉 Cupom válido! 10% de desconto adicional aplicado.")
else:
    print("Nenhum cupom válido aplicado.")

# CÁLCULO FINAL
total = preco
total -= total * desconto
total += total * juros
total -= total * cupom_desconto

print("\nResumo da compra:")
print(f"Nome: {nome}")
print(f"Ingresso: {ingresso_nome} - R${preco:.2f}")
print(f"Atração escolhida: {comediante_nome}")
print(f"Forma de pagamento: {pagamento_nome}")
print(f"Valor final a pagar: R${total:.2f}")

# AVALIAÇÃO
print("\nPor favor, avalie a experiência de compra de 1 a 5:")

while True:
    avaliacao = input("Digite sua nota (1 a 5): ")
    if avaliacao in ["1", "2", "3", "4", "5"]:
        break
    else:
        print("❌ Nota inválida. Digite um número de 1 a 5.")

print(f"\nObrigado pela sua avaliação de {avaliacao} estrela(s)!")
print("Aproveite o espetáculo! ")

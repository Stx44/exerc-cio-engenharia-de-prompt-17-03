# Sistema de Checkout Simples - Versão 1.0

def processar_checkout():
    print("--- Bem-vindo ao Sistema de Checkout ---")

    try:
        # Captura o valor bruto da compra. Usamos float conforme a restrição.
        valor_bruto = float(input("Digite o valor total da compra: "))
        
        # Captura a forma de pagamento e padroniza para letras minúsculas
        forma_pagamento = input("Forma de pagamento (Pix, Boleto, Cartao): ").strip().lower()

        # Inicialização da variável de desconto
        percentual_desconto = 0.0

        # Lógica de decisão para aplicação dos descontos
        if forma_pagamento == "pix":
            percentual_desconto = 0.10  # 10%
        elif forma_pagamento == "boleto":
            percentual_desconto = 0.05  # 5%
        elif forma_pagamento == "cartao" or forma_pagamento == "cartão":
            percentual_desconto = 0.0   # Preço normal
        else:
            # Caso a forma não exista na lista permitida
            print("Erro: Forma de pagamento inválida.")
            return

        # Cálculos matemáticos utilizando o tipo primitivo Float
        valor_desconto = valor_bruto * percentual_desconto
        valor_final = valor_bruto - valor_desconto

        # Mensagem de Acessibilidade Garantida:
        # Padrão: Desconto com X: Valor final | Valor sem desconto
        print(f"\nDesconto com {forma_pagamento.capitalize()}: R$ {valor_final:.2f} | Valor sem o desconto: R$ {valor_bruto:.2f}")
        print(f"Valor com desconto: R$ {valor_final:.2f}")

    except ValueError:
        # Tratamento caso o usuário digite letras no valor da compra
        print("Erro: Por favor, insira um valor numérico válido.")

# Execução do sistema
if __name__ == "__main__":
    processar_checkout()
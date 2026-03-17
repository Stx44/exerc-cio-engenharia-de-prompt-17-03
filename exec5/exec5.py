import re

def validar_cpf(cpf_input: str) -> bool:
    """
    Realiza a validação matemática e lógica de um CPF.
    
    Args:
        cpf_input (str): String contendo o CPF (com ou sem máscara).
        
    Returns:
        bool: True se o CPF for válido, False se falhar nos dígitos ou for sequência.
        
    Raises:
        ValueError: Se contiver letras ou tamanho diferente de 11 dígitos numéricos.
    """
    # 1. Limpeza: Remove pontos e traços
    # Substituímos tudo que não for dígito por string vazia
    cpf_limpo = re.sub(r'\D', '', cpf_input)

    # 2. Verificação de Caracteres Inválidos (Letras no meio dos números)
    # Se a limpeza removeu algo que não era ponto/traço e sobraram letras no original
    # ou se o input original continha letras que o regex não removeu (se usado incorretamente)
    if any(c.isalpha() for c in cpf_input):
        raise ValueError("Erro: O CPF não deve conter letras.")

    # 3. Verificação de Extensão (Falta de caracteres)
    if len(cpf_limpo) != 11:
        raise ValueError(f"Erro: CPF incompleto ou excessivo. Esperado 11 dígitos, recebido {len(cpf_limpo)}.")

    # 4. Regra de Negócio: Bloqueio de sequências repetidas (Ex: 111.111.111-11)
    if cpf_limpo == cpf_limpo[0] * 11:
        return False

    # 5. Cálculo do Primeiro Dígito Verificador (D1)
    # Pesos de 10 a 2 para os primeiros 9 dígitos
    soma_1 = sum(int(cpf_limpo[i]) * (10 - i) for i in range(9))
    resto_1 = (soma_1 * 10) % 11
    d1 = resto_1 if resto_1 < 10 else 0

    if int(cpf_limpo[9]) != d1:
        return False

    # 6. Cálculo do Segundo Dígito Verificador (D2)
    # Pesos de 11 a 2 para os primeiros 10 dígitos (incluindo D1)
    soma_2 = sum(int(cpf_limpo[i]) * (11 - i) for i in range(10))
    resto_2 = (soma_2 * 10) % 11
    d2 = resto_2 if resto_2 < 10 else 0

    if int(cpf_limpo[10]) != d2:
        return False

    return True

# --- Loop de Execução e Testes ---

if __name__ == "__main__":
    print("--- Validador de CPF Ativado ---")
    
    while True:
        entrada = input("\nDigite o CPF para validar (ou 'sair'): ").strip()
        
        if entrada.lower() == 'sair':
            break
            
        # Padrão: Lançar um loop até que o usuário forneça qualquer caracter
        if not entrada:
            print("Entrada vazia detectada. Por favor, digite um valor.")
            continue
            
        try:
            eh_valido = validar_cpf(entrada)
            if eh_valido:
                print(f"Resultado: True (CPF '{entrada}' é válido)")
            else:
                print(f"Resultado: False (CPF '{entrada}' é matematicamente inválido ou sequência proibida)")
                
        except ValueError as e:
            print(f"Ação: {e}")
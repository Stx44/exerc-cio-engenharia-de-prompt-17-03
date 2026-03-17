import re

def validar_cpf(cpf: str) -> bool:
    # 1. Validação de Formato e Caracteres (Regex)
    # Aceita apenas o formato padrão: XXX.XXX.XXX-XX
    padrao_formatado = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
    if not padrao_formatado.match(cpf):
        return False

    # 2. Limpeza para processamento matemático
    numeros = [int(digito) for digito in cpf if digito.isdigit()]

    # 3. Regra de Negócio: Bloqueia sequências de números repetidos
    # (Ex: 111.111.111-11 ou 000.000.000-00)
    if all(n == numeros[0] for n in numeros):
        return False

    # 4. Cálculo do Primeiro Dígito Verificador
    soma = 0
    for i in range(9):
        soma += numeros[i] * (10 - i)
    
    resto = soma % 11
    digito_1 = 0 if resto < 2 else 11 - resto
    
    if numeros[9] != digito_1:
        return False

    # 5. Cálculo do Segundo Dígito Verificador
    soma = 0
    for i in range(10):
        soma += numeros[i] * (11 - i)
    
    resto = soma % 11
    digito_2 = 0 if resto < 2 else 11 - resto

    if numeros[10] != digito_2:
        return False

    return True

# --- Casos de Teste ---
print(validar_cpf("123.456.789-00"))  # False (Cálculo inválido)
print(validar_cpf("111.111.111-11"))  # False (Números repetidos)
print(validar_cpf("000.000.000-00"))  # False (Fraude comum)
print(validar_cpf("529.982.247-25"))  # True  (Válido)
print(validar_cpf("12345678900"))     # False (Formato inválido - falta pontuação)
print(validar_cpf("ABC.DEF.GHI-JK"))  # False (Caracteres não numéricos)
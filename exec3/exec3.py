# ==============================================================================
# SISTEMA DE CONTROLE DE ACESSO - EVENTO
# Versão: 2.0.0 (Refatorada para Python 3.12)
# ==============================================================================

# Informa ao usuário a versão atual do sistema para fins de monitoramento
print("--- Sistema de Controle de Acesso | Versão 2.0.0 ativa ---\n")

# Uso de Constantes: Definição do limite de idade conforme regra de negócio
# Centralizar este valor facilita mudanças futuras na política do evento
MAIORIDADE_MINIMA = 18

def verificar_permissao_entrada(idade_visitante: int) -> str:
    """
    Verifica se o visitante possui a idade mínima necessária para ingressar no evento.

    Args:
        idade_visitante (int): A idade informada pelo indivíduo no check-in.

    Returns:
        str: Mensagem clara indicando o status do acesso (Autorizado ou Bloqueado).
    """
    
    # Passo 1: O sistema recebe o atributo 'idade_visitante' e compara com a constante global
    if idade_visitante >= MAIORIDADE_MINIMA:
        # Passo 2: Se a condição for verdadeira, o método retorna a string de sucesso
        return "Acesso Autorizado: Visitante liberado."
    
    # Passo 3: Caso contrário, retorna a negativa de acesso por idade insuficiente
    else:
        return "Acesso Bloqueado: Idade inferior ao permitido."

# --- Execução do Fluxo Principal ---

# Definimos o valor da idade a ser validada (Exemplo: 20 anos)
idade_para_teste = 10

# Chamada do método de verificação e armazenamento do retorno lógico/textual
resultado_acesso = verificar_permissao_entrada(idade_para_teste)

# Exibição final para o operador do sistema
print(f"Resultado do Processamento: {resultado_acesso}")
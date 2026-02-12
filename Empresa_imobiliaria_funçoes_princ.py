
def calc_quartos (valor_atual, escolhaquarto):
    if escolhaquarto == "S":
        return valor_atual + 250
    return valor_atual

def calc_garagem (valor_atual, escolhagaragem):
    if escolhagaragem == "S":
        return valor_atual + 300
    return valor_atual

def calc_garagem_est (valor_atual, escolhagaragem_est):
    if escolhagaragem_est == "S":
        return valor_atual + 250
    return valor_atual

def calc_vagas (valor_atual, quantidade_vagas):
    if quantidade_vagas > 0:
        return quantidade_vagas * 60 + valor_atual
    return valor_atual

def calc_parcelas (valor_atual, qnt_parcelas):
    if qnt_parcelas > 0:
        return valor_atual / qnt_parcelas
    return valor_atual

def calc_crianca (valor_atual, crianca_inform, valor_desconto):
    if crianca_inform == "N":
        valor_desconto = valor_atual * 0.05
    return valor_atual - valor_desconto

def add_casa (lista, tipo, valor, parcelas, quarto, garagem, vagas):
    novo_imo = {
        "tipo": tipo,
        "valor total": valor,
        "quantidade de parcelas": parcelas,
        "mais quartos": quarto,
        "garagem": garagem,
        "mais vagas": vagas
    }
    lista.append(novo_imo)
    print("Imóvel adicionado.")

def add_apat(lista, tipo, valor, parcelas, crianca, quarto, garagem, vagas):
    novo_imo = {
        "tipo": tipo,
        "valor total": valor,
        "quantidade de parcelas": parcelas,
        "criança": crianca,
        "mais quartos": quarto,
        "garagem": garagem,
        "mais vagas": vagas
    }
    lista.append(novo_imo)
    print("Imóvel adicionado.")

def add_est(lista, tipo, valor, parcelas, quartos, garagem, vagas):
    novo_imo = {
        "tipo": tipo,
        "valor total": valor,
        "quantidade de parcelas": parcelas,
        "mais quartos": quartos,
        "garagem": garagem,
        "mais vagas": vagas
    }
    lista.append(novo_imo)
    print("Imóvel adicionado.")

def show_imo(lista):
    if not lista:
        print('A lista está vazia')
    else:
        print("Lista de imóveis:")
        for i, imovel in enumerate(lista):
            print(f"Id: {i}; Tipo: {imovel['tipo']}; Valor: {imovel['valor total']}; Parcelas: {imovel['quantidade de parcelas']}; +Quartos: {imovel['mais quartos']}; Garagem: {imovel['garagem']}; Vagas: {imovel['mais vagas']}") 

def trash_imo(lista, ind):
    try:
        remove = lista.pop(ind)
        print(f"Imóvel {remove['tipo']} removido.")
    except IndexError:
        print("Esse tal 'id' não existe.")

def menu():
    print()
    print("Escolha uma das opções abaixo:")
    print("Adicionar imóvel (A)")
    print("Ver imóveis (V)")
    print("Remover imóvel (R)")
    print("Sair do sistema (S)")
    print()
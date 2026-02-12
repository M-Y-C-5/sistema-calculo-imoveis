
imoveis = [
    imovelexemplo := {'tipo': 'TESTE',
              'valor total' : 3450,
              'parcelas': 's',
              'quantidade de parcelas': 5,
              'valor das parcelas': 690,
              'mais quartos': 's',
              'garagem' : 's',
              'mais vagas': 'N'
              }
]

escolha_imovel = ''
valor_imovel = 0
valor_imovel_tot = 0
valor_descontado = 0
qnt_vagas = "N"

from Empresa_imobiliaria_funçoes_princ import *

menu()
esc1 = str(input("Digite uma das opções: ").upper())
while esc1 != "S":
    if esc1 == "A":
            escolha_imovel = str(input("Escolha um tipo de imóvel entre [Casa], [Apartamento] ou [Estúdio]: ").upper())

            if escolha_imovel == "CASA":
                print(f"A opção escolhida foi: {escolha_imovel}")
                valor_imovel = 2900
                valor_imovel_tot = 2900

                quartos_imovel = str(input("Desejas mais um quarto: ").upper())
                valor_imovel = calc_quartos(valor_imovel, quartos_imovel)
                valor_imovel_tot = calc_quartos(valor_imovel_tot, quartos_imovel)

                garagem_imovel = str(input("Desejas uma garagem: ").upper())
                valor_imovel = calc_garagem(valor_imovel, garagem_imovel)
                valor_imovel_tot = calc_garagem(valor_imovel_tot, garagem_imovel)

                parcela_imovel = str(input("Desejas parcelar: ").upper())
                if parcela_imovel == "S":
                    parcela_imovel_qnt = int(input("Quantas parcelas MÁXIMO 12: ").upper())
                else:
                    parcela_imovel_qnt = 0
                valor_imovel = calc_parcelas(valor_imovel, parcela_imovel_qnt)

            elif escolha_imovel == "APARTAMENTO":
                print(f"A opção escolhida foi: {escolha_imovel}")
                valor_imovel = 2750
                valor_imovel_tot = 2750

                quartos_imovel = str(input("Desejas mais um quarto: ").upper())

                valor_imovel = calc_quartos(valor_imovel, quartos_imovel)
                valor_imovel_tot = calc_quartos(valor_imovel_tot, quartos_imovel)

                garagem_imovel = str(input("Desejas uma garagem: ").upper())

                valor_imovel = calc_garagem(valor_imovel, garagem_imovel)
                valor_imovel_tot = calc_garagem(valor_imovel_tot, garagem_imovel)

                inform_criancas = str(input("Você possuí crianças: "))

                valor_imovel = calc_crianca(valor_imovel, inform_criancas, valor_descontado)
                valor_imovel_tot = calc_crianca(valor_imovel_tot, inform_criancas, valor_descontado)

                parcela_imovel = str(input("Desejas parcelar: ").upper())
                if parcela_imovel == "S":
                    parcela_imovel_qnt = int(input("Quantas parcelas MÁXIMO 12: "))
                else:
                    parcela_imovel_qnt = 0
                    valor_imovel = calc_parcelas(valor_imovel, parcela_imovel_qnt)

            elif escolha_imovel == "ESTÚDIO":
                quartos_imovel = "N"
                qnt_vagas = 0

                print(f"A opção escolhida foi: {escolha_imovel}")
                valor_imovel = 3200
                valor_imovel_tot = 3200

                garagem_imovel_est = str(input("Desejas uma garagem: ").upper())
                valor_imovel = calc_garagem_est(valor_imovel, garagem_imovel_est)
                valor_imovel_tot = calc_garagem_est(valor_imovel_tot, garagem_imovel_est)
        
                if garagem_imovel_est == "S":
                    mais_garagens = str(input("Você deseja mais garagens em seu imóvel: ").upper())
            
                    if mais_garagens == "S":
                        qnt_vagas = int(input("Quantas vagas a mais: "))
                        valor_imovel = calc_vagas(valor_imovel, qnt_vagas)
                        valor_imovel_tot = calc_vagas(valor_imovel_tot, qnt_vagas)
                else:
                    qnt_vagas = 0

                parcela_imovel = str(input("Desejas parcelar: ").upper())
                if parcela_imovel == "S":
                    parcela_imovel_qnt = int(input("Quantas parcelas MÁXIMO 12: "))
                else:
                    parcela_imovel_qnt = 0

                valor_imovel = calc_parcelas(valor_imovel, parcela_imovel_qnt)

                add_imoest = add_est(imoveis, escolha_imovel, valor_imovel_tot, parcela_imovel_qnt, quartos_imovel, garagem_imovel_est, qnt_vagas)


            if escolha_imovel == "CASA":
                add_imoc = add_casa(imoveis, escolha_imovel, valor_imovel_tot, parcela_imovel_qnt, quartos_imovel, garagem_imovel, qnt_vagas)
            elif escolha_imovel == "APARTAMENTO":
                add_imoa = add_apat(imoveis, escolha_imovel, valor_imovel_tot, parcela_imovel_qnt, inform_criancas, quartos_imovel, garagem_imovel, qnt_vagas)

    elif esc1 == "V":
        show_imovel = show_imo(imoveis)
    elif esc1 == "R":
        id_imovel = int(input('Ponha o Index (ID) do imóvel a ser excluído: '))
        trash_imovel = trash_imo(imoveis, id_imovel)
    else:
        print("Opção inválida.")
    print()
    menu()
    esc1 = str(input("Escolha uma das opções: ").upper())

print()
print("Obrigado por ter usado o sistema...")
print()
def voto(B):
    from datetime import date
    HOJE = date.today().year
    AGE = HOJE - B
    if B > HOJE - 16:
        return f'{AGE} Anos de idade: Não vota ainda...'
    if B < HOJE -  65:
        return f'{AGE} Anos de idade: Voto Opcional.'
    if B < HOJE - 18:
        return f'{AGE} Anos de idade: Voto obrigatório!'


IDADE = int(input('Em que ano você nasceu? '))
print(voto(IDADE))

'''
Operador ternário em Python
'''
logged_user = True

#if logged_user:
#    msg = 'Usúario logad.'
#else:
#    msg = 'Usúario precisa logar'
msg = 'Usúario logad.' if logged_user else 'Usuário precisa logar' # operador ternário

print(msg)
idade = 16
print(f'Pode acessar') if idade >= 18 else print(f'Acesso negado')
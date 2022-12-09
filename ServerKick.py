import os

def print_menu():
    print('1. Vypsat seznam uživatelů přihlášených na server')
    print('2. Odpojit uživatele ze serveru')
    print('3. Ukončit skript')
    print()

def get_users():
    users = os.popen('who').read().strip().split('\n')

    print('Seznam přihlášených uživatelů:')
    for user in users:
        print(f'- {user}')
    print()

def disconnect_user():
    users = os.popen('who').read().strip().split('\n')

    print('Seznam přihlášených uživatelů:')
    for i, user in enumerate(users):
        print(f'{i+1}. {user}')

    user_index = int(input('Zadejte číslo uživatele, kterého chcete odpojit: '))

    user_id = os.popen(f'who | grep "{users[user_index-1]}" | awk {{\'print $2\'}}').read().strip()

    os.system(f'kill {user_id}')

while True:
    print_menu()

    choice = input('Zadejte číslo volby: ')
    print()

    if choice == '1':
        get_users()
    elif choice == '2':
        disconnect_user()
    elif choice == '3':
        break
    else:
        print('Neplatná volba')
        print()

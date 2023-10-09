from Blog import show_menu, add_post, add_user, query_users_posts

while True:
    show_menu()
    choice = input('Selecione uma opção\n')
    
    if choice == "1":
        add_user()
    elif choice == "2":
        add_post()
    elif choice == "3":
        query_users_posts()
    elif choice == "4":
        break
    else:
        print("Opção inválida")

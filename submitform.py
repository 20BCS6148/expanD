import database_form
MENU_PROMT   =""" 
1) Add a new bean.
2) see all beans.
3) Find  abean by name.
4) See which preparation method is used for bean.
5) Exit

Your Selection : 
"""
def menu():
    connection = database_form.connect()
    #database.create_table(connection)

    while(user_input:=input(MENU_PROMT))!="5":
        if user_input=="1":
                Name = input("Enter Bean name :")
                method = input("How you have prepared it: ")
                rating = int(input("Enter rating :"))
                database_form.add_bean(connection,Name,method,rating)
        elif user_input=="2":
            beans = database_form.get_all_beans(connection)
            for bean in beans:
                print(bean)
        elif user_input=="3":
            Name = input("Enter the Bean name : ")
            beans=database_form.get_beans_by_name(connection,Name)
            for bean in beans:
                print(bean)
        elif user_input =="4":
            Name= input("Enter bean name : ")
            bean = database_form.get_best_prep_for_bean(connection,Name)
            print(bean)
        else:
            print("Invalid input !! ")    

menu()


    
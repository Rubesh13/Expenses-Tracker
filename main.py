#geting input file
from db import(
adding_user,
adding_expense,
update_amount,
viewing_expense,
expenses_summary,
export_csv
)


while True:
    print()
    print("=====Expenses Tracker=====")
    print()
    print("1.Add User")
    print("2.Add Expenses")
    print("3.Update expenses")
    print("4.View Summary")
    print("5.Expenses Summary")
    print("6.Export CSV File")
    print("7.EXIT")
    try:
        get_data=int(input("Enter your choice: "))
    except ValurError:
        print("Enter a valid number")
        continue
        
    
    if get_data==1:#adding new user
        adding_user()
        
    elif get_data==2:#adding new expense data
        adding_expense()
        
    elif get_data==3:#updating the expenses
        update_amount()
        
    elif get_data==4:#viewing summary
        viewing_expense()

    elif get_data==5:
        expenses_summary()#showing monthly summary
        
    elif get_data==6:
        export_csv()

    elif get_data==7:
        break

    else:
        print()
        print("Invalid Option")


    
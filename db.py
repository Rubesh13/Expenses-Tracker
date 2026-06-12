import mysql.connector as sq
import csv
import sys

con=None
cur=None

test_password=input("Enter DB password: ")
try:
    test_con=con=sq.connect(
        host="localhost",
        user="root",
        password=test_password,
        database="expenses_tracker"
    )
    test_con.close()
except sq.Error as e:
    print("Database connection is failed,the entered database password is wronng")
    print(e)
    sys.exit()
finally:
    if cur:
        cur.close()
    if con:
        con.close()

def get_connection():
    try:
        con=sq.connect(
            host="localhost",
            user="root",
            password=test_password,
            database="expenses_tracker"
        )
        return con
    except sq.Error as e:
        print(e)
        return None

def adding_user():
    try:
        con=get_connection()
        cur=con.cursor()

        user_id=int(input("User ID: "))
        user_name=input("User Name: ")
        email=input("Email: ")
        created_date=input("Date: ")

        cur.execute("""
        INSERT INTO users(user_id,user_name,email,created_date)
        VALUES(%s,%s,%s,%s)
        """,(user_id,user_name,email,created_date))

        con.commit()
        print("New User Added Successfully!!!")

    except sq.Error as e:
        print(e)

    finally:
        cur.close()
        con.close()

def adding_expense():
    try:
        con=get_connection()
        cur=con.cursor()

        expenses_id=int(input("Expenses ID: "))
        user_id=int(input("User ID: "))
        category_name=input("Category Name: ")
        amount=int(input("Amount: "))
        payment_method=input("Payment Method: ").upper()

        cur.execute(
            "SELECT category_name FROM category WHERE category_name=%s",
            (category_name,)
        )

        result=cur.fetchone()

        if result is None:
            cur.execute("SELECT MAX(category_id) FROM category")
            maxid=cur.fetchone()[0] or 0

            cur.execute("""
            INSERT INTO category(category_id,category_name)
            VALUES(%s,%s)
            """,(maxid+1,category_name))

        cur.execute("""
        INSERT INTO expenses
        (expenses_id,user_id,category_name,amount,payment_method)
        VALUES(%s,%s,%s,%s,%s)
        """,(expenses_id,user_id,category_name,amount,payment_method))

        con.commit()
        print("Expense Added Successfully!!!")

    except sq.Error as e:
        print(e)

    finally:
        cur.close()
        con.close()

def update_amount():
    try:
        con=get_connection()
        cur=con.cursor()

        expenseid=int(input("Expense ID: "))
        new_amount=int(input("New Amount: "))

        cur.execute("""
        UPDATE expenses
        SET amount=%s
        WHERE expenses_id=%s
        """,(new_amount,expenseid))

        con.commit()
        print("Amount Updated Successfully!!!")

    except sq.Error as e:
        print(e)

    finally:
        cur.close()
        con.close()

def viewing_expense():
    try:
        con=get_connection()
        cur=con.cursor()

        cur.execute("SELECT * FROM expenses")

        print("\nExpenses:")
        for row in cur.fetchall():
            print(row)

        cur.execute("SELECT SUM(amount) FROM expenses")
        total=cur.fetchone()[0] or 0

        print("Total Expenses =",total)

    except sq.Error as e:
        print(e)

    finally:
        cur.close()
        con.close()

def expenses_summary():
    try:
        con=get_connection()
        cur=con.cursor()

        cur.execute("""
        SELECT category_name,SUM(amount)
        FROM expenses
        GROUP BY category_name
        """)

        print("\nSummary:")
        for category,amount in cur.fetchall():
            print(category,":",amount)

    except sq.Error as e:
        print(e)

    finally:
        cur.close()
        con.close()

def export_csv():
    try:
        con=get_connection()
        cur=con.cursor()

        cur.execute("SELECT * FROM expenses")
        rows=cur.fetchall()

        with open("expenses.csv","w",newline="") as file:
            writer=csv.writer(file)

            writer.writerow([
                "expenses_id",
                "user_id",
                "category_name",
                "amount",
                "payment_method"
            ])

            writer.writerows(rows)

        print("CSV Exported Successfully!!!")

    except sq.Error as e:
        print(e)

    finally:
        cur.close()
        con.close()


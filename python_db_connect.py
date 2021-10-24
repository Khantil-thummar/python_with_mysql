import mysql.connector as cnt

db = cnt.connect(
    host="localhost",
    user="root",
    passwd="root123",
    database="student"
)


mycursour = db.cursor()

# mycursour.execute("CREATE TABLE Student (s_id int primary key auto_increment, name VARCHAR(255), En_Number INT, Address VARCHAR(100))")
# mycursour.execute("describe Student")



def show_data():
    sql = "select * from student"
    mycursour.execute(sql)
    for i in mycursour:
        print(i)

def insert_data():
    name = (input("Enter Your Name:"))
    en_number = int(input("Enter Your Enrollment Number:"))
    address = (input("Enter Your City Name:"))
    val = (name, en_number, address)
    sql = "insert into Student (name, En_Number, Address) values (%s, %s, %s)"
    mycursour.execute(sql, val)
    print("Record Inserted Successfully.....")
    db.commit()
    return name, en_number, address

def update_data():
    print("Select Id Number For Changing Data...\n")
    show_data()
    id_numbr = int(input("Enter Id_Nmuber:"))
    name = (input("Enter Your Name:"))
    en_number = int(input("Enter Your Enrollment Number:"))
    address = (input("Enter Your City Name:"))

    val = (name, en_number, address, id_numbr)
    sql = "UPDATE student SET name = %s, En_Number = %s, Address = %s WHERE s_id = %s"
    mycursour.execute(sql, val)
    print("Your Data is Updated....")
    db.commit()
    show_data()



def delete_data():
    print("Selecting Row By Its Id_Nmuber:")
    show_data()
    id_numbr = int(input("Enter Id_Nmuber:"))
    sql = "delete from student where s_id = %s"
    val = (id_numbr, )
    mycursour.execute(sql, val)
    db.commit()
    print("Deleted Data Successfully.....")
    show_data()


def show_limited_data():

    name = input("Enter Name For Displaying Data:")
    sql = "select * from student where name = %s"
    val = (name, )
    mycursour.execute(sql, val)
    for x in mycursour:
        print(x)





def main():
    while True:
        print("-------------------------------")
        print("1. Insert Data\n"
              "2. Display All Data\n"
              "3. Display Data By Name\n"
              "4. Update Data\n"
              "5. Delete Data\n"
              "6. Exit")
        choise = int(input("Select Operation:"))
        if choise == 1:
            insert_data()
        elif choise == 2:
            show_data()
        elif choise == 3:
            show_limited_data()
        elif choise == 4:
            update_data()
        elif choise == 5:
            delete_data()
        elif choise == 6:
            print("Closing Operations....")
            break

if __name__ == "__main__":
    main()

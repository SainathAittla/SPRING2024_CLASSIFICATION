import pandas as pd
import sqlite3
from sqlite3 import Error

conn_orders = sqlite3.connect("orders.db")
cur = conn_orders.cursor()

# sql_statement = "select * from customers;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from orders;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from vendors;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from products;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from orderitems;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from productnotes;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)


def ex1():
    # Write an SQL statement that SELECTs all rows from the `customers` table
    # output columns: cust_name, cust_email

    ### BEGIN SOLUTION
    sql_statement = "SELECT cust_name, cust_email From customers;"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df.head(5))
    return sql_statement


def ex2():
    # Write an SQL statement that SELECTs all rows from the `products` table
    # output columns: vend_id

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id From products;"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement


def ex3():
    # Write an SQL statement that SELECTs distinct rows for vend_id from the `products` table
    # output columns: vend_id

    ### BEGIN SOLUTION
    sql_statement = "SELECT distinct vend_id From products;"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement


def ex4():
    # Write an SQL statement that SELECTs the first five rows from the `products` table
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name From products LIMIT 5;"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement


def ex5():
    # Write an SQL statement that SELECTs 4 rows starting from row 3 from `products` table
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name FROM products LIMIT 3,4;"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement



def ex6():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_name
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name From products order by prod_name;"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement


def ex7():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_price and then prod_name 
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name From products order by prod_price, prod_name;"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)   
    return sql_statement


def ex8():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_price (descending order)
    # and then prod_name 
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products ORDER BY prod_price DESC, prod_name"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement


def ex9():
    # Write an SQL statement that SELECTs all rows from `products` table where the price of product is 2.50
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name From products where prod_price is 2.50;"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex10():
    # Write an SQL statement that SELECTs all rows from `products` table where the name of product is Oil can
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products where prod_name LIKE 'Oil can%';"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement


def ex11():
    # Write an SQL statement that SELECTs all rows from `products` table where the price of product is 
    # less than or equal to 10
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products where prod_price <= 10;" 
    ## END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement



def ex12():
    # Write an SQL statement that SELECTs all rows from `products` table where the vendor id is not equal to 1003
    # output columns: vend_id, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_name FROM products where vend_id != 1003;"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex13():
    # Write an SQL statement that SELECTs all rows from `products` table where the product prices are between 5 and 10
    # output columns: prod_name, prod_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name, prod_price FROM products where prod_price BETWEEN 5 and 10;"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement


def ex14():
    # Write an SQL statement that SELECTs all rows from the `customers` table where the customer email is empty
    # output columns: cust_id, cust_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT cust_id, cust_name FROM customers where cust_email IS NULL"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex15():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1003 and
    # the price is less than or equal to 10. 
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name FROM products where vend_id IS 1003 and prod_price <= 10"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex16():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1002 or 1003 and
    # the price is greater than or equal to 5. 
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name FROM products where vend_id >= 1002 and vend_id <= 1003 and prod_price >=5"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex17():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1002 or 1003 or 1005.
    # Use the IN operator for this!
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name FROM products where vend_id >= 1002"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement


def ex18():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is NOT 1002 or 1003.
    # Use the NOT IN operator for this!
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name FROM products where vend_id != 1002 and vend_id != 1003"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex19():
    # Write an SQL statement that SELECTs all rows from the `products` table where the product name starts with 'jet'
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products where prod_name LIKE 'Jet%'"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex20():
    # Write an SQL statement that SELECTs all rows from the `products` table where the product name ends with 'anvil'
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products where prod_name LIKE '%anvil'"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex21():
    # Write an SQL statement that SELECTs all rows from the `vendors` table. Concatenate vendor name and vendor country
    # as vend_title. Order by vend_title. Leave space in between -- example `ACME (USA)`
    # output columns: vend_title

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_name || ' ' || '(' || vend_country || ')' AS vend_title FROM vendors ORDER BY vend_name"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement


def ex22():
    # Write an SQL statement that SELECTs all rows from the `orderitems` table where order number is 20005. 
    # Display an extra calculated column called `expanded_price` that is the result of quantity multiplied by item_price.
    # Round the value to two decimal places. 
    # output columns: prod_id, quantity, item_price, expanded_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, quantity, item_price, ROUND((quantity * item_price),2) AS expanded_price FROM orderitems WHERE order_num = 20005;"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex23():
    # Write an SQL statement that SELECTs all rows from the `orders` table where the order date is between 
    # 2005-09-13 and 2005-10-04
    # output columns: order_num, order_date
    # https://www.sqlitetutorial.net/sqlite-date-functions/sqlite-date-function/
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT order_num, order_date FROM orders WHERE order_date between '2005-09-13' and '2005-10-04'"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex24():
    # Write an SQL statement that calculates the average price of all rows in the `products` table. 
    # Call the average column avg_price
    # output columns: avg_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT AVG(prod_price) as avg_price FROM products"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex25():
    # Write an SQL statement that calculates the average price of all rows in the `products` table 
    # where the vendor id is 1003 . Call the average column avg_price
    # output columns: avg_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT AVG(prod_price) as avg_price FROM products WHERE vend_id = 1003 "
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement



def ex26():
    # Write an SQL statement that counts the number of customers in the `customers` table 
    # Call the count column num_cust
    # output columns: num_cust

    ### BEGIN SOLUTION
    sql_statement = "SELECT COUNT(*) as num_cust FROM customers"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex27():
    # Write an SQL statement that calculates the max price in the `products` table 
    # Call the max column max_price. Round the value to two decimal places. 
    # output columns: max_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT MAX(prod_price) as max_price FROM products"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex28():
    # Write an SQL statement that calculates the min price in the `products` table 
    # Call the min column min_price. Round the value to two decimal places. 
    # output columns: min_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT MIN(prod_price) as min_price FROM products"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement

def ex29():
    # Write an SQL statement that sums the quantity in the `orderitems` table where order number is 20005. 
    # Call the sum column items_ordered
    # output columns: items_ordered

    ### BEGIN SOLUTION
    sql_statement = "SELECT SUM(quantity) as items_ordered FROM orderitems WHERE order_num = 20005"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn_orders)
    print(df)
    return sql_statement


#---------------------------------------------------------------------------------------------------------------------------------------------#

# You cannot use Pandas! I will deduct points after manual check if you use Pandas. You CANNOT use the 'csv' module to read the file

# Hint: Ensure to strip all strings so there is no space in them

# DO NOT use StudentID from the non_normalized table. Let the normalized table automatically handle StudentID. 


def create_connection(db_file, delete_db=False):
    import os
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def execute_sql_statement(sql_statement, conn):
    cur = conn.cursor()
    cur.execute(sql_statement)

    rows = cur.fetchall()

    return rows

conn_non_normalized = create_connection('non_normalized.db')
sql_statement = "select * from Students;"
df = pd.read_sql_query(sql_statement, conn_non_normalized)
# print(df)

def normalize_database(non_normalized_db_filename):
    #     Normalize 'non_normalized.db'
    #     Call the normalized database 'normalized.db'
    #     Function Output: No outputs
    #     Requirements:
    #     Create four tables
    #     Degrees table has one column:
    #         [Degree] column is the primary key

    #     Exams table has two columns:
    #         [Exam] column is the primary key column
    #         [Year] column stores the exam year

    #     Students table has four columns:
    #         [StudentID] primary key column
    #         [First_Name] stores first name
    #         [Last_Name] stores last name
    #         [Degree] foreign key to Degrees table

    #     StudentExamScores table has four columns:
    #         [PK] primary key column,
    #         [StudentID] foreign key to Students table,
    #         [Exam] foreign key to Exams table ,
    #         [Score] exam score

    ### BEGIN SOLUTION
    conn_normalized = create_connection('normalized.db')
    sql_statement = """CREATE TABLE Degrees (
    Degree varchar(255) NOT NULL,
    PRIMARY KEY (Degree) );"""
    create_table(conn_normalized,sql_statement)
    sql_statement = """CREATE TABLE Exams (
    Exam varchar(255) NOT NULL,
    Year int NOT NULL,
    PRIMARY KEY (Exam) );"""
    create_table(conn_normalized,sql_statement)
    sql_statement = """CREATE TABLE Students (
    StudentID int NOT NULL,
    First_Name varchar(255) NOT NULL,
    Last_Name varchar(255) NOT NULL,
    Degree varchar(255) NOT NULL,
    PRIMARY KEY (StudentId),
    FOREIGN KEY (Degree) REFERENCES Degrees(Degree) );"""
    create_table(conn_normalized,sql_statement)
    sql_statement = """CREATE TABLE StudentExamScores (
    PK int NOT NULL,
    StudentId int NOT NULL,
    Exam varchar(255) NOT NULL,
    Score float,
    PRIMARY KEY (PK),
    FOREIGN KEY (StudentId) REFERENCES Students(StudentId),
    FOREIGN KEY (Exam) REFERENCES Exams(Exam) );"""
    create_table(conn_normalized,sql_statement)
    sql_statement = """
    insert into Exams (Exam , Year) values ('exam1',2016);
    """
    execute_sql_statement(sql_statement,conn_normalized)
    sql_statement = """
    insert into Exams (Exam , Year) values ('exam2',2017);
    """
    execute_sql_statement(sql_statement,conn_normalized)
    sql_statement = """
        insert into Exams (Exam , Year) values ('exam6',2017);
        """
    execute_sql_statement(sql_statement, conn_normalized)
    sql_statement = """
        insert into Exams (Exam , Year) values ('exam7',2017);
        """
    execute_sql_statement(sql_statement, conn_normalized)
    sql_statement = """
        insert into Exams (Exam , Year) values ('exam3',2018);
        """
    execute_sql_statement(sql_statement, conn_normalized)
    sql_statement = """
        insert into Exams (Exam , Year) values ('exam8',2018);
        """
    execute_sql_statement(sql_statement, conn_normalized)
    sql_statement = """
        insert into Exams (Exam , Year) values ('exam9',2018);
        """
    execute_sql_statement(sql_statement, conn_normalized)
    sql_statement = """
        insert into Exams (Exam , Year) values ('exam10',2019);
        """
    execute_sql_statement(sql_statement, conn_normalized)
    sql_statement = """
        insert into Exams (Exam , Year) values ('exam4',2019);
        """
    execute_sql_statement(sql_statement, conn_normalized)
    sql_statement = """
        insert into Exams (Exam , Year) values ('exam5',2020);
        """
    execute_sql_statement(sql_statement, conn_normalized)

    sql_statement = """
            insert into Degrees (Degree) values ('graduate');
            """
    execute_sql_statement(sql_statement, conn_normalized)

    sql_statement = """
                insert into Degrees (Degree) values ('undergraduate');
                """
    execute_sql_statement(sql_statement, conn_normalized)

    sql_statement = """
                    insert into Students (StudentId,First_Name,Last_Name,Degree) 
                    values (1,'Andrew','Halt','graduate');
                    """
    execute_sql_statement(sql_statement, conn_normalized)
    sql_statement = """
                        insert into Students (StudentId,First_Name,Last_Name,Degree) 
                        values (2,'Mathew','Perry','graduate');
                        """
    execute_sql_statement(sql_statement, conn_normalized)

    sql_statement = """
                        insert into Students (StudentId,First_Name,Last_Name,Degree) 
                        values (3,'Jeoy','Tribianni','graduate');
                        """
    execute_sql_statement(sql_statement, conn_normalized)

    sql_statement = """
                        insert into Students (StudentId,First_Name,Last_Name,Degree) 
                        values (4,'Rachel','Green','undergraduate');
                        """
    execute_sql_statement(sql_statement, conn_normalized)

    sql_statement = """
                            insert into Students (StudentId,First_Name,Last_Name,Degree) 
                            values (5,'Monica','Geller','undergraduate');
                            """
    execute_sql_statement(sql_statement, conn_normalized)

    sql_statement = """
                            insert into Students (StudentId,First_Name,Last_Name,Degree) 
                            values (6,'Ross','Geller','graduate');
                            """
    execute_sql_statement(sql_statement, conn_normalized)

    sql_statement = """
                            insert into StudentExamScores (PK,StudentId,Exam,Score) 
                            values (1,1,'exam1',20.00);
                            """
    execute_sql_statement(sql_statement, conn_normalized)

    sql_statement = """
                                insert into StudentExamScores (PK,StudentId,Exam,Score) 
                                values (2,2,'exam2',80.00);
                                """
    execute_sql_statement(sql_statement, conn_normalized)

    sql_statement = """
                                insert into StudentExamScores (PK,StudentId,Exam,Score) 
                                values (3,3,'exam3',40.00);
                                """
    execute_sql_statement(sql_statement, conn_normalized)

    sql_statement = """
                                insert into StudentExamScores (PK,StudentId,Exam,Score) 
                                values (4,4,'exam4',60.00);
                                """
    execute_sql_statement(sql_statement, conn_normalized)
    conn_normalized.commit()


### END SOLUTION
        

def ex30(conn):
    # Write an SQL statement that SELECTs all rows from the `Exams` table and sort the exams by Year
    # output columns: exam, year
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT Exam,Year FROM Exams order by Year;"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    print(df)
    return sql_statement


def ex31(conn):
    # Write an SQL statement that SELECTs all rows from the `Degrees` table and sort the degrees by name
    # output columns: degree
    
    ### BEGIN SOLUTION
    sql_statement = "select Degree from Degrees order by Degree;"
    ## END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    print(df)
    return sql_statement


def ex32(conn):
    # Write an SQL statement that counts the numbers of gradate and undergraduate students
    # output columns: degree, count_degree
    
    ### BEGIN SOLUTION
    sql_statement = "Select S.Degree, Count(SS.StudentId) as count_degree from Students S join StudentExamScores as SS on S.StudentId = SS.StudentId Group By S.Degree;"
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    print(df)
    return sql_statement


def ex33(conn):
    # Write an SQL statement that calculates the exam averages for exams; sort by average in descending order.
    # output columns: exam, year, average
    # round to two decimal places
    
    
    ### BEGIN SOLUTION
    sql_statement = """select se.Exam , e.year , round(avg(se.Score),2) as average 
                       from StudentExamScores se 
                       join Exams e
                       on se.Exam = e.Exam
                       order by average desc"""
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    print(df)
    return sql_statement


def ex34(conn):
    # Write an SQL statement that calculates the exam averages for degrees; sort by average in descending order.
    # output columns: degree, average 
    # round to two decimal places
    
    ### BEGIN SOLUTION
    sql_statement = """select s.Degree , round(avg(se.Score),2) as average 
                       from StudentExamScores se 
                       join Students s
                       on se.StudentId = s.StudentId
                       order by average desc"""
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    print(df)
    return sql_statement

def ex35(conn):
    # Write an SQL statement that calculates the exam averages for students; sort by average in descending order. Show only top 10 students
    # output columns: first_name, last_name, degree, average
    # round to two decimal places
    # Order by average in descending order
    # Warning two of the students have the same average!!!
    
    ### BEGIN SOLUTION
    sql_statement = """select s.First_Name , s.Last_Name , s.Degree , round(avg(se.Score),2) as average 
                       from StudentExamScores se 
                       join Students s
                       on se.StudentId = s.StudentId
                       order by average desc
                       limit 10"""
    ### END SOLUTION 
    df = pd.read_sql_query(sql_statement, conn)
    print(df)
    return sql_statement


if __name__ == '__main__':
    conn_orders = sqlite3.connect("orders.db")
    cur = conn_orders.cursor()
    ex1(conn_orders=conn_orders)
    ex2(conn_orders=conn_orders)
    ex3(conn_orders=conn_orders)
    ex4(conn_orders=conn_orders)
    ex5(conn_orders=conn_orders)
    ex6(conn_orders=conn_orders)
    ex7(conn_orders=conn_orders)
    ex8(conn_orders=conn_orders)
    ex9(conn_orders=conn_orders)
    ex10(conn_orders=conn_orders)
    ex12(conn_orders=conn_orders)
    ex13(conn_orders=conn_orders)
    ex14(conn_orders=conn_orders)
    ex15(conn_orders=conn_orders)
    ex16(conn_orders=conn_orders)
    ex17(conn_orders=conn_orders)
    ex18(conn_orders=conn_orders)
    ex19(conn_orders=conn_orders)
    ex20(conn_orders=conn_orders)
    ex21(conn_orders=conn_orders)
    ex22(conn_orders=conn_orders)
    ex23(conn_orders=conn_orders)
    ex24(conn_orders=conn_orders)
    ex25(conn_orders=conn_orders)
    ex26(conn_orders=conn_orders)
    ex27(conn_orders=conn_orders)
    ex28(conn_orders=conn_orders)
    ex29(conn_orders=conn_orders)
    


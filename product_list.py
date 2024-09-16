import sqlite3

conn = sqlite3.connect('products.db')
cur = conn.cursor()
user=0
# cur.execute('CREATE TABLE products (id int primary key, product_name text, product_price int);')
while user !=4:
    user = int(input('\nproduct manager \n'
          '---------------\n'
          '1-Enter a product\n'
          '2-list all products\n'
          '3-Search product\n'
          '4-Exit\n'
          '\n'
          'Enter your Choice: \n'))


    if user == 1 :
        a = int(input('Enter product id: '))
        b = (input ('Enter product name: '))
        c = int(input('Enter product price: '))
        cur.execute('insert into products values(?, ?, ?)',(a,b,c))
        conn.commit()

    elif user == 2 :
        for product in cur.execute('select * from products'):
            print(product)

    elif user == 3:
        s_product = input('Enter product Name: ')
        for product in cur.execute('select * from products where product_name like ?',(s_product, )):
            print(product)

else :
    conn.commit()
    conn.close()









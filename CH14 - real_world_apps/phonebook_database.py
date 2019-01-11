import sqlite3
import json

person_data_list = json.loads(open('./person_data.json').read())
business_data_list = json.loads(open('./business.json').read())


conn = sqlite3.connect('phonebook_project.db')
c = conn.cursor()

def create_business_table():
   """
       creates a table containing business data.
   """
   c.execute('CREATE TABLE IF NOT EXISTS business(business_name TEXT, address_line_1 TEXT, address_line_2 TEXT, address_line_3 TEXT, postcode TEXT, country TEXT, telephone_number TEXT, business_category TEXT)')
   conn.commit()


def create_person_table():
   """
       creates a table containing person data.
   """
   c.execute('CREATE TABLE IF NOT EXISTS person(first_name TEXT, last_name TEXT, address_line_1 TEXT, address_line_2 TEXT, address_line_3 TEXT, postcode TEXT, country TEXT, telephone_number TEXT)')
   conn.commit()


def dynamic_person_data_entry():
    for item in person_data_list:
        first_name = item["first_name"]
        last_name = item["last_name"]
        address_line_1 = item["address_line_1"]
        address_line_2 = item["address_line_2"]
        address_line_3 = item["address_line_3"]
        postcode = item["postcode"]
        country = item["country"]
        telephone_number = item["telephone_number"]
        c.execute('INSERT INTO person(first_name,last_name,address_line_1,address_line_2,address_line_3,postcode,country,telephone_number) VALUES(?,?,?,?,?,?,?,?)',(first_name,last_name,address_line_1,address_line_2,address_line_3,postcode,country,telephone_number))
        conn.commit()

def dynamic_business_data_entry():
    for item in business_data_list:
        business_name = item["business name"]
        address_line_1 = item["address_line_1"]
        address_line_2 = item["address_line_2"]
        address_line_3 = item["address_line_3"]
        postcode = item["postcode"]
        country = item["country"]
        telephone_number = item["telephone_number"]
        business_category = item["business_category"]
        c.execute('INSERT INTO business(business_name, address_line_1,address_line_2,address_line_3,postcode,country,telephone_number, business_category) VALUES(?,?,?,?,?,?,?,?)',(business_name,address_line_1,address_line_2,address_line_3,postcode,country,telephone_number, business_category))
        conn.commit()
      
create_business_table()
create_person_table()
dynamic_person_data_entry()
dynamic_business_data_entry()




def retrieve_business_cat():
#    business_cat_search = input("what business type are you looking for?    ")
    shop_list = []
    c.execute(('SELECT * FROM business WHERE business_category = "Toys"'))
    for row in c.fetchall():
        shop_list.append(row[0])
    return shop_list
    

print(retrieve_business_cat())
    

















import sqlite3
import json
import requests

person_data_list = json.loads(open('./person_data.json').read())
business_data_list = json.loads(open('./business.json').read())



conn = sqlite3.connect('phonebook_project.db')
c= conn.cursor()

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
   
def create_postcode_table():
   """
       creates a table containing person data.
   """
   c.execute('CREATE TABLE IF NOT EXISTS coordinates(postcode TEXT, longitude INT, latitude INT)')
   conn.commit()




def dynamic_coordinates_data_entry():
     postcode_list = []
     for item in person_data_list:
         postcode_list.append(item["postcode"])
     
     for item in business_data_list:
         postcode_list.append(item["postcode"])


     unique_postcode_list = set(postcode_list)

     endpoint = "https://api.postcodes.io/postcodes/"
     coor_dict = []
     for item in unique_postcode_list:
        payload = item
        postcode_response = requests.get(endpoint + payload)
        data_postcode = postcode_response.json()
        print(data_postcode["status"])
        if data_postcode["status"] == 200:
            longitude_val = data_postcode['result']['longitude']
            latitude_val = data_postcode['result']['latitude']
            print(longitude_val, latitude_val)
            dic_1 = {"postcode": payload, "longitude": longitude_val, "latitude": latitude_val} 
            coor_dict.append(dic_1)
        else:
            print(payload)
        
     
     for item in coor_dict:
        postcode = item["postcode"]
        longitude = item["longitude"]
        latitude = item["latitude"]
        c.execute('INSERT INTO coordinates(postcode, longitude, latitude ) VALUES(?, ?, ?)',(postcode, longitude, latitude,))
        conn.commit()
      

def dynamic_person_data_entry():
    for item in person_data_list:
        first_name = item["first_name"]
        last_name = item["last_name"]
        address_line_1 = item["address_line_1"]
        address_line_2 = item["address_line_2"]
        address_line_3 = item["address_line_3"]
        postcode_with_space = item["postcode"]
        country = item["country"]
        telephone_number = item["telephone_number"]
        c.execute('INSERT INTO person(first_name,last_name,address_line_1,address_line_2,address_line_3,postcode,country,telephone_number) VALUES(?,?,?,?,?,?,?,?)',(first_name,last_name,address_line_1,address_line_2,address_line_3,postcode_with_space,country,telephone_number))
        conn.commit()

def dynamic_business_data_entry():
    for item in business_data_list:
        business_name = item["business_name"]
        address_line_1 = item["address_line_1"]
        address_line_2 = item["address_line_2"]
        address_line_3 = item["address_line_3"]
        postcode_with_space = item["postcode"]
        country = item["country"]
        telephone_number = item["telephone_number"]
        business_category = item["business_category"]
        c.execute('INSERT INTO business(business_name, address_line_1,address_line_2,address_line_3,postcode,country,telephone_number, business_category) VALUES(?,?,?,?,?,?,?,?)',(business_name,address_line_1,address_line_2,address_line_3,postcode_with_space,country,telephone_number, business_category))
        conn.commit()
      




def retrieve_business_cat():
    business_cat_search = input("Enter Type of Business ").title()
    
    
#    print(type(business_cat_search))
    c.execute('SELECT * FROM business  WHERE business_category =? ' ,  (business_cat_search,))
    business_type_filtered_list = []
    for row in c.fetchall():
      business_type_filtered_list.append(row)
    if business_type_filtered_list==[] :
        print("business type not found")
    else:
        print(business_type_filtered_list)
     
            
            
    
        



def retrieve_business_name():
    business_name_search = input("Enter Name of Business ").title()
    print(business_name_search)
#    print(type(business_cat_search))
    c.execute('SELECT * FROM business WHERE business_name =? ' ,  (business_name_search,))
    business_name_filtered_list = []
    for row in c.fetchall():
        business_name_filtered_list.append(row)
    if business_name_filtered_list==[] :
        print("business name not found")
    else:
        print(business_name_filtered_list)

#create_business_table()
#create_person_table()
#create_postcode_table()
retrieve_business_name()    
retrieve_business_cat()    
#dynamic_person_data_entry()
#dynamic_business_data_entry()
#dynamic_coordinates_data_entry()



    
#
#
#
#Person_postcode_api_call():
#    for item in person_data_list:
#        x = item["postcode"]
#        postcode_no_space = x.replace(" ", "")
#        if postcode_no_space not in postcode_table:
#            call_api()
#        else:
#            pass
#    business_postcode_api_call()
#    
#business_postcode_api_call():
#    for item in business_data_list:
#        x = item["postcode"]
#        postcode_no_space = x.replace(" ", "")
#        if postcode_no_space not in postcode_table:
#            call_api()
#        else:
#            pass
    



import psycopg2 as ps

sql = '''
SELECT * FROM phone_book
WHERE 
'''

conn = ps.connect(host = 'localhost',
                  dbname = 'postgres',
                  user = 'postgres',
                  password = 'Barcelona_1899',
                  port = '5432' 
)

cur = conn.cursor()


print(r"Do you want to search by phone(0)/name(1)/break(any num) enter the number:")
mode=int(input())
if mode==0:
        sql+="phone_number"
        print("Enter number")
        subint=int(input())
        print("""Select option:
        1-phone is equal to number
        2-phone starts with the number
        3-phone ends with the number
        4-phone contains the number""")
        mode1=int(input())
        if mode1==1:
            sql+="='{}'".format(subint)
        elif mode1==2:
            sql+=" iLIKE '{}%'".format(subint)
        elif mode1==3:
            sql+=" iLIKE '%{}'".format(subint)
        else:
            sql+=" iLIKE '%{}%'".format(subint)
elif mode==1:
        sql+="""name"""
        print("Enter string")
        substr=input()
        print("""Select option:
        1-name is equal to string
        2-name starts with the string
        3-name ends with the string
        4-name contains the string""")
        mode1=int(input())
        if mode1==1:
            sql+="='{}'".format(substr)
        elif mode1==2:
            sql+=" iLIKE '{}%'".format(substr)
        elif mode1==3:
            sql+=" iLIKE '%{}'".format(substr)
        else:
            sql+=" iLIKE '%{}%'".format(substr)
cur.execute(sql)
print(cur.fetchall())
    
conn.commit()


cur.close()
conn.close()
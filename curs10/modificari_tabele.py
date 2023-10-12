import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='cristian'
)

cursor = my_db.cursor()
# cursor.execute("SHOW TABLES")
# print(list(cursor))
# print(cursor.fetchall())

# cursor.execute('SELECT * FROM projects')
# cursor.execute('SELECT name, address, varsta FROM projects WHERE address="Ploiesti" OR address="Brasov" ORDER BY varsta DESC')  #AND project_number="312"')
# result = cursor.fetchall()
# print(result)

# result = cursor.fetchall()
# print(result)
#
# for i in result:
#     print(i[2])

# result = []
# for row in cursor.fetchall():
#     dictionary = {}
#     for i, value in enumerate(row):
#         dictionary.update({cursor.description[i][0]: value})
#     result.append(dictionary)
# result = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
# for i in result:
#     print(i['address'])

# cursor.execute('DELETE FROM projects WHERE project_number=310')
# my_db.commit()
cursor.execute('SELECT * FROM projects WHERE project_number IN (310,312)')


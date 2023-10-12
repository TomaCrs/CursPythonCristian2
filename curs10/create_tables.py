import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='cristian'
)

cursor = my_db.cursor()
try:
    cursor.execute('CREATE TABLE projects (id INT AUTO_INCREMENT PRIMARY KEY,'
                   'name VARCHAR(255),'
                   'address VARCHAR(255),'
                   'project_number INT)')
except mysql.connector.errors.ProgrammingError:
    pass
# try:
#     cursor.execute('ALTER TABLE projects ADD COLUMN agt INT')
# except mysql.connector.errors.ProgrammingError:
#     pass
# try:
#     cursor.execute('ALTER TABLE projects DROP COLUMN agt')
# except mysql.connector.errors.ProgrammingError:
#     pass
# try:
#     cursor.execute('ALTER TABLE projects RENAME COLUMN age TO varsta')
# except mysql.connector.errors.ProgrammingError:
#     pass
# sql = "INSERT INTO projects (name, address, varsta, project_number) VALUES (%s, %s, %s, %s)"
# val = [
#     ('Petre', 'Bucuresti', 25, 123),
#     ('Amalia', 'Ploiesti', 12, 312),
#     ('Radu', 'Buzau', 22, 677)
# ]
# cursor.executemany(sql, val)
# my_db.commit()
sql = "UPDATE projects SET address='Brasov' where address='Bucuresti'"
cursor.execute(sql)
my_db.commit()

import mysql.connector

def getMarks(value):
    if value == None:
        return 'null'

    if type(value) == str:
        return '"' + value + '"'
    else:
        return str(value)

mydb = mysql.connector.connect(
    host="192.168.14.105",
#    host="127.0.0.1",
    user="root",
    password="12345",
    database='umkehrosmose'
)
tables = ['inputs', 'umkehrosmose.values', 'sensors', 'outputs']

for table in tables:

    create_table_sql = 'CREATE TABLE ' + table  + ' ( \n'
    end = ''

    insert = 'INSERT INTO '

    cursor = mydb.cursor()
    sql = 'SHOW COLUMNS FROM ' + table
    cursor.execute(sql)
    result = cursor.fetchall()


    first_line = True
    for line in result:
        column =  ' ' + line[0] + ' ' + line[1]
        if line[2] == 'NO':
            column = column + ' NOT NULL'
        if line[3] == 'PRI':
            end = end + 'PRIMARY KEY(' + line[0] + '), \n'
        if line[4]:
            column = column + ' DEFAULT ' + line[4];

        create_table_sql = create_table_sql + column + ', \n'

        if first_line:
            insert = insert + '(' + line[0]
        else:
            insert = insert + ', ' + line[0]
        first_line = False

    create_table_sql = create_table_sql + end;
    create_table_sql = create_table_sql[:-1]
    create_table_sql = create_table_sql + ');'

    insert = insert + ') \n'

    sql = 'SELECT * FROM ' + table
    cursor.execute(sql)
    result = cursor.fetchall()

    for line in result:
        insert_line = ''
        first_line = True
        for cell in line:
            if first_line:
                insert_line = insert_line + '(' + getMarks(cell)
            else:
                insert_line = insert_line + ', ' + getMarks(cell)
            first_line = False
        insert = insert + insert_line + '), \n'
    insert = insert[:-1] + ';'

    f = open('./data_' + table + '.sql', 'w')
    f.write(create_table_sql + '\n\n' + insert)
    f.close()
    cursor.close()

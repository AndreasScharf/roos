import grundfossensor as gfs
import mysql.connector
import time
from gpiozero import MCP3008
import dbconfig

current_milli_time = lambda: int(round(time.time() * 1000))
mydb = None
def main():

    mydb = mysql.connector.connect(
        host=dbconfig.config['host'],
        user=dbconfig.config['user'],
        password=dbconfig.config['pw'],
        database=dbconfig.config['db']
    )

    sensors = []
    mycursor = mydb.cursor()
    sql = 'SELECT ID, barcode, type FROM sensors'
    mycursor.execute(sql)
    result = mycursor.fetchall()

    for line in result:
        sensor = gfs.grundfossensor(
            barcode=line[1],
            sensor_id=line[0],
            type=line[2]
        )

        sensors.append(sensor)
    print('All Sensors setup')
    mycursor.close()

    sql = 'SELECT ID, FK_values, FK_sensor, type, offset, equation FROM inputs WHERE active and not type="calc" and not type="time"'
    while 1:
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for line in result:
            type = line[3]
            value = 0
            if type == 'gfs':
                sensor_id = line[2]
                sensor = [elem for elem in sensors if elem.sensor_id == sensor_id][0]

                if line[4] == 'temp':
                    value = sensor.get_tempratur()
                elif line[4] == 'press':
                    value = sensor.get_pessure()
                elif line[4] == 'flow':
                    value = sensor.get_flow()

            elif type == 'analog':
                adc = MCP3008(channel=int(line[4]))
                value = adc.value * 3.3
                return calculate(line[5], value)
            elif type == 'amount':
                current_time = current_milli_time()
                if not int(line['offset']) == 0:
                    delta_time = current_time - int(line['offset'])
                    line[5] = line[5].replace('[t]', delta_time / 60000)
                    value = calculate(line[5])

                correct_time_sql = 'UPDATE umkehrosmose.inputs SET offset="' + current_time + '" WHERE ID=' + line[0]
                correct_time_cur = mydb.cursor()
                correct_time_cur.execute(correct_time_sql)
                mydb.commit()
                correct_time_cur.close()

            elif type == 'calc':
                value = calculate(line[5])
            if value == 'Error':
                print('Error', line[0])
                continue

            eintrag_sql = 'UPDATE ro.values SET value=' + str(value) + ' WHERE ID=' + str(line[1]) + ' AND not manual;'
            eintrag_cursor = mydb.cursor()
            eintrag_cursor.execute(eintrag_sql)
            mydb.commit()
            eintrag_cursor.close()

def calculate(string, x=None):
    numbers = ''
    number = ''
    inNumber = False
    for c in string:
        if inNumber and not c == ']':
            number = number + c
        elif c == '[':
            inNumber = True
        elif c == ']':
            inNumber = False
            numbers = numbers + (' OR ID=' + number )
            number = ''
    if x:
      string = string.replace('x', str(x))

    sql = 'SELECT ID, value FROM ro.values WHERE ID=-1' + numbers
    cursor = mydb.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for line in result:
        string = string.replace('[' + str(line[0]) + ']', str(line[1]))

    return eval(string)
if __name__ == '__main__':
    main()

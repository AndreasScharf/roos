import grundfossensor as gfs
import mysql.connector
import time
import timer
import dbconfig
current_milli_time = lambda: int(round(time.time() * 1000))

mydb = None
def main():
    global mydb
    mydb = mysql.connector.connect(
        host=dbconfig.config['host'],
        user=dbconfig.config['user'],
        password=dbconfig.config['pw'],
        database=dbconfig.config['db']
    )

    debuglist = []

    timers = []
    sql = 'SELECT ID, FK_values, FK_sensor, type, offset, equation FROM inputs WHERE active and type="calc" OR type="time"'
    while 1:

        mycursor = mydb.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for line in result:
            type = line[3]
            value = 0

            if type == 'calc':
                calculate_str = str(line[5]).replace('[t]', str(current_milli_time()))
                value = calculate(calculate_str)
            elif type == 'time':
                calculate_str = str(line[5]).replace('[t]', str(current_milli_time()))

                cur_timer = [elem for elem in timers if elem.id == line[0]]
                offset = 0
                if not len(cur_timer):
                    cur_timer = timer.timer(line[0])
                    if line[4]:
                        cur_timer.reset = int(line[4])
                    else:
                        cur_timer.reset = 0
                    timers.append(cur_timer)
                else:
                    cur_timer = cur_timer[0]

                offset = line[4]


                if offset:
                    index = calculate_str.rindex('*')
                    new_timer = calculate(calculate_str[0 : index])
                    set_bit = calculate(calculate_str[(index + 1):])

                    if set_bit and not cur_timer.timer:
                        cur_timer.timer = new_timer
                        cur_timer.reset = 2
                    if (not set_bit) and cur_timer.reset == 0:
                        cur_timer.timer = new_timer
                        cur_timer.reset = 3
                    if (not set_bit) and cur_timer.reset==3:
                        cur_timer.reset = 0
                        cur_timer.timer = 0

                    value = (cur_timer.elapsed() and (not cur_timer.reset == 3)) or (not cur_timer.elapsed() and cur_timer.reset == 3)

                    if value and cur_timer.reset == 2:
                        cur_timer.reset = 0
                    if (not value) and cur_timer.reset ==3:
                        cur_timer.reset = 1
                        cur_timer.timer = 0

                    print('time=',calculate_str, ' value=', value, 'reset=', cur_timer.reset, 'timer', cur_timer.timer)
                else:
                    new_timer_value = calculate(calculate_str)#gibt mir neuen zeit wert ist 0 wenn aus

                    if  (not new_timer_value) or (not cur_timer.timer):
                      cur_timer.timer = new_timer_value

                    value = cur_timer.elapsed()



            if value == 'Error':
                print('Error', line[0])
                continue
        #       For debugging use
            if line[0] in debuglist:
                print(str(line[1]) + ', '  + str(value) + ' = ' + str(line[5]))

            eintrag_sql = 'UPDATE ro.values SET value=' + str(value) + ' WHERE ID=' + str(line[1]) + ' AND not manual;'
            eintrag_cursor = mydb.cursor()
            eintrag_cursor.execute(eintrag_sql)
            mydb.commit()

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
    try:
        return eval(string)
    except Exception as e:
        print(string)
        return 'Error'
if __name__ == '__main__':
    main()

import output
import mysql.connector
import time
import dbconfig
current_milli_time = lambda: int(round(time.time() * 1000))



pump_offset = 2000 #ms
mydb = None
def main():
    global mydb
    mydb = mysql.connector.connect(
        host=dbconfig.config['host'],
        user=dbconfig.config['user'],
        password=dbconfig.config['pw'],
        database=dbconfig.config['db']
    )

    pumps = []
    ventils = []

    setup_c = mydb.cursor()
    sql = 'SELECT ID, type, Name, run_pin, ready_pin, feedback_pin FROM outputs'
    setup_c.execute(sql)
    result = setup_c.fetchall()

    for line in result:
        if line[1] == 'pump':
            pump = output.pump(
                actor_id=line[0],
                run_pin=line[3],
                ready_pin=line[4],
                feedback_pin=line[5]
            )
            pumps.append(pump)
        elif line[1] == 'ventil':
            ventil = output.ventil(
                actor_id=line[0],
                pin=line[3]
            )
            ventils.append(ventil)
    setup_c.close()
    print('All actors are setup')

    sql = 'SELECT o.ID, type, value, ready, feedback_in, FK_values_disorder FROM outputs o INNER JOIN ro.values v ON o.FK_values=v.ID where active'
    while 1:
        working_c = mydb.cursor()
        working_c.execute(sql)
        result = working_c.fetchall()

        for line in result:
            actor_id = line[0]
            value = line[2]

            if line[1] == 'pump':
                pump = [elem for elem in pumps if elem.actor_id == actor_id][0]
                disorder = not pump.get_ready()

                pump.set_run(value)
                feedback_in = line[4]
                new_time = 0
                current_time = current_milli_time()

                if not feedback_in and value and not pump.get_feedback(): #pumpe gerade eingeschaltent
                    global pump_offset
                    new_time = current_time + pump_offset
                elif feedback_in and value and not pump.get_feedback(): #pumpe eingeschaltet und noch noch kein feedback da
                    disorder = disorder or feedback_in < current_time


                if disorder:
                    pump.set_run(0)
                    new_time = feedback_in

                set_c = mydb.cursor()
                set_sql = 'UPDATE ro.outputs SET feedback_in=' + str(new_time) + ' WHERE ID=' + str(actor_id)
                set_c.execute(set_sql)
                mydb.commit()
                set_sql = 'UPDATE ro.values SET value=' + str(int(disorder)) + ' WHERE ID=' + str(line[5]) + ' AND not manual;'
                set_c.execute(set_sql)
                mydb.commit()
                set_c.close()

            elif line[1] == 'ventil':
                ventil = [elem for elem in ventils if elem.actor_id == actor_id][0]
                if value:
                    ventil.open()
                else:
                    ventil.close()

        working_c.close()
if __name__ == '__main__':
    main()

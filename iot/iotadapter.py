import mysql.connector
import time
import socketio
from datetime import datetime



current_milli_time = lambda: int(round(time.time() * 1000))

ip = '85.214.215.187'
port = 5000
mad = 'eddy_ro'
values_to_cloud = [1, 2, 3, 4, 5, 16, 18, 19, 20, 21, 22, 23]
units_to_cloud = ['', '', '', '', 'bar', 'bar', 'm³', 'm³', 'm³', 'm³', '%', '°C']

mydb = mysql.connector.connect(
    host="192.168.14.105",
#    host="127.0.0.1",
    user="root",
    password="12345",
    database='umkehrosmose'
)
sio = socketio.Client()

def main():

  socket_connected = False
  @sio.event
  def connect():
    print("I'm connected!")
    global socket_connected
    socket_connected = True
    print('socket,', socket_connected)
    sio.emit('alive', {'mad': mad})

  @sio.event
  def connect_error(self):
    print("The connection failed!")
    global socket_connected
    socket_connected = False

  @sio.event
  def disconnect():
    print("I'm disconnected!")
    global socket_connected
    socket_connected = False

  while 1:
    if not socket_connected:
        try:
          sio.connect('http://' + ip + ':' + str(port))
          socket_connected = True
        except KeyboardInterrupt:
          raise
        except:
          print('socket not connected')

    message = [
    {'name': 'mad', 'value':mad, 'unit':''},
    {'name': 'time', 'value':datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'unit':''}, ]

    sql_condition = ' WHERE '
    for value in values_to_cloud:
        sql_condition = sql_condition + 'ID=' + str(value) + ' OR '

    sql_condition = sql_condition[:-3]
    cursor = mydb.cursor()
    sql = 'SELECT name, value FROM umkehrosmose.values ' + sql_condition + ' ORDER BY ID;'
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    i = 0
    for line in result:
        message.append({'name': line[0], 'value': line[1], 'unit': units_to_cloud[i]})
        i = i + 1

    cursor.close()
    if socket_connected:
      sio.emit('recv_data', message)
      sio.sleep(300)


if __name__ == '__main__':
    main()

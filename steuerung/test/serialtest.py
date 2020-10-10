import grundfossensor as gfs

sensor = gfs.grundfossensor(
    barcode='99455941-01-850-00079',
    sensor_id=1,
    type='RPS'
)

while 1:
    print('temp',  sensor.get_tempratur())
    print('press', sensor.get_pessure())

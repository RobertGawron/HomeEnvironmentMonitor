import smbus
import time
import datetime
import sqlite3

db_name = '../HomeEnviromentMonitorServer/db.sqlite3'
conn = sqlite3.connect(db_name)
c = conn.cursor()
 
# Get I2C bus
bus = smbus.SMBus(1)
bus.write_byte(0x40, 0xF5)
 
while(True):
    time.sleep(0.3)
     
    # SI7021 address, 0x40  Read 2 bytes, Humidity
    data0 = bus.read_byte(0x40)
    data1 = bus.read_byte(0x40)
     
    # Convert the data
    humidity = ((data0 * 256 + data1) * 125 / 65536.0) - 6
     
    time.sleep(0.3)
    bus.write_byte(0x40, 0xF3)
    time.sleep(0.3)
     
    # SI7021 address, 0x40 Read 2 bytes, Temperature
    data0 = bus.read_byte(0x40)
    data1 = bus.read_byte(0x40)
     
    # Convert the data and output it
    celsTemp = ((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85
    fahrTemp = celsTemp * 1.8 + 32
     
    print ("Relative Humidity is : %.2f %%" %humidity)
    print ("Temperature in Celsius is : %.2f C" %celsTemp)
    
    # to have exactly the same timestamp on both measurements in database
    now = datetime.datetime.now()
    
    c.execute('insert into datalogger_humiditymeassurement (sample_value, sample_date) values (?, ?)', (humidity, now, )  )
    c.execute('insert into datalogger_temperaturemeassurement (sample_value, sample_date) values (?, ?)', (celsTemp, now, )  )
    
    conn.commit()
    
    time.sleep(60)
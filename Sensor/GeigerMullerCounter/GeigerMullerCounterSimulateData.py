import datetime
import random
import sqlite3


class GeigerMullerCounterSimulateData():
    def __init__(self, database_path_filename):
        self.database_handler = sqlite3.connect(database_path_filename)

    def simulate(self, sensor_id,
                 number_of_generated_samples, max_sample_value):
        database_query = self.database_handler.cursor()

        base = datetime.datetime.today()
        date_list = [base - datetime.timedelta(minutes=m)
                     for m in range(number_of_generated_samples)]

        for sample_timestamp in date_list:
            sample_value = random.randint(0, max_sample_value)
            database_query.execute('insert into Sensor_measurement\
                (Date, Value, Sensor_id)values (?, ?, ?);',
                                   (sample_timestamp, sample_value,
                                    sensor_id, ))

        self.database_handler.commit()

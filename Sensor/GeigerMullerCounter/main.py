from GeigerMullerCounterSimulateData import GeigerMullerCounterSimulateData

if __name__ == "__main__":
    database_path_filename = '../../Server/Server/db.sqlite3'
    simulator = GeigerMullerCounterSimulateData(database_path_filename)

    sensor_id = 1
    number_of_generated_samples = 60*24  # 24 hours
    max_sample_value = 120
    simulator.simulate(sensor_id,
                       number_of_generated_samples, max_sample_value)

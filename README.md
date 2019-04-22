# Home Environment Monitor

## Purpose

Home Environment Monitor is a web application for visualizing and analyzing environmental measurement data collected from various sensors. The application is built on Grafana and InfluxDB, and is containerized using Docker for easy deployment and management.

This project is designed to run on a Raspberry Pi and was initially created to gather data from the following sensor-based projects:

* [Gamma Spectrometer](https://github.com/RobertGawron/GammaSpectrometer)
* [Ionization Chamber](https://github.com/RobertGawron/IonizationChamber)
* [Semiconductor Radioactivity Detector](https://github.com/RobertGawron/SemiconductorRadioactivityDetector)
* [Geiger-Muller Counter](https://github.com/RobertGawron/GeigerMullerCounter)
* Weather Station: Monitors home temperature and humidity.

## Features
* Real-time data visualization: Display sensor data using customizable Grafana dashboards.
* Data storage: Efficient storage of time-series data using InfluxDB.
* Modular sensor integration: Easily extend to include new sensors and data sources.
* Raspberry Pi compatible: Lightweight enough to run on a Raspberry Pi, perfect for home-based environmental monitoring.
* Docker-based deployment: Simplified setup and containerized services for easy installation and scaling.

## Setup

### Prerequisites

TODO
<!--
Make sure you have the following installed on your Raspberry Pi:

Docker: Used to run the application in a containerized environment.
Docker Compose: To manage multiple services (Grafana, InfluxDB) as a single application.
You can install Docker and Docker Compose by running the following commands:

bash
Copier le code
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo apt-get install docker-compose
Installation
Clone the repository:

bash
Copier le code
git clone https://github.com/RobertGawron/HomeEnvironmentMonitor.git
cd HomeEnvironmentMonitor
Set up the configuration:

Customize the config.yml file (if required) with your sensor and database information.

Start the application:

Use Docker Compose to start all services:

bash
Copier le code
sudo docker-compose up -d
Access the web interface:

Once the services are running, you can access the Grafana dashboard by navigating to:

arduino
Copier le code
http://<your-raspberry-pi-ip>:3000
Default Grafana credentials:
Username: admin
Password: admin (you’ll be prompted to change it on the first login)
Data Sources Setup
After logging into Grafana, you’ll need to configure InfluxDB as the data source:

In the Grafana dashboard, navigate to Configuration > Data Sources.
Add a new InfluxDB data source and configure it with the following details:
URL: http://influxdb:8086
Database: your-database-name
Username: your-username
Password: your-password
Adding New Sensors
To integrate additional sensors, follow these steps:

Configure your sensor to send data to InfluxDB (directly or via a script).
Update Grafana dashboards to visualize the new data. You can create custom panels to display the sensor data in real-time.
Contributing
Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request. Please ensure your code follows the project's coding standards and is well-documented.
-->
### License
This project is licensed under the MIT License. See the LICENSE file for details.


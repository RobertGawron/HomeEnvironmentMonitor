# HomeEnvironmentMonitor

[![Static Code Analysis](https://github.com/RobertGawron/HomeEnvironmentMonitor/workflows/Static%20Code%20Analysis/badge.svg)](https://github.com/RobertGawron/HomeEnvironmentMonitor/actions?query=workflow%3A%22Static+Code+Analysis%22)

## Summary

This is a RaspberryPi based web sever for storage and visualization of data from various sensors that I made:
* [Gamma Spectrometer](https://github.com/RobertGawron/GammaSpectrometer)
* [Ionization Chamber](https://github.com/RobertGawron/IonizationChamber)
* [Semiconductor Radioactivity Detector](https://github.com/RobertGawron/SemiconductorRadioactivityDetector)
* [Geiger-Muller Counter](https://github.com/RobertGawron/GeigerMullerCounter)

## Setup

In ./Server directory run

```
virtualenv env
source env/Scripts/activate
pip install -r requirements.txt
```
# HomeEnvironmentMonitor

[![Static Code Analysis](https://github.com/RobertGawron/HomeEnvironmentMonitor/workflows/Static%20Code%20Analysis/badge.svg)](https://github.com/RobertGawron/HomeEnvironmentMonitor/actions?query=workflow%3A%22Static+Code+Analysis%22)

## Summary

**Note: this project is in very early state, also I'm not a web developer, so probably a lot of things are wrong. Any feedback is welcome :-)**

This is a RaspberryPi based web sever for storage and visualization of data from various sensors, it was made to work dor below ones, but it should be easily extendable for new ones:
* [Gamma Spectrometer](https://github.com/RobertGawron/GammaSpectrometer)
* [Ionization Chamber](https://github.com/RobertGawron/IonizationChamber)
* [Semiconductor Radioactivity Detector](https://github.com/RobertGawron/SemiconductorRadioactivityDetector)
* [Geiger-Muller Counter](https://github.com/RobertGawron/GeigerMullerCounter)
* Weather Station (home temperature and humidity sensor).

## Setup

* [Setting-up server](./Server/README.md)
* Sensors:
    * TBD, they will probably run as separate processes and communicate via database queries.




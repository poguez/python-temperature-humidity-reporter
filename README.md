# Python Temperature and humidity reporter for Raspberry Pi

Raspbian-Python-based service for reporting temperature and humidity with AOSONG 2302 or any DHT sensor. 

## Dependencies

[Adafruit_Python_DHT](https://github.com/adafruit/Adafruit_Python_DHT) v1.3.2

Raspbian Jessie 
(There is an issue with upper versions because of Adafruit_Python_DHT dependency.)
 
Also check `requirements.txt`

## Test hardware
- Raspberry Pi 3
- AOSONG 2302

## Install Adafruit_Python_DHT from source

Install from source the version 1.3.2 because it is not yet available on PyPi.

```

git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install

```

## Configuration

Clone the repository:

`git clone this repo in /home/pi`

Configure your URL and json payload parameters.
```

    {
        "measurement_type_id": 2,
        "magnitude": t,
        "measurement_area": 1, 
        "created_at": ""
    }

```

Copy the service to systemd:

`sudo cp python-temperature-humidity-reporter.service /etc/systemd/system`

Change permission for the service:

`sudo chmod 664 /etc/systemd/python-temperature-humidity-reporter.service`

Reload systemd services:

`sudo systemctl daemon-reload`

Enable the service:

`sudo systemctl enable python-temperature-humidity-reporter.service`

Start the service:

`sudo systemctl start python-temperature-humidity-reporter.service`

## Related repositories

[Scala Akka-http measurement store](https://github.com/poguez/measurement-store-service)
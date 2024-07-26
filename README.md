# DS18B20-thermometer-service
An RPi flask REST API for the DS18B20 waterproof thermometer

Ensure the w1-gpio line is present at the end of the /boot/config.txt file. If the GPIO pin on the 
RPi is not GPIO4, then change the second parameter accordingly

vi /boot/config.txt
dtoverlay=w1-gpio,gpiopin=4

Currently listens on port 5000, can be changed in the service file

Supported Endpoints
/DS18B20/c
{"value":25.25}

/DS18B20/f
{"value":77.45}



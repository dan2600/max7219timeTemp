Project for Raspberry PI to display Temp and next Manhattan Bound L train on 4 8x8 LED screens run by Max7219 chips.

Python 2.7 because why not.

dependency:

sudo -H pip install --upgrade gtfs-realtime-bindings
sudo -H pip install protobuf3_to_dict
sudo -H pip install -U python-dotenv
sudo -H  pip install request
sudo -H pip install --upgrade luma.led_matrix

also need Luma.LED_Matrix and to enable GPIO pins, install instructions are here:
https://luma-led-matrix.readthedocs.io/en/latest/install.html

also you need to make a .env file with a API_KEY=
you need to get an API key from the MTA
http://datamine.mta.info/user/register

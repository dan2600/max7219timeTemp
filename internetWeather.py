from weather import Weather, Unit
from requests.exceptions import ConnectionError
weather = Weather()
def getWeather():
    weather = Weather(unit=Unit.FAHRENHEIT)

    try:
        location = weather.lookup('2459115')
    except ConnectionError as e:
        print e
        class error:
            def text(x):
                return "read error"
            def temp(x):
                return "0"
        condition = error()
        return [condition]
    try:
        condition = location.condition()
    except:
    	print("Read Error")
        class error:
            def text(x):
                return "read error"
            def temp(x):
                return "0"
        condition = error()
    return [condition]
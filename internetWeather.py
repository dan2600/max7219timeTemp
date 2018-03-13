from weather import Weather, Unit
weather = Weather()
def getWeather():
	weather = Weather(unit=Unit.FAHRENHEIT)
	location = weather.lookup_by_location('brooklyn')
	condition = location.condition()
	forecasts = location.forecast()
	return [condition, forecasts]



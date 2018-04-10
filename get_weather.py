from weather import Weather, Unit
import location

def weather_loc(location):
	print(location+"\'s weather and forecast")
	weather = Weather(unit=Unit.CELSIUS)
	location = weather.lookup_by_location(location)
	condition = location.condition
	#print(condition.text)
	print("Last updated "+condition.date+" Condition :- "+condition.text)
	forecasts = location.forecast
	#print(len(forecasts))
	for forecast in forecasts:
	    print("On date "+forecast.date+" Condition :- "+forecast.text+" High :- "+forecast.high+" Low :- "+forecast.low)

def get_local_weather():
	return weather_loc(location.get_city())

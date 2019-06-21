# Solar Position Algorithm

Calculate the solar position (azimuth and elevation) for any day and time (tested only after 00:00 on January 1, 1970).

## Usage

Create a sun object `sol = Sun()`. Using the method `calcSun()` prints the calculated solar position. 

	sol.calcSun(year=2019, day=14, month=6, hour=17, minute=49, second=0 lat=43, long=-78)
	
Several optional keyword arguments are provided:
-`year`, `month`, `day` date input
-`hour`, `minute`, `second` time input UTC
-`lat` and `long` are keywords for latitude and longitude, in degrees (N.B. 78W is entered as `long=-78` and 43S is entered as `lat=-43`).

## Future Features

- Calculate azimuth at apparent sunrise and apparent sunset
- Calculate time at solar noon
- Graph solar track
- Plot and/or calculate at a given time interval

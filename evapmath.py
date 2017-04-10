import math
 
# Temp Dry Bulb
Tdbf = int(input("Temperature in Fahrenheit: "))
 
# Convert Tdb to Celsius
Tdb = (Tdbf - 32) / (9.0/5.0)
 
# Humidity in Whole Number
Hum = float(input("Humidity: \n"))
 
# Calculate RH/Temp to get DewPoint
X = 1-(0.01*Hum)
Td = Tdb-(14.55+0.144*Tdb)*X-((2.5+0.007*Tdb)*X)**3-(15.0+0.117*Tdb)*X**14
Tdf = (Td*1.8)+32
 
# Temp Wet bulb
Twb = (-5.806+0.672*Tdb-0.006*Tdb*Tdb+(0.061+0.004*Tdb+0.000099*Tdb*Tdb)*Hum+(-0.000033-0.000005*Tdb-0.0000001*Tdb*Tdb)*Tdb*Tdb)
 
# Temp Leaving Air
Tla = Tdb - ((Tdb - Twb) * .85)
 
#Convert Temp Leaving Air from Celsius to Fahrenheit
Tfh = (Tla * (9.0/5.0)) + 32
 
print 'Temperature Leaving Evap Cooler is: %sF' % Tfh
print 'Dewpoint is: %sF' % Tdf
print 'Temp Wetbulb #1 is %sC' %Twb

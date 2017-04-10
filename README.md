# pyCooler
pyMath for Effectiveness of an Evaporation cooler using an input of just Temp and Humidity

This was written one hot summer while I sat in my livingroom swealtering under the high heat and high humidity of a swamp cooler.
I got up, went to the humdifier and put a thermometer in front of it.  Than went outside, checked the temp outside and realized
that the bloody thing was just blowing hot air into the house.  Thus, pyCooler was born.  I figured there had to be a way
to realize the efficency of a swamp cooler.  Yes, you can take temp wet bulb, the dewpoint, the current humidity levels and
the effectiveness of the swamp cooler and run the numbers all from the safety of weather.com, a piece of scratch paper and a
calculator.  But that defeated my purpose.  I wanted automation, a way where I could run my little arduino creation with a
DHT22 Temp/Humidity sensor and just let it output the estimated Output Temp.

One look, 'oh it's 90F outside and it's only going to cool it to 87F but probably push off a bunch of humidity in the house, 
 I'll just open windows and kick the fan on the swamp coolor'.  Or 'oh it's 90 and it will drop it to 76, I'll live with that'.
 
 The Attached code is just the math.  Your input is python (I will dig through my old code and find my origional C code for the
 pyCooler that I used for this arduino.  However the math is pretty simple and can be converted to C quite quickly.  From there
 just input the data from the arduino into the input fields.  Or manually put temp/humidity in and output your results.
 
 Happy Coding!
 

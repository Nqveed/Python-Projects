# Standard Devitiation:
# speed=[86,87,88,86,87,85,86]/6=3.1 ,2.9 
# [1+2+4+6+2+4]
# There are 2 type of SD: Low SD and high SD,
# example for Low SD:
import numpy
speed=[86,87,88,86,87,85,86]
a= numpy.std(speed)
print(a)
# example for high SD:
import numpy
speed=[32,111,138,28,59,77,97]
b= numpy.std(speed)
print(b)
# Variance: how the values are spread
# if  you take the square of root of Variance you will get the SD.
# to calculate the Variance you have to do the below thing
# speed=[32+111+138+28+59+77+97]=77.4
# 32-77.4= -45.6 square root 2079.16
# 111-77.4= 33.3 square root  1122.25
# 138-77.4= 61.6 square root  3794.56
# 28-77.4= -49.4 square root  2494.36
# 59-77.4= 18.4  square root   338.56
# 77.77.4= -.4   square root   0.25
# 97-77.4=  19.6 square root   384.16
# Variance is the average number of these squared difference
# (2079.16+1122.25+3794.56+2494.36+338.56+0.25+384.16)/7=1451.85
# As we leaned  the formula the SD is the square root of the Variance
# square root 1451.85= 37.84
# example of numpy std()
import numpy
speed=[32,111,138,28,59,77,97]
c= numpy.std(speed)
print(c)
# symbol of SD and Variance:
# Standard Devitiation= sigma
# Variance symbol=square root

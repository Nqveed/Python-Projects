# Data Data set: [99,86,87,88,111,86,103,87,94,78,77,85,87]
# In ML and math also there baseically three values that are actually interest to us:
# Mean: the average value
# Median:  the mid point value
# Mode:the most common value
# Here in this example we  have speed of cars
# Speed =  [99,86,87,88,111,86,103,87,94,78,77,85,87]
# Mean: to calculate the mean, sum all the values
# sum of all speed/cars( 99+86+87+88+111+86+103+87+94+78+77+85+87)/13 - avg values = 89.84
import numpy as np
speed =  [99,86,87,88,111,86,103,87,94,78,77,85,87]
b=np.mean(speed) 
print(b)
# Median: Here we will find the middle value median value 87.0
import numpy as np
speed =  [99,86,87,88,111,86,103,87,94,78,77,85,87]
c = np.median(speed)
print(c)
# even numbers values
import numpy as np
sp = [2,4,6,8,10,12]
d=np.median(sp)
print(d)
# Mode: the value that appears most number of times:we will use scipy mode()
from scipy import stats
speed =  [99,86,87,88,111,86,103,87,94,78,77,85,87]
h= stats.mode(speed)
print(h)







# Data Distribution: How do we get to big Data set
# Here now we will create a array containing 250 random floats between 0.0 to 5.0
import numpy as np
a= np.random.uniform(0.0,5.0,250)
print(a)
# visualiization of big Data set
import numpy as np
import matplotlib.pyplot as plt
b= np.random.uniform(0.0,5.0,250)
plt.hist(b,5)
plt.show()
# Big Data Distribution 
# now we create an array with 100000 random numbers and display them using the hist 100 bars
import numpy as np
a= np.random.uniform(0.0,5.0,250)
print(a)
# visualiization of big Data set
import numpy as np
import matplotlib.pyplot as plt
c= np.random.uniform(0.0,5.0,100000)
plt.hist(c,100)
plt.show()

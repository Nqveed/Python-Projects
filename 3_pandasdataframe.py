# Various ways to creating DataFrame as using dictionary 
import pandas as pd
data={'Name':['Naveed','Varun','Natin','Diljit'],'Age':[30,37,34,32],'Salary':[100000,80000,70000,75000]}
df=pd.DataFrame(data)
print(df)
# using list
import pandas as pd
data1=[['Naveed',30,100000],['Varun',37,80000],['Natin',34,7000],['Diljit',32,750000],['Ranveer',31,65000]]
df=pd.DataFrame(data1,columns=['Name','Age','Salary'])
print(df)
# using array
# import pandas as pd
# import numpy as np
# data1=np.array([['Naveed',30,100000],['Varun',37,80000],['Sharma',34,70000],['Rahul',32,750000],['Ranveer',31,65000]])
# df=pd.DataFrame(data1,columns=['Name','Age','Salary'])
# print(df)
# import pandas as pd
# data = { "cal":[350,400,450],"duration":[40,45,50]}
# b = pd.DataFrame(data)
# print(b)
# import pandas as pd
# data = { "cal":[350,400,450],"duration":[40,45,50]}
# b = pd.DataFrame(data)
# print(b.loc[0])
# import pandas as pd
# data = { "cal":[350,400,450],"duration":[40,45,50]}
# b = pd.DataFrame(data)
# print(b.loc[[0,1]])
# import pandas as pd
# data = { "cal":[350,400,450],"duration":[40,45,50]}
# b = pd.DataFrame(data, index=["day1", "day2" , "day3"])
# print(b)
# import pandas as pd
# data = { "cal":[350,400,450],"duration":[40,45,50]}
# b = pd.DataFrame(data, index=["day1", "day2" , "day3"])
# print(b.loc[["day2","day3"]])
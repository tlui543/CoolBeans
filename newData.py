import pandas as pd
import matplotlib.pyplot as plt

data1990 = [0.4, 0.2, 3.8, 12.4, 3.6, 17.7, 3.3, 6.1, 2.7, 2.0, 1.9, 0.5, 7.4, 4.5, 0.0, 3.0, 0.5, 3.6, 3.7, 8.0, 10.4, 1.6, 0.0]

data2014 = [0.5, 0.5, 6.2, 15.6, 11.2, 18.4, 5.2, 22.6, 3.1, 2.1, 2.6, 0.8, 8.0, 18.1, 4.0, 19.4, 1.2, 8.8, 6.8, 12.5, 14.3, 2.5, 0.6]

countries = ["Afghanistan", "Bahamas", "Canada", "China", "Dominican Republic", "Ethiopia", "Guam", "Hungary", "India", "Japan", "Korean Rep", "Liberia", "Malaysia", "Netherlands", "Oman", "Peru", "Qatar", "Russian Federation", "Serbia", "Thailand", "USA", "Vietnam", "Yemen Rep." ]



dataDF = pd.DataFrame (
  {
    "data1990": data1990,
    "data2014": data2014,
    "countries": countries
  }
)

print (dataDF)



dataDF.plot(
  x='countries',
  y=['data1990', 'data2014'],
  kind='bar',
  title = ''' Marine Protected Area (% of Total Territorial Area) in Selected Countries
   in 1990 v.s. 2014 ''',
  colormap = 'Pastel2'
)




plt.xlabel('Countries')
plt.ylabel('Marine Protected Area (% of total territorial area) ')
plt.show()



#http://data.worldbank.org/indicator/ER.PTD.TOTL.ZS?view=chart

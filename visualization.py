import requests 
from datetime import datetime
import matplotlib.pyplot as plt
#city_name=input("Enter name of the city: ")
city_list=["karachi","Quetta","islamabad","kohat","lahore","Multan","Rawalpindi","faisalabad","Sialkot","Jhang","Sahiwal","Balochistan","Sargodha","Bahawalpur","Gujranwala","Muzaffarabad","Mirpur","Hyderabad","Nawabshah","Murree","Sukkur","Chitral","Dera Ghazi Khan","okara"]
y=[]
for i in city_list:
    api_key="1cacf70de74ded39e4aec3dca2ff9436"
    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+i+"&appid="+api_key
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()
    for j in api_data:
        if j=="main":
            print(i,": ",api_data[j]["temp"])
            y.append(api_data[j]["temp"])
#temperature pattern visualization
plt.style.use("Solarize_Light2")     
fig,sub_plot=plt.subplots(figsize=(20,60))
plt.xticks(rotation=45, fontsize=10)
sub_plot.grid(True, linestyle='--', alpha=0.6)      
sub_plot.plot(city_list,y)
sub_plot.set(title="Temperature visualization of different cities of pakistan",xlabel="Cities",ylabel="Temperature")
plt.show()
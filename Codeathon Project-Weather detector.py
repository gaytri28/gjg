from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title('Live AQI Fetcher')

fw=LabelFrame(root, padx = 50, pady = 50)
fw.pack(padx=25,pady=25)

#function to fetch live AQI of Las Vegas
def LasVegas():
        w1=Toplevel()
        f1=LabelFrame(w1,padx=50,pady=50,bg='yellow',relief=RAISED)
        f1.pack(padx=15,pady=15)
        api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=96A38DFD-5C56-4740-AD99-E38C0C855A1B")
        api=json.loads(api_request.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']
        if category=='Good':
                weather_color='#0C0'
        elif category=='Moderate':
                weather_color='#FFFF00'
        elif category=='Unhealthy for sensitive groups':
                weather_color='#ff9900'
        elif category=='Unhealthy':
                weather_color='#FF0000'
        elif category=='Very unhealthy':
                weather_color='#990066'
        elif category=='Hazardous':
                weather_color='#660000'
        mylabel=Label(f1,text='The Color of text shows intensity of pollutants:',font=('Helvetica',24),anchor=E).grid(row=0,column=0,padx=50)
        mylabel2=Label(f1,text=city+' LIVE Air quality'+' : '+str(quality)+' - '+category,font=('Helvetica',22),fg=weather_color).grid(row=2,column=0,pady=15)
       
        

#function to fetch live AQI of New York
def NewYork():
        w2=Toplevel()
        f2=LabelFrame(w2,padx=50,pady=50,bg='cyan',relief=RAISED)
        f2.pack(padx=15,pady=15)
        api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10001&distance=5&API_KEY=96A38DFD-5C56-4740-AD99-E38C0C855A1B")
        api=json.loads(api_request.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']
        if category=='Good':
                weather_color='#0C0'
        elif category=='Moderate':
                weather_color='#FFFF00'
        elif category=='Unhealthy for sensitive groups':
                weather_color='#ff9900'
        elif category=='Unhealthy':
                weather_color='#FF0000'
        elif category=='Very unhealthy':
                weather_color='#990066'
        elif category=='Hazardous':
                weather_color='#660000'
        mylabel=Label(f2,text='The Color of text shows intensity of pollutants:',font=('Helvetica',24),anchor=E).grid(row=0,column=0,padx=50)
        mylabel2=Label(f2,text=city+' LIVE Air quality'+' : '+str(quality)+' - '+category,font=('Helvetica',22),fg=weather_color).grid(row=2,column=0,pady=15)
       
#function to fetch live AQI of Los Angeles
def LosAngeles():
        w3=Toplevel()
        f3=LabelFrame(w3,padx=50,pady=50,bg='turquoise',relief=RAISED)
        f3.pack(padx=15,pady=15)
        api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=90001&distance=5&API_KEY=96A38DFD-5C56-4740-AD99-E38C0C855A1B")
        api=json.loads(api_request.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']
        if category=='Good':
                weather_color='#0C0'
        elif category=='Moderate':
                weather_color='#FFFF00'
        elif category=='Unhealthy for sensitive groups':
                weather_color='#ff9900'
        elif category=='Unhealthy':
                weather_color='#FF0000'
        elif category=='Very unhealthy':
                weather_color='#990066'
        elif category=='Hazardous':
                weather_color='#660000'
        mylabel=Label(f3,text='The Color of text shows intensity of pollutants:',font=('Helvetica',24),anchor=E).grid(row=0,column=0,padx=50)
        mylabel2=Label(f3,text=city+' LIVE Air quality'+' : '+str(quality)+' - '+category,font=('Helvetica',22),fg=weather_color).grid(row=2,column=0,pady=15)
      
        
        
#function to fetch live AQI of Chicago
def chicago():
        w4=Toplevel()
        f4=LabelFrame(w4,padx=50,pady=50,bg='Teal',relief=RAISED)
        f4.pack(padx=15,pady=15)
        api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=60007&distance=5&API_KEY=96A38DFD-5C56-4740-AD99-E38C0C855A1B")
        api=json.loads(api_request.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']
        if category=='Good':
                weather_color='#0C0'
        elif category=='Moderate':
                weather_color='#FFFF00'
        elif category=='Unhealthy for sensitive groups':
                weather_color='#ff9900'
        elif category=='Unhealthy':
                weather_color='#FF0000'
        elif category=='Very unhealthy':
                weather_color='#990066'
        elif category=='Hazardous':
                weather_color='#660000'
        mylabel=Label(f4,text='The Color of text shows intensity of pollutants:',font=('Helvetica',24),anchor=E).grid(row=0,column=0,padx=50)
        mylabel2=Label(f4,text=city+' LIVE Air quality'+' : '+str(quality)+' - '+category,font=('Helvetica',22),fg=weather_color).grid(row=2,column=0,pady=15)
        
        


#function to fetch live AQI of San Francisco
def SanFrancisco():
        w5=Toplevel()
        f5=LabelFrame(w5,padx=50,pady=50,bg='#98ff98',relief=RAISED)
        f5.pack(padx=15,pady=15)
        api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=94102&distance=5&API_KEY=96A38DFD-5C56-4740-AD99-E38C0C855A1B")
        api=json.loads(api_request.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']
        if category=='Good':
                weather_color='#0C0'
        elif category=='Moderate':
                weather_color='#FFFF00'
        elif category=='Unhealthy for sensitive groups':
                weather_color='#ff9900'
        elif category=='Unhealthy':
                weather_color='#FF0000'
        elif category=='Very unhealthy':
                weather_color='#990066'
        elif category=='Hazardous':
                weather_color='#660000'
        mylabel=Label(f5,text='The Color of below text shows intensity of pollutants:',font=('Helvetica',24),anchor=E).grid(row=0,column=0,padx=50)
        mylabel2=Label(f5,text=city+' LIVE Air quality'+' : '+str(quality)+' - '+category,font=('Helvetica',22),fg=weather_color).grid(row=2,column=0,pady=15)
       
        
#Label for instruction
label_a=Label(fw,text='This is a program to fetch live Air Quality Index of below mentioned mega cities. Please click a button',font=('Helvetica',24)).grid(row=0,column=0)
label_b=Label(fw,text='NOTE: This program requires internet access as it fetches live AQI. Please ensure net connectivity!',font=('Helvetica',24)).grid(row=2,column=0,pady=20)


#Buttons for various states        
Button_1=Button(fw,text='Las Vegas',command=LasVegas,anchor=W).grid(row=6,column=0,pady=15)
Button_2=Button(fw,text='New York',command=NewYork).grid(row=7,column=0,pady=15)
Button_3=Button(fw,text='Los Angeles',command=LosAngeles).grid(row=8,column=0,pady=15)
Button_4=Button(fw,text='Chicago',command=chicago).grid(row=9,column=0,pady=15)
Button_5=Button(fw,text='San Francisco',command=SanFrancisco).grid(row=10,column=0,pady=15)


root.mainloop()
               

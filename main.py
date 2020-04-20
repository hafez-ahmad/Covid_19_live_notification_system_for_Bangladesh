 # coding=utf8
import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime
import threading
from datetime import date

today = date.today()



# parsing html and extracting data
def get_corona_detail_of_Bangladesh():
    url = "https://www.iedcr.gov.bd/"
    r=requests.get(url)
    html=r.text
    soup=bs4.BeautifulSoup(html,'html.parser')
    tbody=soup.find('tbody')
    t_row=tbody.find_all('td')
    return t_row[15].text


def get_death():
    url1 = "https://www.iedcr.gov.bd/"
    r1=requests.get(url1)
    html1=r1.text
    soup1=bs4.BeautifulSoup(html1,'html.parser')
    imp=soup1.find_all('div',class_='col-sm-3')
    death=imp[3]
    t=death.text
    t1=t[13:16]
    return t1

# function use to  reload the data from website
def refresh():
    newdata = get_corona_detail_of_Bangladesh()
    print("Refreshing..")
    mainLabel['text'] = newdata


# function for notifying...
def notify_me():
    while True:
        plyer.notification.notify(
            title="COVID 19 cases of Bangladesh",
            message=get_corona_detail_of_Bangladesh() ,
            timeout=10,
            app_icon='Coronavirus.ico'
        )
        time.sleep(30)



# creating gui:
root = tk.Tk()
root.geometry("900x800")
root.iconbitmap("Coronavirus.ico")
root.title("CORONA DATA TRACKER  Bangladesh ,built by Hafez Ahmad হাফেজ আহমদ ")
root.configure(background='white')
f = ("poppins", 25, "bold")
banner = tk.PhotoImage(file="Iconarchive-Blue-Election-Election-Banner.png")
bannerLabel = tk.Label(root, image=banner)
bannerLabel.pack()
mainLabel = tk.Label(root, text='Covid-19 Live and Notification System for Bangladesh ' , font=f, bg='white')
mainLabel.pack()
mainLabel = tk.Label(root, text=" Total Case: " +get_corona_detail_of_Bangladesh(), font=f, bg='white')
mainLabel.pack()
mainLabel = tk.Label(root, text=" Total Deaths: "+ get_death() , font=f, bg='white')
mainLabel.pack()

mainLabel = tk.Label(root, text='Data source: https://www.iedcr.gov.bd/ ' , font=f, bg='white')
mainLabel.pack()


mainLabel = tk.Label(root, text=today, font=f, bg='white')
mainLabel.pack()

reBtn = tk.Button(root, text="Refresh Me", font=f, relief='solid', command=refresh)
reBtn.pack()

mainLabel = tk.Label(root, text='Developed By Hafez Ahmad ' , font=f, bg='white')
mainLabel.pack()

#mainLabel = tk.Label(root, text=" কি করবেন  :\n ১: ঘন ঘন সাবান ও পানি দিয়ে বা অ্যালকোহলযু্ক্ত হাত-ধোয়ার সামগ্রী ব্যবহার করে আপনার হাত ধূয়ে নিন \n২: মুখ ঢেকে হাঁচি দেয়া \n৩: কাশি বা হাঁচি দেবার সময় মুখ এবং নাক কনুই দিয়ে বা টিস্যু দিয়ে ঢেকে রাখুন। \n৪: ঠান্ডা লেগেছে বা জ্বরের লক্ষণ আছে এমন ব্যক্তি\n৫:ঠান্ডা লেগেছে বা জ্বরের লক্ষণ আছে এমন ব্যক্তির সংস্পর্শ এড়িয়ে চলুন\n৬: আপনার বা আপনার সন্তানের জ্বর, কাশি বা শ্বাসকষ্ট হলে দ্রুত চিকিৎসা সেবা নিন।\n৭: আপনার বা আপনার সন্তানের জ্বর, কাশি বা শ্বাসকষ্ট হলে দ্রুত চিকিৎসা সেবা নিন" , font=f, bg='white')
mainLabel = tk.Label(root, text=' ঘরে থাকুন ও নিরাপদে থাকুন ' , font=f, bg='white')
mainLabel.pack()
# create a new thread
th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()


root.mainloop()

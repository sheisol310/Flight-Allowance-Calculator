import tkinter as tk
from datetime import datetime
from tkinter.ttk import Combobox


def cal_perdiem():
    report_time = datetime(int(yr1.get()), int(mon1.get()), int(day1.get()), int(hr1.get()), int(min1.get()))
    end_time = datetime(int(yr2.get()), int(mon2.get()), int(day2.get()), int(hr2.get()), int(min2.get()))
    period = end_time - report_time
    minutes = period.total_seconds() / 60
    hours = minutes / 60
    print('Total difference in hour: ', hours)
    after_hours = hours + 3
    sequence = " {} + 3 = {}".format(hours, after_hours)
    perdiem_hr.config(state='normal')
    perdiem_hr.delete(0, tk.END)
    perdiem_hr.insert(0, sequence)
    perdiem_hr.config(state='disabled')

    p_money = after_hours * 90
    perdiem_amount.config(state='normal')
    perdiem_amount.delete(0, tk.END)
    perdiem_amount.insert(0, p_money)
    perdiem_amount.config(state='disabled')


def cal_flight_allowance():
    total_hr = int(flight_hours.get())
    rate = int(flight_rate.get())
    ensure_pay = rate * 60
    if total_hr < 60:
        f_money = ensure_pay
    elif total_hr == 60:
        f_money = 60 * rate * 1.25
    elif 60 < total_hr <= 75:
        f_money = rate * 1.25 * 60 + rate * 1.5 * (total_hr - 60)
    elif 75 < total_hr <= 90:
        f_money = rate * 1.25 * 60 + rate * 1.5 * 15 + rate * 1.75 * (total_hr - 75)
    elif 90 < total_hr <= 100:
        f_money = rate * 1.25 * 60 + rate * 1.5 * 15 + rate * 1.75 * 15 + rate * 2.5 * (total_hr - 90)
    elif total_hr > 100:
        f_money = rate * 1.25 * 60 + rate * 1.5 * 15 + rate * 1.75 * 15 + rate * 2.5 * 10 + rate * 3.5 * (
                total_hr - 100)

    flight_allow.config(state='normal')
    flight_allow.delete(0, tk.END)
    flight_allow.insert(0, f_money)
    flight_allow.config(state='disabled')


window = tk.Tk()
window.geometry("500x420")
window.resizable(width=True, height=True)
window.title('EVA Allowance Calculator')

l1 = tk.Label(window, text="航班日支費計算", font=("Arial bold", 20))
l1.place(x=20, y=20)
l2 = tk.Label(window, text="報到時間 : ", font=("Arial", 14))
l2.place(x=20, y=80)

yr1 = tk.StringVar()
mon1 = tk.StringVar()
day1 = tk.StringVar()
hr1 = tk.StringVar()
min1 = tk.StringVar()

tk.Label(window, text='Year').place(x=100, y=60)
year_combobox_1 = Combobox(window, width=5, values=[*range(2021, 2100)], textvariable=yr1, justify='center')
year_combobox_1.place(x=100, y=80)

tk.Label(window, text='Month').place(x=180, y=60)
month_combobox_1 = Combobox(window, width=3, values=[*range(1, 13)], textvariable=mon1, justify='center')
month_combobox_1.place(x=180, y=80)

tk.Label(window, text='Day').place(x=240, y=60)
day_combobox_1 = Combobox(window, width=4, values=[*range(1, 32)], textvariable=day1, justify='center')
day_combobox_1.place(x=240, y=80)

tk.Label(window, text='Hour').place(x=310, y=60)
hour_combobox_1 = Combobox(window, width=3, values=[*range(0, 24)], textvariable=hr1, justify='center')
hour_combobox_1.place(x=310, y=80)

tk.Label(window, text='Minute').place(x=370, y=60)
minutes_combobox_1 = Combobox(window, width=3, values=[*range(0, 60)], textvariable=min1, justify='center')
minutes_combobox_1.place(x=370, y=80)

yr2 = tk.StringVar()
mon2 = tk.StringVar()
day2 = tk.StringVar()
hr2 = tk.StringVar()
min2 = tk.StringVar()

l3 = tk.Label(window, text="降落時間 : ", font=("Arial", 14))
l3.place(x=20, y=110)

year_combobox_2 = Combobox(window, width=5, values=[*range(2021, 2100)], textvariable=yr2, justify='center')
year_combobox_2.place(x=100, y=110)

month_combobox_2 = Combobox(window, width=3, values=[*range(1, 13)], textvariable=mon2, justify='center')
month_combobox_2.place(x=180, y=110)

day_combobox_2 = Combobox(window, width=4, values=[*range(1, 32)], textvariable=day2, justify='center')
day_combobox_2.place(x=240, y=110)

hour_combobox_2 = Combobox(window, width=3, values=[*range(0, 24)], textvariable=hr2, justify='center')
hour_combobox_2.place(x=310, y=110)

minutes_combobox_2 = Combobox(window, width=3, values=[*range(0, 60)], textvariable=min2, justify='center')
minutes_combobox_2.place(x=370, y=110)

b1 = tk.Button(window, text="日支計算", font=("Arial", 14), border=3, command=cal_perdiem, height=2, width=10, bg="green",
               fg='black', borderwidth=10)
b1.place(x=340, y=170)

l4 = tk.Label(window, text="日支時數 : ", font=("Arial", 14))
l4.place(x=20, y=150)
perdiem_hr = tk.Entry(window, font=("Arial", 12), state='disabled', bd=2.5, justify='center')
perdiem_hr.place(x=100, y=150)

l5 = tk.Label(window, text="日支金額 : ", font=("Arial", 14))
l5.place(x=20, y=180)
perdiem_amount = tk.Entry(window, font=("Arial", 12), state='disabled', bd=2.5, justify='center')
perdiem_amount.place(x=100, y=180)

l6 = tk.Label(window, text="飛行津貼計算", font=("Arial bold", 20))
l6.place(x=20, y=240)

flight_hours = tk.StringVar()
flight_rate = tk.StringVar()

l7 = tk.Label(window, text="津貼費率 : ", font=("Arial", 14))
l7.place(x=20, y=275)
e1 = tk.Entry(window, font=("Arial", 12), bd=2.5, textvariable=flight_rate, justify='center')
e1.place(x=100, y=275)

l8 = tk.Label(window, text="總飛時數 : ", font=("Arial", 14))
l8.place(x=20, y=310)
e2 = tk.Entry(window, font=("Arial", 12), bd=2.5, textvariable=flight_hours, justify='center')
e2.place(x=100, y=310)

b2 = tk.Button(window, text="津貼計算", font=("Arial", 14), border=3, command=cal_flight_allowance, height=2, width=10,
               bg="green",
               fg='black', borderwidth=10)
b2.place(x=340, y=335)

l8 = tk.Label(window, text="飛行津貼金額 : ", font=("Arial", 14))
l8.place(x=20, y=345)
flight_allow = tk.Entry(window, font=("Arial", 14), state='disabled', bd=2.5, justify='center')
flight_allow.place(x=120, y=345)

window.mainloop()

import tkinter as tk
import datetime

window = tk.Tk()

lbl = tk.Label(window, text="Contract Builder", fg='black', font=("Helvetica", 18), anchor="ne")
lbl.pack()
window.iconbitmap("icon.ico")

version = tk.Label(window, text="v1.01", fg='black', font=("Helvetica", 9), anchor="e")
version.pack()

# Frames

frame_first_driver = tk.Frame(master=window, width=320, height=520, relief=tk.GROOVE, borderwidth=5)
frame_first_driver.place(x=80, y=140)
frame_first_driver.columnconfigure(0, minsize=50)
frame_first_driver.rowconfigure(list(range(0, 19)), minsize=25)

frame_second_driver = tk.Frame(master=window, width=320, height=520, relief=tk.GROOVE, borderwidth=5)
frame_second_driver.place(x=420, y=140)
frame_second_driver.columnconfigure(0, minsize=50)
frame_second_driver.rowconfigure(list(range(0, 19)), minsize=25)

frame_car = tk.Frame(master=window, width=320, height=520, relief=tk.GROOVE, borderwidth=5)
frame_car.place(x=760, y=140)
frame_car.columnconfigure(1, minsize=50)
frame_car.rowconfigure(list(range(0, 19)), minsize=25)

frame_company = tk.Frame(master=window, width=320, height=200, relief=tk.GROOVE, borderwidth=5)
frame_company.place(x=80, y=670)
frame_company.columnconfigure(0, minsize=50)
frame_company.rowconfigure(list(range(0, 5)), minsize=25)

frame_abroad = tk.Frame(master=window, width=320, height=200, relief=tk.GROOVE, borderwidth=5)
frame_abroad.place(x=420, y=670)
frame_abroad.columnconfigure([0, 1], minsize=50)
frame_abroad.rowconfigure(list(range(0, 3)), minsize=25)

frame_defects = tk.Frame(master=window, width=320, height=200, relief=tk.GROOVE, borderwidth=5)
frame_defects.place(x=760, y=670)
frame_defects.columnconfigure(0, minsize=50)
frame_defects.rowconfigure(list(range(0, 2)), minsize=25)

frame_price = tk.Frame(master=window, width=320, height=280, relief=tk.GROOVE, borderwidth=5)
frame_price.place(x=1100, y=140)
frame_price.columnconfigure([0, 1], minsize=50)
frame_price.rowconfigure(list(range(0, 7)), minsize=25)

frame_other = tk.Frame(master=window, width=320, height=280, relief=tk.GROOVE, borderwidth=5)
frame_other.place(x=1100, y=370)
frame_other.columnconfigure([0, 1], minsize=50)
frame_other.rowconfigure(list(range(0, 7)), minsize=25)

# Labels of frames

label_first_driver = tk.Label(master=frame_first_driver, text="First driver", font=("Helvetica", 14))
label_first_driver.grid(row=0, column=0)

label_second_driver = tk.Label(master=frame_second_driver, text="Second Driver", font=("Helvetica", 14))
label_second_driver.grid(row=0, column=0)

label_car = tk.Label(master=frame_car, text="Car", font=("Helvetica", 14))
label_car.grid(row=0, column=0, columnspan=2)

label_company = tk.Label(master=frame_company, text="Company", font=("Helvetica", 14))
label_company.grid(row=0, column=0)

label_abroad = tk.Label(master=frame_abroad, text="Abroad travel allowed", font=("Helvetica", 14))
label_abroad.grid(row=0, column=0, columnspan=2, padx=39)

label_defects = tk.Label(master=frame_defects, text="Defects", font=("Helvetica", 14))
label_defects.grid(row=0, column=0, columnspan=2, padx=103)

label_price = tk.Label(master=frame_price, text="Fee", font=("Helvetica", 14))
label_price.grid(row=0, column=0, columnspan=2, )

label_other = tk.Label(master=frame_other, text="Other", font=("Helvetica", 14))
label_other.grid(row=0, column=0, columnspan=2, padx=102)

# First driver requisites

label_name = tk.Label(master=frame_first_driver, text="Name", font=("Helvetica", 11))
label_name.grid(row=1, column=0, sticky="s")
field_name = tk.Entry(frame_first_driver, bd=4, width=35)
field_name.grid(row=2, column=0, padx=15)

label_birth_date = tk.Label(master=frame_first_driver, text="Birth date", font=("Helvetica", 11))
label_birth_date.grid(row=3, column=0, sticky="s")
field_birth_date = tk.Entry(frame_first_driver, bd=4, width=35)
field_birth_date.grid(row=4, column=0)

label_birth_place = tk.Label(master=frame_first_driver, text="Birth place", font=("Helvetica", 11))
label_birth_place.grid(row=5, column=0, sticky="s")
field_birth_place = tk.Entry(frame_first_driver, bd=4, width=35)
field_birth_place.grid(row=6, column=0)

label_address = tk.Label(master=frame_first_driver, text="Address", font=("Helvetica", 11))
label_address.grid(row=7, column=0, sticky="s")
field_address = tk.Entry(frame_first_driver, bd=4, width=35)
field_address.grid(row=8, column=0)

label_phone = tk.Label(master=frame_first_driver, text="Phone number", font=("Helvetica", 11))
label_phone.grid(row=9, column=0, sticky="s")
field_phone = tk.Entry(frame_first_driver, bd=4, width=35)
field_phone.grid(row=10, column=0)

label_passport = tk.Label(master=frame_first_driver, text="Passport", font=("Helvetica", 11))
label_passport.grid(row=11, column=0, sticky="s")
field_passport = tk.Entry(frame_first_driver, bd=4, width=35)
field_passport.grid(row=12, column=0)

label_pass_date = tk.Label(master=frame_first_driver, text="Date of issue", font=("Helvetica", 11))
label_pass_date.grid(row=13, column=0, sticky="s")
field_pass_date = tk.Entry(frame_first_driver, bd=4, width=35)
field_pass_date.grid(row=14, column=0)

label_license = tk.Label(master=frame_first_driver, text="Driver license", font=("Helvetica", 11))
label_license.grid(row=15, column=0, sticky="s")
field_license = tk.Entry(frame_first_driver, bd=4, width=35)
field_license.grid(row=16, column=0)

label_license_date = tk.Label(master=frame_first_driver, text="Date of issue", font=("Helvetica", 11))
label_license_date.grid(row=17, column=0, sticky="s")
field_license_date = tk.Entry(frame_first_driver, bd=4, width=35)
field_license_date.grid(row=18, column=0, pady=6)

# Company requisites

label_company_name = tk.Label(master=frame_company, text="Company", font=("Helvetica", 11))
label_company_name.grid(row=1, column=0, sticky="s")
field_company_name = tk.Entry(frame_company, bd=4, width=35)
field_company_name.grid(row=2, column=0, padx=15)

label_pdv = tk.Label(master=frame_company, text="EIN", font=("Helvetica", 11))
label_pdv.grid(row=3, column=0, sticky="s")
field_pdv = tk.Entry(frame_company, bd=4, width=35)
field_pdv.grid(row=4, column=0)

# Second driver requisites

label_name_2 = tk.Label(master=frame_second_driver, text="Name", font=("Helvetica", 11))
label_name_2.grid(row=1, column=0, sticky="s")
field_name_2 = tk.Entry(frame_second_driver, bd=4, width=35)
field_name_2.grid(row=2, column=0, padx=15)

label_birth_date_2 = tk.Label(master=frame_second_driver, text="Birth date", font=("Helvetica", 11))
label_birth_date_2.grid(row=3, column=0, sticky="s")
field_birth_date_2 = tk.Entry(frame_second_driver, bd=4, width=35)
field_birth_date_2.grid(row=4, column=0)

label_birth_place_2 = tk.Label(master=frame_second_driver, text="Birth place", font=("Helvetica", 11))
label_birth_place_2.grid(row=5, column=0, sticky="s")
field_birth_place_2 = tk.Entry(frame_second_driver, bd=4, width=35)
field_birth_place_2.grid(row=6, column=0)

label_address_2 = tk.Label(master=frame_second_driver, text="Address", font=("Helvetica", 11))
label_address_2.grid(row=7, column=0, sticky="s")
field_address_2 = tk.Entry(frame_second_driver, bd=4, width=35)
field_address_2.grid(row=8, column=0)

label_phone_2 = tk.Label(master=frame_second_driver, text="Phone number", font=("Helvetica", 11))
label_phone_2.grid(row=9, column=0, sticky="s")
field_phone_2 = tk.Entry(frame_second_driver, bd=4, width=35)
field_phone_2.grid(row=10, column=0)

label_passport_2 = tk.Label(master=frame_second_driver, text="Passport", font=("Helvetica", 11))
label_passport_2.grid(row=11, column=0, sticky="s")
field_passport_2 = tk.Entry(frame_second_driver, bd=4, width=35)
field_passport_2.grid(row=12, column=0)

label_pass_date_2 = tk.Label(master=frame_second_driver, text="Date of issue", font=("Helvetica", 11))
label_pass_date_2.grid(row=13, column=0, sticky="s")
field_pass_date_2 = tk.Entry(frame_second_driver, bd=4, width=35)
field_pass_date_2.grid(row=14, column=0)

label_license_2 = tk.Label(master=frame_second_driver, text="Driver license", font=("Helvetica", 11))
label_license_2.grid(row=15, column=0, sticky="s")
field_license_2 = tk.Entry(frame_second_driver, bd=4, width=35)
field_license_2.grid(row=16, column=0)

label_license_date_2 = tk.Label(master=frame_second_driver, text="Date of issue", font=("Helvetica", 11))
label_license_date_2.grid(row=17, column=0, sticky="s")
field_license_date_2 = tk.Entry(frame_second_driver, bd=4, width=35)
field_license_date_2.grid(row=18, column=0, pady=6)

# Car requisites

label_car_type = tk.Label(master=frame_car, text="Car Model", font=("Helvetica", 11))
label_car_type.grid(row=1, column=0, sticky="s", columnspan=2)
field_car_type = tk.Entry(frame_car, bd=4, width=35)
field_car_type.grid(row=2, column=0, padx=15, columnspan=2)

label_car_number = tk.Label(master=frame_car, text="VIN", font=("Helvetica", 11))
label_car_number.grid(row=3, column=0, sticky="s", columnspan=2)
field_car_number = tk.Entry(frame_car, bd=4, width=35)
field_car_number.grid(row=4, column=0, columnspan=2)

label_rent_begin = tk.Label(master=frame_car, text="Rental start date", font=("Helvetica", 11))
label_rent_begin.grid(row=5, column=0, sticky="s", columnspan=2)
field_rent_begin = tk.Entry(frame_car, bd=4, width=20)
field_rent_begin.grid(row=6, column=0)

label_rent_end = tk.Label(master=frame_car, text="Return date", font=("Helvetica", 11))
label_rent_end.grid(row=7, column=0, sticky="s", columnspan=2)
field_rent_end = tk.Entry(frame_car, bd=4, width=35)
field_rent_end.grid(row=8, column=0, columnspan=2)

label_rent_days = tk.Label(master=frame_car, text="Number of days", font=("Helvetica", 11))
label_rent_days.grid(row=9, column=0, sticky="s", columnspan=2)
field_rent_days = tk.Entry(frame_car, bd=4, width=35)
field_rent_days.grid(row=10, column=0, columnspan=2)

label_price_km = tk.Label(master=frame_car, text="Cost/km", font=("Helvetica", 11))
label_price_km.grid(row=11, column=0, sticky="s", columnspan=2)
field_price_km = tk.Entry(frame_car, bd=4, width=35)
field_price_km.grid(row=12, column=0, columnspan=2)

label_start_place = tk.Label(master=frame_car, text="Pick-up place", font=("Helvetica", 11))
label_start_place.grid(row=13, column=0, sticky="s", columnspan=2)
field_start_place = tk.Entry(frame_car, bd=4, width=35)
field_start_place.grid(row=14, column=0, columnspan=2)

label_return_place = tk.Label(master=frame_car, text="Return place", font=("Helvetica", 11))
label_return_place.grid(row=15, column=0, sticky="s", columnspan=2)
field_return_place = tk.Entry(frame_car, bd=4, width=35)
field_return_place.grid(row=16, column=0, columnspan=2)

# Fuel

label_fuel = tk.Label(master=frame_car, text="Fuel", font=("Helvetica", 11))
label_fuel.grid(row=17, column=0, columnspan=2)

fuel_type = tk.StringVar(frame_car, "95 RON")

button_fuel_type_1 = tk.Radiobutton(frame_car, text="95 RON", variable=fuel_type, value="95 RON", relief="flat")
button_fuel_type_1.grid(row=18, column=0, pady=5)

button_fuel_type_2 = tk.Radiobutton(frame_car, text="Diesel", variable=fuel_type, value="Diesel", relief="flat")
button_fuel_type_2.grid(row=18, column=1)


# Price

label_price = tk.Label(master=frame_price, text="Base fee", font=("Helvetica", 11))
label_price.grid(row=1, column=0, sticky="s")
field_price = tk.Entry(frame_price, bd=4, width=13)
field_price.grid(row=2, column=0, padx=15)

label_tax = tk.Label(master=frame_price, text="Tax", font=("Helvetica", 11))
label_tax.grid(row=3, column=0, sticky="s")
field_tax = tk.Entry(frame_price, bd=4, width=13)
field_tax.grid(row=4, column=0)

label_payment_type = tk.Label(master=frame_price, text="Payment method", font=("Helvetica", 9))
label_payment_type.grid(row=5, column=0, sticky="s")
# field_payment_type = tk.Entry(frame_price, bd=4, width=13)
# field_payment_type.grid(row=6, column=0)

payment_type = tk.StringVar(frame_price)
payment_type.set("CARD")

menu_payment_type = tk.OptionMenu(frame_price, payment_type, "CASH", "CARD")
menu_payment_type.grid(row=6, column=0)

label_discount = tk.Label(master=frame_price, text="Discount", font=("Helvetica", 10))
label_discount.grid(row=1, column=1, sticky="s")
field_discount = tk.Entry(frame_price, bd=4, width=13)
field_discount.grid(row=2, column=1, padx=15)

label_full_price = tk.Label(master=frame_price, text="Total", font=("Helvetica", 10))
label_full_price.grid(row=3, column=1, sticky="s")
field_full_price = tk.Entry(frame_price, bd=4, width=13)
field_full_price.grid(row=4, column=1)


label_deposit = tk.Label(master=frame_price, text="Deposit", font=("Helvetica", 10))
label_deposit.grid(row=5, column=1, sticky="s")
field_deposit = tk.Entry(frame_price, bd=4, width=13)
field_deposit.grid(row=6, column=1)

# Abroad travel

abroad_travel = tk.IntVar(frame_abroad, 0)

button_abroad_1 = tk.Radiobutton(frame_abroad, text="YES", variable=abroad_travel, value=1, relief="flat")
button_abroad_1.grid(row=1, column=0, pady=25)

button_abroad_2 = tk.Radiobutton(frame_abroad, text="NO", variable=abroad_travel, value=0, relief="flat")
button_abroad_2.grid(row=1, column=1)

# Defects

defects = tk.IntVar(frame_abroad, 1)

label_defects = tk.Label(master=frame_defects, text="Defect fixation performed by client", font=("Helvetica", 10))
label_defects.grid(row=1, column=0, sticky="w")
cb_defects = tk.Checkbutton(frame_defects, text="", variable=defects, onvalue=1, offvalue=0)
cb_defects.grid(row=1, column=1, sticky="n", pady=5)

# Other

documents = tk.IntVar(frame_other, 0)

cb_documents = tk.Checkbutton(frame_other, text="Documents", variable=documents, onvalue=1, offvalue=0)
cb_documents.grid(row=1, column=0, sticky="w")

firstaid = tk.IntVar(frame_other, 0)

cb_firstaid = tk.Checkbutton(frame_other, text="First aid kit", variable=firstaid, onvalue=1, offvalue=0)
cb_firstaid.grid(row=1, column=1, sticky="w")

insurance = tk.IntVar(frame_other, 0)

cb_insurance = tk.Checkbutton(frame_other, text="Insurance", variable=insurance, onvalue=1, offvalue=0)
cb_insurance.grid(row=2, column=0, sticky="w")

triangle = tk.IntVar(frame_other, 0)

cb_triangle = tk.Checkbutton(frame_other, text="Triangle", variable=triangle, onvalue=1, offvalue=0)
cb_triangle.grid(row=2, column=1, sticky="w")

wifi_router = tk.IntVar(frame_other, 0)

cb_wifi_router = tk.Checkbutton(frame_other, text="Wi-Fi Router", variable=wifi_router, onvalue=1, offvalue=0)
cb_wifi_router.grid(row=3, column=0, sticky="w")

navigator = tk.IntVar(frame_other, 0)

cb_navigator = tk.Checkbutton(frame_other, text="Navigator", variable=navigator, onvalue=1, offvalue=0)
cb_navigator.grid(row=3, column=1, sticky="w")

domkrate = tk.IntVar(frame_other, 0)

cb_domkrate = tk.Checkbutton(frame_other, text="Jack", variable=domkrate, onvalue=1, offvalue=0)
cb_domkrate.grid(row=4, column=0, sticky="w")

lamps = tk.IntVar(frame_other, 0)

cb_lamps = tk.Checkbutton(frame_other, text="Lights", variable=lamps, onvalue=1, offvalue=0)
cb_lamps.grid(row=4, column=1, sticky="w")

spare_tire = tk.IntVar(frame_other, 0)

cb_spare_tire = tk.Checkbutton(frame_other, text="Spare tire", variable=spare_tire, onvalue=1, offvalue=0)
cb_spare_tire.grid(row=5, column=0, sticky="w")

cchair = tk.IntVar(frame_other, 0)

cb_cchair = tk.Checkbutton(frame_other, text="Child seat", variable=cchair, onvalue=1, offvalue=0)
cb_cchair.grid(row=5, column=1, sticky="w")

buster = tk.IntVar(frame_other, 0)

cb_buster = tk.Checkbutton(frame_other, text="Booster", variable=buster, onvalue=1, offvalue=0)
cb_buster.grid(row=6, column=0, sticky="w")

#date insertion


def take_date():
    current_date = datetime.datetime.now()
    field_rent_begin.delete(0, tk.END)
    field_rent_begin.insert(0, current_date.strftime("%d.%m.%Y %H:%M"))


btn_insert_date = tk.Button(frame_car, text="Today", bg="white", command=take_date, height=1, width=10)
btn_insert_date.grid(row=6, column=1)

#price insertion


def calculate_price():
    try:
        price = field_price.get()
        days = field_rent_days.get()
        cost = int(price) * int(days)
        field_full_price.delete(0, tk.END)
        field_full_price.insert(0, str(cost))
    except:
        return 0
    return cost


btn_price = tk.Button(frame_price, text="€", bg="white", font=("Helvetica", 8), command=calculate_price, height=1, width=2)
btn_price.grid(row=4, column=1, sticky="e", padx=12)

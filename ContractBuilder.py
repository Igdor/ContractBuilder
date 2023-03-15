import json
from pdfwriter import *
import os
from MainWindow import *


def get_all_data():
    data = {}
    data.update({"name": field_name.get(), "birth_date": field_birth_date.get(), "birth_place": field_birth_place.get(),
                 "address": field_address.get(), "phone": field_phone.get(), "passport": field_passport.get(),
                 "pass_date": field_pass_date.get(), "license": field_license.get(), "license_date": field_license_date.get(),
                 "name2": field_name_2.get(), "birth_date2": field_birth_date_2.get(), "birth_place2": field_birth_place_2.get(),
                 "address2": field_address_2.get(), "phone2": field_phone_2.get(), "passport2": field_passport_2.get(),
                 "pass_date2": field_pass_date_2.get(), "license2": field_license_2.get(), "license_date2": field_license_date_2.get(),
                 "car_type": field_car_type.get(), "car_number": field_car_number.get(), "rent_begin": field_rent_begin.get(),
                 "rent_end": field_rent_end.get(), "rent_days": field_rent_days.get(), "price_km": field_price_km.get(),
                 "start_place": field_start_place.get(), "return_place": field_return_place.get(), "company_name": field_company_name.get(),
                 "pdv": field_pdv.get(), "price": field_price.get(), "tax": field_tax.get(),
                 "payment_type": payment_type.get(), "discount": field_discount.get(), "full_price": field_full_price.get(),
                 "deposit": field_deposit.get(), "fuel_type": fuel_type.get(), "can_abroad": abroad_travel.get(),
                 "documents": documents.get(), "firstaid": firstaid.get(), "insurance": insurance.get(), "triangle": triangle.get(),
                 "wifi_router": wifi_router.get(), "navigator": navigator.get(), "domkrate": domkrate.get(), "lamps": lamps.get(),
                 "spare_tire": spare_tire.get(), "cchair": cchair.get(), "buster": buster.get(), "defects": defects.get()})

    return data


def save_data():
    data = get_all_data()
    js = json.dumps(data)
    file = open("template.json", "w")
    file.write(js)
    file.close()


def load_data():
    with open("template.json") as file:
        data = json.load(file)

        # first driver
        field_name.delete(0, tk.END)
        field_name.insert(0, data["name"])
        field_birth_date.delete(0, tk.END)
        field_birth_date.insert(0, data["birth_date"])
        field_birth_place.delete(0, tk.END)
        field_birth_place.insert(0, data["birth_place"])
        field_address.delete(0, tk.END)
        field_address.insert(0, data["address"])
        field_phone.delete(0, tk.END)
        field_phone.insert(0, data["phone"])
        field_passport.delete(0, tk.END)
        field_passport.insert(0, data["passport"])
        field_pass_date.delete(0, tk.END)
        field_pass_date.insert(0, data["pass_date"])
        field_license.delete(0, tk.END)
        field_license.insert(0, data["license"])
        field_license_date.delete(0, tk.END)
        field_license_date.insert(0, data["license_date"])

        # Second driver
        field_name_2.delete(0, tk.END)
        field_name_2.insert(0, data["name2"])
        field_birth_date_2.delete(0, tk.END)
        field_birth_date_2.insert(0, data["birth_date2"])
        field_birth_place_2.delete(0, tk.END)
        field_birth_place_2.insert(0, data["birth_place2"])
        field_address_2.delete(0, tk.END)
        field_address_2.insert(0, data["address2"])
        field_phone_2.delete(0, tk.END)
        field_phone_2.insert(0, data["phone2"])
        field_passport_2.delete(0, tk.END)
        field_passport_2.insert(0, data["passport2"])
        field_pass_date_2.delete(0, tk.END)
        field_pass_date_2.insert(0, data["pass_date2"])
        field_license_2.delete(0, tk.END)
        field_license_2.insert(0, data["license2"])
        field_license_date_2.delete(0, tk.END)
        field_license_date_2.insert(0, data["license_date2"])

        # Car
        field_car_type.delete(0, tk.END)
        field_car_type.insert(0, data["car_type"])
        field_car_number.delete(0, tk.END)
        field_car_number.insert(0, data["car_number"])
        field_rent_begin.delete(0, tk.END)
        field_rent_begin.insert(0, data["rent_begin"])
        field_rent_end.delete(0, tk.END)
        field_rent_end.insert(0, data["rent_end"])
        field_rent_days.delete(0, tk.END)
        field_rent_days.insert(0, data["rent_days"])
        field_price_km.delete(0, tk.END)
        field_price_km.insert(0, data["price_km"])
        field_start_place.delete(0, tk.END)
        field_start_place.insert(0, data["start_place"])
        field_return_place.delete(0, tk.END)
        field_return_place.insert(0, data["return_place"])
        fuel_type.set(data["fuel_type"])

        # Company
        field_company_name.delete(0, tk.END)
        field_company_name.insert(0, data["company_name"])
        field_pdv.delete(0, tk.END)
        field_pdv.insert(0, data["pdv"])

        # Defects
        defects.set(data["defects"])

        # Price
        field_price.delete(0, tk.END)
        field_price.insert(0, data["price"])
        field_tax.delete(0, tk.END)
        field_tax.insert(0, data["tax"])

        payment_type.set(data["payment_type"])

        field_discount.delete(0, tk.END)
        field_discount.insert(0, data["discount"])
        field_full_price.delete(0, tk.END)
        field_full_price.insert(0, data["full_price"])
        field_deposit.delete(0, tk.END)
        field_deposit.insert(0, data["deposit"])

        # Other
        documents.set(data["documents"])
        firstaid.set(data["firstaid"])
        domkrate.set(data["domkrate"])
        lamps.set(data["lamps"])
        insurance.set(data["insurance"])
        triangle.set(data["triangle"])
        spare_tire.set(data["spare_tire"])
        cchair.set(data["cchair"])
        wifi_router.set(data["wifi_router"])
        navigator.set(data["navigator"])
        buster.set(data["buster"])


def print_pdf():
    data = get_all_data()
    print_all(data)
    filename = "pdf/filled_contract.pdf"
    os.system("start " + filename)
    return "Ok"


def print_blank_pdf():
    data = get_all_data()
    print_on_blank(data)
    filename = "pdf/blank_contract.pdf"
    os.system("start " + filename)
    return "Ok"


btn_save = tk.Button(window, text="Save", bg="grey", command=save_data, height=2, width=16)
btn_save.place(x=1100, y=630)
btn_load = tk.Button(window, text="Load", bg="grey", command=load_data, height=2, width=16)
btn_load.place(x=1250, y=630)
btn_print = tk.Button(window, text="Print PDF", bg="green", command=print_pdf, height=2, width=16)
btn_print.place(x=1100, y=695)
btn_print_blank = tk.Button(window, text="Print on blank", bg="green", command=print_blank_pdf, height=2, width=16)
btn_print_blank.place(x=1250, y=695)

window.title("Contract Builder")
window.geometry("1450x900+10+20")
window.mainloop()

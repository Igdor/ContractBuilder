from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def create_pdf(data):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    can.setFont('FreeSans', 11)
    # First column
    # First driver
    can.drawString(135, 717, data["name"])
    can.drawString(135, 698, data["birth_date"])
    can.drawString(135, 680, data["birth_place"])
    if len(data["address"]) > 30:
        can.setFont('FreeSans', 9)
        can.drawString(135, 664, data["address"][:48])
        can.drawString(135, 656, data["address"][48:])
        can.setFont('FreeSans', 11)
    else:
        can.drawString(135, 660, data["address"])
    can.drawString(135, 642, data["phone"])
    can.drawString(135, 622, data["passport"])
    can.drawString(135, 602, data["pass_date"])
    can.drawString(135, 584, data["license"])
    can.drawString(135, 564, data["license_date"])
    # Second driver
    can.drawString(135, 544, data["name2"])
    can.drawString(135, 525, data["birth_date2"])
    can.drawString(135, 505, data["birth_place2"])
    if len(data["address2"]) > 30:
        can.setFont('FreeSans', 9)
        can.drawString(135, 492, data["address2"][:48])
        can.drawString(135, 484, data["address2"][48:])
        can.setFont('FreeSans', 11)
    else:
        can.drawString(135, 486, data["address2"])
    can.drawString(135, 466, data["phone2"])
    can.drawString(135, 446, data["passport2"])
    can.drawString(135, 427, data["pass_date2"])
    can.drawString(135, 410, data["license2"])
    can.drawString(135, 390, data["license_date2"])
    # Company
    can.drawString(135, 372, data["company_name"])
    can.drawString(135, 352, data["pdv"])
    # Second column
    # Car
    can.drawString(420, 717, data["car_type"])
    can.drawString(420, 698, data["car_number"])
    can.drawString(420, 680, data["rent_begin"])
    can.drawString(420, 660, data["rent_end"])
    can.drawString(420, 641, data["rent_days"])
    can.drawString(420, 621, data["price_km"])
    can.drawString(420, 545, data["start_place"])
    can.drawString(420, 525, data["return_place"])
    # Fuel
    if data["fuel_type"] == "BMB95":
        can.roundRect(344, 580, 30, 15, 8)
    else:
        can.roundRect(380, 580, 30, 15, 8)
    # Price
    can.drawString(402, 507, data["price"])
    can.drawString(402, 487, data["tax"])
    can.drawString(402, 467, data["payment_type"])
    can.drawString(520, 507, data["discount"])
    can.drawString(520, 487, data["full_price"])
    can.drawString(520, 467, data["deposit"])
    # Abroad travel
    if data["can_abroad"] == 0:
        can.roundRect(523, 428, 40, 15, 8)
    else:
        can.roundRect(523, 445, 40, 15, 8)
    # Defects
    can.drawString(325, 331, "V" if data["defects"] == 1 else "")
    # Other
    can.drawString(386, 412, "V" if data["documents"] == 1 else "")
    can.drawString(443, 412, "V" if data["firstaid"] == 1 else "")
    can.drawString(500, 412, "V" if data["domkrate"] == 1 else "")
    can.drawString(560, 412, "V" if data["lamps"] == 1 else "")
    can.drawString(386, 393, "V" if data["insurance"] == 1 else "")
    can.drawString(443, 393, "V" if data["triangle"] == 1 else "")
    can.drawString(500, 393, "V" if data["spare_tire"] == 1 else "")
    can.drawString(560, 393, "V" if data["cchair"] == 1 else "")
    can.drawString(386, 373, "V" if data["wifi_router"] == 1 else "")
    can.drawString(443, 373, "V" if data["navigator"] == 1 else "")
    can.drawString(500, 373, "V" if data["buster"] == 1 else "")
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)
    return new_pdf

def print_on_blank(data):
    new_pdf = create_pdf(data)
    output = PdfFileWriter()
    page = new_pdf.getPage(0)
    output.addPage(page)
    outputStream = open("pdf/blank_contract.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    return "Ok"

def print_all(data):

    existing_pdf = PdfFileReader(open("pdf/Contract-example.pdf", "rb"))
    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
#    page2 = existing_pdf.getPage(1) #Actual contract had a second page
    new_pdf = create_pdf(data)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
#    output.addPage(page2)
    outputStream = open("pdf/filled_contract.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    return "Ok"

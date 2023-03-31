import pytesseract
from PIL import Image
from PyPDF2 import PdfReader




option = ""
while option not in ["1","2","3"]:
    option = input("\nIndique si quiere:\n1- Leer una imágen\n2- Leer un PDF\n3- Salir\n\n")


print("\n--------------------------------------------------------------------------------")

if option == "1":
    # Image OCR reader
    image = Image.open("image.png")
    print(pytesseract.image_to_string(image))


if option == "2":
    # PDF OCR reader
    text = ""
    pageNumber = 0

    pdf = PdfReader('fullbook.pdf')
    for page in pdf.pages:
        print("---------- PAGINA " + str(pageNumber+1) + " ----------")
        page = pdf.pages[pageNumber]
        text = page.extract_text() + "\n\n\n\n"
        text = text.replace(str(pageNumber+1),"")
        print(text)
        pageNumber += 1


if option == "3":
    print("Thank you for using the app!")

print("\n--------------------------------------------------------------------------------")
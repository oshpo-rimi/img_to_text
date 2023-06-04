import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Open an image file
image = Image.open('asdfdfssdaff.jpg')

# Use PyTesseract to extract text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
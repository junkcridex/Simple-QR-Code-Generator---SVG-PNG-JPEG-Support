import os
import pyqrcode 

# Function to get URL input from user
def get_url_input():
    while True:
        url = input("@vilwahub: [ QR Code Generator ] \nPaste URL for QR generation: ")
        if url.strip():  # Check if the input is not empty after stripping whitespace
            return url

# Function to get the desired file format from user
def get_file_format():
    while True:
        print("Select the desired file format:")
        print("1. SVG")
        print("2. JPEG")
        print("3. PNG")
        choice = input("Enter the number corresponding to the desired file format: ")
        if choice in ['1', '2', '3']:
            return {'1': 'svg', '2': 'jpeg', '3': 'png'}[choice]
        else:
            print("Invalid choice. Please enter the number corresponding to the desired file format.")

# Get URL input from user
url_input = get_url_input()

# Generate QR code 
qr_code = pyqrcode.create(url_input)

# Get desired file format from user
file_format = get_file_format()

# Define the default file name
default_file_name = "myqr"

# Check if the file name already exists, if so, rename the file
file_name = f"{default_file_name}.{file_format}"
counter = 1
while os.path.exists(file_name):
    file_name = f"{default_file_name}_{counter}.{file_format}"
    counter += 1

# Save the QR code based on the selected file format
if file_format == 'svg':
    qr_code.svg(file_name, scale=8)
elif file_format == 'jpeg':
    qr_code.png(file_name, scale=8)
elif file_format == 'png':
    qr_code.png(file_name, scale=8)

print(f"QR code saved as '{file_name}'")

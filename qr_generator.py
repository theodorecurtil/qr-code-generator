import qrcode
from pathlib import Path

def generate_qr_code(url: str, filename: str) -> None:
    """
    Generate a QR code for the given URL and save it as an image file.
    
    :param url: The URL to encode in the QR code
    :param filename: The name of the file to save the QR code image as
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def main():
    while True:
        url = input("Enter the website URL (or 'q' to quit): ")
        if url.lower() == 'q':
            break
        
        filename = input("Enter the filename for the QR code image (e.g., my_qr_code.png): ")
        
        generate_qr_code(url, filename)
        print(f"QR code generated and saved as {filename}")
        print()

if __name__ == "__main__":
    main()

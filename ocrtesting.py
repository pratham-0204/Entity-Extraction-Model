import cv2
import pytesseract
import re

# Load the image
img = cv2.imread(r'D:\Aikens\student_resource\images\81aZ2ozp1GL.jpg')

# Check if the image is loaded
if img is None:
    print("Error: Could not read the image.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to make text stand out
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Extract text using pytesseract
    extracted_text = pytesseract.image_to_string(thresh)

    print("Extracted text:\n", extracted_text)

    # Define regex pattern to extract measurements
    pattern = r'(\d+\.?\d*\s?(cm|kg|g|mm|m|W|V|mA))'
    matches = re.findall(pattern, extracted_text)

    # Print extracted measurements with units
    if matches:
        print("Extracted measurements:")
        for match in matches:
            print(match)
    else:
        print("No measurements found.")

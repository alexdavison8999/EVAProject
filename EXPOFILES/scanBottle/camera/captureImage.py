import cv2
import pytesseract


def parse_image(imagePath: str) -> dict:
    """
    Returns a dictionary of strings parsed from the image
    """
    return_dict = {}

    # Load the image
    image = cv2.imread(imagePath)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to preprocess the image
    thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Apply dilation to make the text bolder
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilated = cv2.dilate(thresholded, kernel, iterations=3)

    # Apply OCR to recognize the text
    text: str = pytesseract.image_to_string(dilated)

    text_lines = text.split("\n")

    return text


if __name__ == "__main__":
    image_path = "EXPOFILES/assets/ibuprofen.jpg"

    text = parse_image(imagePath=image_path)

    print(type(text))
    print(text)

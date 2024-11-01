import easyocr
import sys

# Select the reader language
reader = easyocr.Reader(['en'])

# Read in image name as argument 1
image_name = str(sys.argv[1])
img_stem = image_name.split('.')

# First process the image using the other script, the load it
img_path = img_stem[0] + "-result.png"

# Read the image
result = reader.readtext(img_path)

# Print out the result
for (bbox, text, prob) in result:
    print(f'Text: {text}, Probability: {prob}')

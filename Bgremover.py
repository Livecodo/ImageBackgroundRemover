from rembg import remove
from PIL import Image

input_image=" "    # Input path
output_image=" "   # Output path

inp=Image.open(input_image)
output=remove(inp)
output.save(output_image)
from PIL import Image, ImageChops

# Load the images
img1 = Image.open('path/to/first/image.jpg')  # Replace with the path to your first image
img2 = Image.open('path/to/second/image.png')  # Replace with the path to your second image

# Apply the 'multiply' blend mode
result = ImageChops.multiply(img1, img2)

# Save the result
result.save('path/to/save/result.jpg')  # Replace with the desired output path and format

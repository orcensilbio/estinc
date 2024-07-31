import cv2

# Load an image from file
image_path = 'path_to_your_image.jpg'
image = cv2.imread(image_path)

# Display the loaded image
cv2.imshow('Generated Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

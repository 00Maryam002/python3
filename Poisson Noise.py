import cv2
import numpy as np


image_path = input("Please enter the image path: ")
image = cv2.imread(image_path)

if image is None:
    print("Image not found. Please enter the correct path.")
    exit()


def add_poisson_noise(image):
    noisy_image = np.copy(image)
    height, width, channels = image.shape

    # Apply Poisson noise 
    for i in range(height):
        for j in range(width):
            for c in range(channels):
                noise = np.random.poisson(image[i, j, c] / 255.0 * 256)
                noisy_image[i, j, c] = np.clip(noise, 0, 255)
    
    return noisy_image

# Function to remove noise using a simple median filter
def remove_noise(image):
    denoised_image = np.copy(image)
    height, width, channels = image.shape

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            for c in range(channels):
                # Take a 3x3 neighborhood of the current pixel
                neighborhood = [
                    image[i-1, j-1, c], image[i-1, j, c], image[i-1, j+1, c],
                    image[i, j-1, c], image[i, j, c], image[i, j+1, c],
                    image[i+1, j-1, c], image[i+1, j, c], image[i+1, j+1, c]
                ]
                # Apply median filtering
                denoised_image[i, j, c] = np.median(neighborhood)

    return denoised_image

# Apply Poisson noise
noisy_poisson = add_poisson_noise(np.copy(image))

# Remove noise 
denoised_poisson = remove_noise(noisy_poisson)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Poisson Noise", noisy_poisson)
cv2.imshow("Denoised Poisson", denoised_poisson)

cv2.waitKey(0)
cv2.destroyAllWindows()



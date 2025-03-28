import numpy as np
from PIL import Image

# Flips the image horizontally and vertically
def flip_image(image_array):
    image_array = image_array[:,::-1]  # Flip left-to-right
    image_array = image_array[::-1]  # Flip up-to-down
    return image_array
np.add(1, 2)
# Adds random noise to the image
def add_noise(image_array, intensity=25):
    noise = np.random.randint(-intensity, intensity, image_array.shape, dtype=np.int16)  # Generate random noise
    noisy_image = np.clip(image_array + noise, 0, 255).astype(np.uint8)  # Add noise and clip values to 0-255
    return noisy_image

# Brightens a specific channel (e.g., red, green, blue) by a fixed value
def brighten_channels(image_array, channel_index, value=40):
    image_array[:, :, channel_index] = np.clip(image_array[:, :, channel_index] + value, 0, 255)  # Brighten and clip
    return image_array

# Applies a black mask to a rectangular region in the image
def apply_mask(image_array, x, y, width, height):
    image_array[y:y+height, x:x+width] = [0, 0, 0]  # Set pixel values in the region to black
    return image_array

# Main function to perform all image manipulations
def main():
    image = Image.open("birds.jpg")  # Load the image using PIL
    image_array = np.array(image)  # Convert the image to a NumPy array

    # Perform image manipulations
    image_array = flip_image(image_array)  # Flip the image
    image_array = add_noise(image_array, intensity=25)  # Add random noise
    image_array = brighten_channels(image_array, channel_index=0, value=40)  # Brighten the red channel
    height, width, _ = image_array.shape  # Get image dimensions
    image_array = apply_mask(image_array, x=width//2 - 50, y=height//2 - 50, width=100, height=100)  # Apply a mask

    modified_image = Image.fromarray(image_array)  # Convert NumPy array back to PIL image
    modified_image.save("modified_birds.jpg")  # Save the modified image
    print("Image manipulations completed and saved as 'modified_birds.jpg'.")

if __name__ == "__main__":
    main()  # Run the main function
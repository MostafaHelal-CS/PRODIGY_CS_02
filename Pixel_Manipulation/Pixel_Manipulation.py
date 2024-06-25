from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def show_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

def encrypt_image(input_path, key):
    # Open the input image
    image = Image.open(input_path)
    pixels = np.array(image)
    
    # Encrypt the pixels by applying XOR with the key
    encrypted_pixels = pixels ^ key
    
    # Create an encrypted image
    encrypted_image = Image.fromarray(encrypted_pixels)
    
    return image, encrypted_image

def decrypt_image(encrypted_image, key):
    # Convert encrypted image to numpy array
    pixels = np.array(encrypted_image)
    
    # Decrypt the pixels by applying XOR with the key
    decrypted_pixels = pixels ^ key
    
    # Create a decrypted image
    decrypted_image = Image.fromarray(decrypted_pixels)
    
    return decrypted_image

# Example usage
key = 123  # Example key for XOR operation
original_image, encrypted_image = encrypt_image('input_image.png', key)
decrypted_image = decrypt_image(encrypted_image, key)

# Display the images
show_image(original_image, 'Original Image')
show_image(encrypted_image, 'Encrypted Image')
show_image(decrypted_image, 'Decrypted Image')

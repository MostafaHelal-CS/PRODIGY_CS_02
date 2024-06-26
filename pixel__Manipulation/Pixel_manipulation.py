from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open the input image
    image = Image.open(input_path)
    pixels = np.array(image)
    
    # Encrypt the pixels by applying XOR with the key
    encrypted_pixels = pixels ^ key
    
    # Create an encrypted image
    encrypted_image = Image.fromarray(encrypted_pixels)
    
    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    # Open the encrypted image
    image = Image.open(input_path)
    pixels = np.array(image)
    
    # Decrypt the pixels by applying XOR with the key
    decrypted_pixels = pixels ^ key
    
    # Create a decrypted image
    decrypted_image = Image.fromarray(decrypted_pixels)
    
    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

key = 123  # Example key for XOR operation
encrypt_image('input_image.png', 'encrypted_image.png', key)
decrypt_image('encrypted_image.png', 'decrypted_image.png', key)

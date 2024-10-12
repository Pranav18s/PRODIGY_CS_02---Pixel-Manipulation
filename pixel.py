from PIL import Image
import os

# Encrypt Image
def encrypt_image(input_image_path, output_image_path):
    print(f"Encrypting the file: {input_image_path}")
    
    if not os.path.exists(input_image_path):
        print(f"Error: The file '{input_image_path}' does not exist.")
        return

    image = Image.open(input_image_path)
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            # Shift pixel values for encryption
            pixels[i, j] = ((r + 50) % 256, (g + 50) % 256, (b + 50) % 256)

    image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

# Decrypt Image
def decrypt_image(encrypted_image_path, output_image_path):
    print(f"Decrypting the file: {encrypted_image_path}")
    
    if not os.path.exists(encrypted_image_path):
        print(f"Error: The file '{encrypted_image_path}' does not exist.")
        return

    image = Image.open(encrypted_image_path)
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            # Reverse the encryption by subtracting the value
            pixels[i, j] = ((r - 50) % 256, (g - 50) % 256, (b - 50) % 256)

    image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

if __name__ == "__main__":
    input_image = "C:\\Users\\prana\\OneDrive\\Desktop\\python project\\PUBG.png"
    encrypted_image = "encrypted_PUBG.png"
    decrypted_image = "decrypted_PUBG.png"

    # Encrypt the image
    encrypt_image(input_image, encrypted_image)

    # Decrypt the image (to check if we get the original back)
    decrypt_image(encrypted_image, decrypted_image)

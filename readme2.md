PRODIGY_CS_02 - Pixel Manipulation - Image Encryption & Decryption 🖼️🔐
This Python project implements a simple image encryption and decryption mechanism using the XOR operation. The process involves manipulating the pixel values of an image to encrypt or decrypt it based on a key. This is a fast and reversible encryption method, making it easy to securely transform and restore images. 📸

✨ Features
XOR Encryption/Decryption: Efficient, reversible encryption method using XOR operation 🔄.
Customizable Key: Allows the use of an integer key between 0 and 255 for encryption 🔑.
Image Compatibility: Handles image manipulation using the Pillow and NumPy libraries.
🚀 How It Works
XOR Encryption 🔒
The encryption process uses the XOR (exclusive OR) operation on the pixel values of an image.
Reversible: The same operation is used for both encryption and decryption. Applying XOR with the same key again will restore the original image.
Key Constraints 🔑
The key must be an integer between 0 and 255, as it is used to generate a key array.
This key array is then applied to the pixel values of the image, making it essential for both encryption and decryption.
Image Handling 🖼️
The code assumes the input image is in a format compatible with the Pillow library.
The image is converted into a NumPy array for pixel manipulation.
After encryption/decryption, the image is saved back.
🛠️ How to Use
Clone the repository:

bash
Copy code
git clone https://github.com/Pranav18s/python-project-encryption.git

Install dependencies:

bash
Copy code
pip install pillow
pip install numpy
Run the script:

bash
Copy code
python PixelManipulation.py

🔑 Example Usage
plaintext
Copy code
Do you want to encrypt or decrypt an image? (e/d): e
Enter the path to the image: C:\Users\prana\OneDrive\Desktop\python project\PUBG.png
Enter a numeric key for encryption/decryption (0-255): 123
Encryption complete. Encrypted image saved as 'encrypted_image.png'.

👤 Author
pranav s
www.linkedin.com/in/pranav-s-85b106269

📄 License
This project is licensed under the MIT License.


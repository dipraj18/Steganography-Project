import cv2
import os
import string

# Ensure correct image path
image_path = r"C:\Users\yashp\OneDrive\Desktop\New folder (2)\Stenography-main\Stenography-main\mypic.jpg.jpg"
img = cv2.imread(image_path)

# Check if the image was loaded correctly
if img is None:
    print("Error: Image not found. Please check the file path.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Dictionaries for encoding/decoding
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Variables for pixel coordinates
m = 0
n = 0
z = 0

# Encoding the message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = (n + 1) % img.shape[0]
    m = (m + 1) % img.shape[1]
    z = (z + 1) % 3

# Save encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")

# Decryption
message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")

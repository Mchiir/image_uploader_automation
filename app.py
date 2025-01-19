import os
import time
import subprocess
import logging
import signal
import sys

# logging set up
logging.basicConfig(filename='upload_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Program information
program_name = "MQTT Image Uploader"
author = "Mr. Mchrispin"
version = "1.0.0"
welcome_message = f"{program_name} - Version {version}\nAuthor: {author}"

# The folder to monitor for new images
image_folder = './src'

# The folder to move uploaded images to
uploaded_folder = './dist'

# The upload URL and key attribute
upload_url = 'https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php'
key_attribute = 'imageFile'

# Program initialization log
logging.info(welcome_message)
print(welcome_message)
print("Program is starting...")

# Check if the folders exist, if not, create them
if not os.path.exists(image_folder):
    os.makedirs(image_folder)
    logging.info(f"Created the source folder: {image_folder}")
    print(f"Created the source folder: {image_folder}")
    
if not os.path.exists(uploaded_folder):
    os.makedirs(uploaded_folder)
    logging.info(f"Created the destination folder: {uploaded_folder}")
    print(f"Created the destination folder: {uploaded_folder}")

# Signal handler to capture graceful exit (Ctrl+C)
def signal_handler(sig, frame):
    print("\nGoodbye! Program is stopping...")
    logging.info("Program stopped by user.")
    sys.exit(0)

# Set up signal handler for graceful exit
signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        # Checking the image folder for new files
        for filename in os.listdir(image_folder):
            if filename.endswith('.jpg'):
                image_path = os.path.join(image_folder, filename)
                
                # Waiting 30 seconds before uploading
                time.sleep(30)
                
                # Uploading each image using curl
                command = f'curl -X POST -F "{key_attribute}=@{image_path}" {upload_url}'
                subprocess.run(command, shell=True)
                
                # Checking if file already exists in the 'uploaded' folder
                uploaded_path = os.path.join(uploaded_folder, filename)
                if os.path.exists(uploaded_path):
                    # Creating a unique filename by appending a number or timestamp
                    base, ext = os.path.splitext(filename)
                    timestamp = time.strftime("%Y%m%d-%H%M%S")
                    filename = f"{base}_{timestamp}{ext}"
                    uploaded_path = os.path.join(uploaded_folder, filename)
                    
                # Moving the uploaded image to the 'uploaded' folder
                os.rename(image_path, uploaded_path)
                
                # Log the success message
                logging.info(f"The file {filename} has been successfully uploaded.")
                
        # Waiting for 1 second before checking the folder again
        time.sleep(1)

except KeyboardInterrupt:
    # This block is triggered when the user stops the program with Ctrl+C
    print("\nGoodbye! Program is stopping...")
    logging.info("Program stopped by user.")
import paho.mqtt.client as mqtt
import base64

def on_connect(client, userdata, flags, rc):
    print("\nConnected with result code " + str(rc) +"\n")
    client.subscribe("/instructor_gabriel") # Listen for messages from Instructor Gabriel

def on_message(client, userdata, msg):
    print("\nInstructor Gabriel: " + str(msg.payload.decode())) # Display text messages from the instructor
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Connect to the MQTT broker
client.connect("82.165.97.169", 1883, 60)
# Start the network loop
client.loop_start()
student_topic = "/mugisha_chrispin" # put your topic here as full names, small_letters no spaces

while True:
    option = input("\nType 'text' to send a message or 'image' to send a picture: ").strip().lower()
    
    if option == "text":
        message = input("\nEnter your message: ")
        client.publish(student_topic, message) # Send text message to the instructor
    elif option == "image":
        image_path = input("\nEnter the image file path (e.g., 'picture.jpg'): ").strip()
 
        try:
        # Read and encode the image in Base64
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            
            # Send image as Base64 string
            client.publish(student_topic, f"image:{encoded_string}")
            print("\nImage sent successfully!")

        except Exception as e:
            print(f"\nError sending image: {e}")

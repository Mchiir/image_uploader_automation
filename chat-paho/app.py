import paho.mqtt.client as mqtt

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # client.subscribe("/instructor_gabriel")  # Listen for messages from Instructor Gabriel
    client.subscribe("/jovin")  # Listen for messages from Instructor Gabriel

# Callback when a message is received from the subscribed topic
def on_message(client, userdata, msg):
    print("Instructor Gabriel: " + str(msg.payload.decode()))  # Display messages from the Instructor

# Create an MQTT client instance
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker (Add the broker address inside the quotes)
client.connect("82.165.97.169", 1883, 60)

# Start the network loop
client.loop_start()

# Infinite loop to send messages
while True:
    message = input("You: ")
    client.publish("/jovin", message)  # Send message to the instructor

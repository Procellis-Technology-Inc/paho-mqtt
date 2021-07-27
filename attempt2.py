import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("procellis/messages")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))

username = input("What's your username? ")
client = mqtt.Client(username)
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io")
client.loop_start()

while True:
    message = input("What is your message: ")
    client.publish("procellis/messages", username+ ": " + message)
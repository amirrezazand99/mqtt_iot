# python 3.6

import random
import time
import json

from paho.mqtt import client as mqtt_client


broker = '45.149.77.235'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'ali'
# password = 'javadi'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQyMzQyNjI1LCJpYXQiOjE2Mzk3NTA2MjUsImp0aSI6IjIzZjc2NDMwZjdkMzRhMzdhMTk5NmUxZWY4OWU5MjAyIiwidXNlcl9pZCI6MX0.YWg8SwiDGeDMG50d3LBVPkXu0n92prxaWePsipy2Nzg", "ID_of_device":"d", "labeled":"e", "parameter1":"test_2"}
        msg = json.dumps(msg)
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()

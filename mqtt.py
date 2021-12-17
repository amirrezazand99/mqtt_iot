
import random

from paho.mqtt import client as mqtt_client
import requests
import json

broker = '45.149.77.235'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'




def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        js = json.loads(msg.payload.decode())
        token = js['token']
        dic = {}
        for k in js.keys():
            if k != 'token':
                dic[k] = js[k]
        request = requests.post('https://ioitiran.ir/api/Devices/CreateRecord/',
                                data=json.dumps(dic),
                                headers={'Authorization': f"Bearer {token}",
                                         'Content-Type': 'application/json'})

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()

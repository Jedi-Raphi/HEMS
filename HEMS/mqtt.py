from paho.mqtt import client as mqtt_client
import password
import json
confi = {}
new_data_flag = False
power = 0.0
goal = 0.0
new_goal_flag = False

def connect_mqtt(broker_ip ,broker_port, conf):
    def on_connect(client, userdata, flags, reason_code, properties):
        if reason_code == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {reason_code}")

    client = mqtt_client.Client(
        client_id="HEMSv1",
        callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2,
    )
    # For paho-mqtt 1.x, instantiate without callback_api_version:
    # client = mqtt_client.Client(client_id)

    client.username_pw_set(password.Mqtt_user,password.Mqtt_password)
    client.on_connect = on_connect
    client.connect(broker_ip, broker_port)
    global confi
    confi = conf
    client.loop_start()
    return client


def subscribe(client: mqtt_client.Client, topic):
    def on_message(client, userdata, msg):
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        topic = msg.topic
        payload = msg.payload.decode()

        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            data = payload
        
        #print(f'value : {data} sur {topic}')
        if topic == f"shellies/{confi["Grid_power"]["ID"]}/emeter/0/power":
            try:

                #print(f'conso : {data} W')
                global new_data_flag, power
                power = float(data)
                new_data_flag = True
            except ValueError:
                print("Value error")

        if topic == f"HEMS/setings/goal":
            try:

                #print(f'conso : {data} W')
                global goal, new_goal_flag
                goal = float(data)
                new_goal_flag = True
            except ValueError:
                print("Value error")


    client.on_message = on_message
    client.subscribe(topic)

def publish(client: mqtt_client.Client, topic, msg):
    status = client.publish(topic,msg)
    return status

    




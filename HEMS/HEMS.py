import json
import mqtt
import password
import time 

from simple_pid import PID



try:
    with open('conf.json', 'r') as conf_file:
        conf = json.load(conf_file)

except FileNotFoundError:
    print("File not found!")
except json.JSONDecodeError:
    print("Invalid JSON format!")
except Exception as e:
    print(f"An error occurred: {str(e)}")



#start mqtt
broker_ip = conf["MQTT_object_broker"]["IP"]
broker_port = conf["MQTT_object_broker"]["Port"]
broker_method = conf["MQTT_object_broker"]["Method"]
client = mqtt.connect_mqtt(broker_ip,broker_port, conf)


mqtt.subscribe(client, f'shellies/{conf["Grid_power"]["ID"]}/emeter/0/power')
#mqtt.subscribe(client, f'shellies/#')
mqtt.subscribe(client, f'HEMS/setings/goal')



def Distri(surplus):
    


    perc = surplus / float(conf["Devices"]["Water_tank1"]["Max_consuption"])
    mqtt.publish(    client, f'HEMS/{conf["Devices"]["Water_tank1"]["ID"]}/actions/pwr_perc', perc)





surplus_capa = 0.0
for i in conf["Devices"]:
    surplus_capa = surplus_capa + float(conf["Devices"][i]["Max_consuption"])
print(surplus_capa)




pid = PID(0.3, 0.3, 0, 0, 1, (0,surplus_capa))


while True:
    if mqtt.new_data_flag == True:

        mqtt.new_data_flag = False
        surplus = pid(mqtt.power)
        print(f'grid : {mqtt.power} W et {surplus} W envoyées sur triac')

        Distri(surplus)
    


    if mqtt.new_goal_flag == True:
        pid.setpoint = mqtt.goal
        pid.integral = 0
        print(f"new goal : {pid.setpoint}")
        mqtt.new_goal_flag = False

    



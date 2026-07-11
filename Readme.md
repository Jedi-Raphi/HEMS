# Quick start guide
```bash
git clone https://github.com/Jedi-Raphi/HEMS.git
cd HEMS
```

```bash
mosquiito_passwd mosquitto/config/passwords.txt hems
```
> enter new password
>
> complete your info in docker-compose.yml
```docker-compose
    environment:
      - MQTT_USER=hems
      - MQTT_PASSWORD=your_password
```
## setup HEMS/config.json
<details>
  <summary>if your mqtt broker is not on the same machine</summary>
  
 then insert the mqtt brokuer ip
```jsonc
  "MQTT_object_broker": {
    "IP": "mosquitto_broker", //change this to your ip
    "Port": 1883,
    "Method": "MQTT"
  },
```
</details>
enter details for grid power mesurements

```jsonc
 "Grid_power": {
    "Type": "Shelly",
    "Gen": 1,
    "Method": "MQTT",
    "ID": "shellyem-34945470F287", //put the mqtt mame of the shelly
    "Chanel": 0
  },
```

in `"Devices": {}`
```jsonc
setups yours devices 
 "Water_tank1": {
      "Type": "water_tank", //what should be considered not used now
      "Sheme": "triac", //not used now
      "ID":"Water_tank1", //mqtt name
      "Max_consuption":"2000", //set the device max power consuption
      "Method": "MQTT",  //not used now
      "Sensor": {
        "Water_temp": {
          "Absolute_max": 80,  //stop heating after this temps
          "Max": 70, //don't heat after this temp exept if surplus high
          "Min": 40, //try not to get under
          "Absolute_min": 30 //use gid to heat untill min temp
        }
      },
      "Actions": {
        "Heating": true
      },
      "Need": {
        "Activate": { //not configure now but will force another device to power on
          "Water_pump1": true
        }
      }
    }
```
# start HEMS
```bash
docker compose up --build
```

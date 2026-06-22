from djitellopy import Tello
fly = Tello()
fly.connect()
print(fly.get_battery())
print(fly.VS_UDP_IP)
print(fly.VS_UDP_PORT)
print(fly.TIME_BTW_COMMANDS)
print(fly.RESPONSE_TIMEOUT)
fly.end()
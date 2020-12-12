from config import token, my_id
import time
import API

while True:
    API.send_u(my_id, token)
    API.del_u(my_id)
    time.sleep(5400)

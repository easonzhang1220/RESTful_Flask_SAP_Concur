import uuid
import requests
import time

for i in range(220):
    id_ = uuid.uuid4()
    requests.post("http://localhost:5000/items/{}".format(id_))
    time.sleep(0.03)

# import uuid
# from locust import HttpLocust, TaskSet, task
#
#
# class MyTaskSet(TaskSet):
#     @task
#     def random_post_id(self):
#         ess already in use: ('', 8089)
#         self.client.post("/items/{}".format(id))
#
# class MyLocust(HttpLocust):
#     task_set = MyTaskSet
#     min_wait = 100
#     max_wait = 100

import uuid,requests, time
for i in range(220):
    id = uuid.uuid4()
    requests.post("http://localhost:5000/items/{}".format(id))
    time.sleep(0.03)




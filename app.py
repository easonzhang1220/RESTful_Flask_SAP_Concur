from flask import Flask
from flask_restful import Api, Resource
import datetime

app = Flask(__name__)
api = Api(app)


# items example:
# [{ item:{ id: 123, timestamp: 2016-01-01T23:01:01.000Z } }]
# data stack
items = []

def time_diffent(timestring, time_now):
    """
    :param self:
    :param timestring:
    :return:
    """
    a = datetime.datetime.strptime(time_now[:-1], '%Y-%m-%dT%H:%M:%S.%f')
    b = datetime.datetime.strptime(timestring[:-1], '%Y-%m-%dT%H:%M:%S.%f')
    return (a - b).seconds


class Items(Resource):
    def post(self, id):
        if id in [item["item"]["id"] for item in items]:
            return "the ID \'{}\' already exists.".format(id), 400

        item = {
            "item": {
                "id": id,
                "timestamp": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z"
            }
        }

        items.append(item)
        return item, 201


class All_itmes(Resource):
    def get(self):
        global items

        if len(items) > 100:
            time_now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z"
            lastest_100_items = items[-100:]
            # clean data and generate return items
            items = [item for item in items[:-100] if time_diffent(item["item"]["timestamp"], time_now) < 2]
            items += lastest_100_items
            return items

        return items


api.add_resource(All_itmes, "/items")
api.add_resource(Items, "/items/<string:id>")

app.run(debug=True)

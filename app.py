
from flask import Flask
from flask_restful import Api
from routes import EventList
from routes import EventList, Event


BASE_URL = '/api'

app = Flask(__name__)

api = Api(app)
api.add_resource(EventList, f'{BASE_URL}/Events')
api.add_resource(Event, f'{BASE_URL}/Events/<event_id>')


if __name__ == '__main__':
    app.run(debug=True)

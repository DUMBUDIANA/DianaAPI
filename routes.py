from flask_restful import Resource


class EventList(Resource):
    def get(self):
        return {'hello':  'from eventlist'}


class Event(Resource):
    def get(self):
        return {'hello': 'from event {event_id}'}

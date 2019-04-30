from eventbrite import Eventbrite
import settings


def connect():
    return Eventbrite(settings.API_KEY)


def bt614_user():
    return connect().get_user()


def user_id():
    return settings.ID

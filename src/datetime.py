from datetime import datetime
import pytz


class DateTime:
    __DEFAULT_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(self, timezone='Europe/Kiev'):
        self.timezone = pytz.timezone(timezone)

    def get_current_time(self, format=__DEFAULT_FORMAT):
        now = datetime.now(self.timezone)

        return now.strftime(format)

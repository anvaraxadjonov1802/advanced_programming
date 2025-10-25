from datetime import datetime


class TimeProvider:
    def now_hour(self):
        """Ayni damdagi soatni oladi"""
        return datetime.now().hour


class Greeter:
    def __init__(self, time_provider: TimeProvider):
        self.time_provider = time_provider

    def greet(self, name):
        hour = self.time_provider.now_hour()
        if 5 <= hour < 12:
            return f"Good Morning, {name}!"
        elif 12 <= hour < 18:
            return f"Good Afternoon, {name}!"
        else:
            return f"Good Evening, {name}!"
    
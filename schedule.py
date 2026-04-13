from datetime import datetime
from time import sleep

class ScheduleBuilder:

    def __init__(self):
        self.week_schedule = "Output: \n"
        self.date = ""
        self.title = ""

    def timestamp_gen(self):
        """
        year: YYYY - 2026
        month: M - 4, 12
        day: D - 1, 30
        hour: H - 1, 13
        minute: m - 1, 60
        stream: title - Offline, Yapping & Playing Game
        """
        if self.title == "Offline":
            self.week_schedule = self.week_schedule + f"<t:{int(datetime(self.date.year, self.date.month, self.date.day).timestamp())}:D> - {self.title}" + "\n"
        else:
            self.week_schedule = self.week_schedule + f"<t:{int(datetime(self.date.year, self.date.month, self.date.day, self.date.hour, self.date.minute).timestamp())}:F> - <t:{int(datetime(self.date.year, self.date.month, self.date.day, self.date.hour, self.date.minute).timestamp())}:R> - {self.title}" + "\n"




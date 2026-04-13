from schedule import ScheduleBuilder
from pyscript import web, when
from datetime import datetime, timedelta

sb = ScheduleBuilder()

inc = 1

start_date = None

@when("click", "#continue")
def input(event):
    global inc
    sb.date = start_date
    while inc <= 7:
        sb.title = web.page[f"title{inc}"].value
        if sb.title != "Offline":
            web_time = datetime.strptime(web.page[f"time{inc}"].value, "%H:%M").time()
            sb.date = datetime.combine(sb.date.date(), web_time)
        sb.timestamp_gen()
        sb.date += timedelta(days=1)
        inc += 1
    inc = 1
    web.page["output"].innerText = sb.week_schedule
    sb.week_schedule = "Output: \n"

@when("click", "#submit")
def submit_date(event):
    global start_date
    start_date = datetime.strptime(web.page["week"].value, "%Y-%m-%d")
    web.page["feedback"].innerText = f"{start_date} has been set as starting date"

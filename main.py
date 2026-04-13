from schedule import ScheduleBuilder
from pyscript import web, when
from datetime import datetime

sb = ScheduleBuilder()

inc = 0

@when("click", "#continue")
def input(event):
    global inc
    if inc < 6:
        time_input = web.page["time-input"].value
        title_input = web.page["title-input"].value
        sb.title = title_input
        if title_input == "Offline":
            sb.date = datetime.strptime(time_input, "%m-%d-%Y")
        else:
            sb.date = datetime.strptime(time_input, "%m-%d-%Y %H:%M")
        sb.timestamp_gen()
        inc += 1
        web.page["response"].innerText = f"{time_input} has been added to the schedule message"
    elif inc == 6:
        time_input = web.page["time-input"].value
        title_input = web.page["title-input"].value
        sb.title = title_input
        if title_input == "Offline":
            sb.date = datetime.strptime(time_input, "%m-%d-%Y")
        else:
            sb.date = datetime.strptime(time_input, "%m-%d-%Y %H:%M")
        sb.timestamp_gen()
        button = web.page["continue"]
        button.innerText = "Print Final Schedule"
        web.page["response"].innerText = f"{time_input} has been added to the schedule message"
        inc = 7
    else:
        output = web.page["output"]
        output.innerText = sb.week_schedule

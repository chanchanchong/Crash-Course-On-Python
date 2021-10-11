# lists of tasks
# - process the events to create a report
# - sort the list of events chronologically
# - we'll store the data in a dictionary of sets (it will be use to keep track of who's logged in where)
# - function that generates the dictionary
# - function that prints the dictionary

# problem statement = we want to write a script that generates a report of which users
# are logged in to which machines at that time.

class Event:
    date = ""
    type = ""
    user = ""
    machine = ""


def get_event_date(event):
    return event.date


# process
def current_users(events):
    events.sort(key=get_event_date())
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines


def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


def main():
    events = []


if __name__ == '__main__':
    main()

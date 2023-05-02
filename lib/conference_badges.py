def badge_maker(name):
    return 'Hello, my name is ' + name + '.'

def batch_badge_creator(names):
    return ["Hello, my name is " + name + "." for name in names]

def assign_rooms(names):
    i = 1
    room_assignment = []
    for name in names:
        room_assignment.append("Hello, " + name + "! You'll be assigned to room " + str(i) + "!")
        i += 1
    return room_assignment

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
       print(room)
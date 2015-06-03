
def convert_to_seconds(time):
    time_list = time.split(':')
    new_time = int(time_list[0]) * 3600 + int(time_list[1]) * 60 + int(time_list[2])
    return new_time

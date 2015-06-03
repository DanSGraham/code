#A Program to convert standard time format " HH:MM:SS" to seconds
#BY Daniel Graham

def convert_to_seconds(time):
    """converts the time string into seconds which can then be used by the graph"""
    time_list = time.split(':')
    new_time = int(time_list[0]) * 3600 + int(time_list[1]) * 60 + int(time_list[2])
    return new_time

def convert_to_regtime(time_in_seconds):
    reg_time_hours = time_in_seconds/3600
    reg_time_minutes = (time_in_seconds - reg_time_hours*3600)/60
    reg_time_seconds = time_in_seconds - reg_time_hours*3600 - reg_time_minutes*60
    reg_time = '%02d:%02d:%02d' % (reg_time_hours, reg_time_minutes, reg_time_seconds)
    return reg_time

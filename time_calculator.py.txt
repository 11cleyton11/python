clock = {
    'hour': [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'meridian': ['AM','PM'],
    'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
    'added_day': 0,
}

def add_time(start, duration, day = ''):
    
    if duration == '0:00':
        if day == '':        
            if clock['added_day'] == 0:
                return f'{start}'
            elif clock['added_day'] == 1:
                return f'{start} (next day)'
            else:
                return f'{start} ({clock["added_day"]} days later)'
        else:
            if clock['added_day'] == 0:
                return f'{start}, {day}'
            elif clock['added_day'] == 1:
                return f'{start}, {day} (next day)'
            else:
                return f'{start}, {day} ({clock["added_day"]} days later)'

    hour = ''
    added_hour = ''
    start_day = ''

    for char in start:
        if char.isdigit():
            hour += char
        else:
            break
    for char in duration:
        if char.isdigit():
            added_hour += char
        else:
            break
    hour_index = (int(hour) + 12) % 12 

    minute = start[-5] + start[-4]
    added_minute = duration[-2] + duration[-1]

    if start[-2] == 'A':
        meridian = clock['meridian'][0]
    elif start[-2] == 'P':
        meridian = clock['meridian'][1]

    if day != '':
        day = day.capitalize()

    for d in clock['day']:
        if d == day:
            start_day = d
            day_index = clock['day'].index(start_day)

    if int(added_minute) > 0:
        total_minute = int(minute) + int(added_minute)
        if total_minute >= 60:
            minute = str(total_minute - 60)
            if len(minute) == 1:
                minute = '0' + minute
            added_hour = str(int(added_hour) + 1)
        else:
            minute = str(total_minute)
        added_minute = '00'
            
    if int(added_hour) > 0:
        hour_index = (int(hour) + 13) % 12
        added_hour = str(int(added_hour) - 1)
        if hour_index == 0 and start[-2] == 'A':
            start = f'{clock["hour"][hour_index]}:{minute} PM'
        elif hour_index == 0 and start[-2] == 'P':
            start = f'{clock["hour"][hour_index]}:{minute} AM'
            clock['added_day'] += 1
            if start_day != '':
                start_day = clock['day'][(day_index + 8) % 7]
        else:
            start = f'{clock["hour"][hour_index]}:{minute} {meridian}'
        duration = f'{added_hour}:{added_minute}'
        return add_time(start, duration, start_day)

print(add_time('11:55 AM', '3:12', 'satUrday'))
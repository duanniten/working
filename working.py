import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if  matches := re.search(
                            r'([0-9][0-9]?):?([0-9][0-9]?)?.+(AM|PM) +to +'
                            r'([0-9][0-9]?):?([0-9][0-9]?)?.+(AM|PM)',
                            s):
        hour_start, minute_strart, meridiem_start, hour_fin, minute_fin, meridiem_fin = matches.groups() 

        if 0 < int(hour_start) > 12 or 0 < int(hour_fin) > 12:
            raise ValueError
        
        if minute_strart!= None and int(minute_strart) > 59:
            raise ValueError
        
        if minute_fin!= None and int(minute_fin) > 59:
            raise ValueError

        if meridiem_start == 'PM':
            hour_start = int(hour_start) + 12
        else:
            hour_start = int(hour_start)

        if meridiem_fin == 'PM':
            hour_fin = int(hour_fin) + 12
        else:
            hour_fin = int(hour_fin)

        if minute_strart == None:
            minute_strart = '0'
        
        if minute_fin == None:
            minute_fin = '0'

        if hour_start == 12 and meridiem_start == 'AM':
            hour_start = 0
        
        if hour_fin == 12 and meridiem_fin == 'AM':
            hour_fin = 0

        minute_strart = int(minute_strart)
        minute_fin = int(minute_fin)

        final_string = f'{hour_start:02}:{minute_strart:02} to {hour_fin:02}:{minute_fin:02}'

        return final_string
    else:
        raise ValueError

if __name__ == "__main__":
    main()
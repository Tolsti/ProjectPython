def format_duration(seconds):
    if seconds == 0:
        return 'now'

    years = ((seconds // 3600) // 24) // 365
    days = (seconds // 3600) // 24 % 365
    hours = (seconds // 3600) % 24
    minutes = seconds // 60 % 60
    seconds = seconds % 60
    result = str()

    if years > 0:
        result += '{} year'.format(years)
        if years > 1:
            result += 's'
        if days > 0 or hours > 0 or minutes > 0:
            result += ', '

    if days > 0:
        result += '{} day'.format(days)
        if days > 1:
            result += 's'
        if hours > 0 or minutes > 0:
            result += ', '

    if hours > 0:
        result += '{} hour'.format(hours)
        if hours > 1:
            result += 's'
        if minutes > 0 and seconds != 0:
            result += ', '
        if minutes > 0 and seconds == 0:
            result += ' and '

    if minutes > 0:
        result += '{} minute'.format(minutes)
        if minutes > 1:
            result += 's'
        if seconds > 0:
            result += ' and '

    if seconds > 0:
        result += '{} second'.format(seconds)
        if seconds > 1:
            result += 's'

    return result


print(format_duration(0), "now")

print(format_duration(1) == "1 second")
print(format_duration(62) == "1 minute and 2 seconds")
print(format_duration(120) == "2 minutes")
print(format_duration(3600) == "1 hour")
print(format_duration(3662) == "1 hour, 1 minute and 2 seconds")

print(format_duration(15731080) == "182 days, 1 hour, 44 minutes and 40 seconds")
print(format_duration(132030240) == "4 years, 68 days, 3 hours and 4 minutes")
print(format_duration(205851834) == "6 years, 192 days, 13 hours, 3 minutes and 54 seconds")
print(format_duration(253374061) == "8 years, 12 days, 13 hours, 41 minutes and 1 second")
print(format_duration(242062374) == "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")
print(format_duration(101956166) == "3 years, 85 days, 1 hour, 9 minutes and 26 seconds")
print(format_duration(33243586) == "1 year, 19 days, 18 hours, 19 minutes and 46 seconds")

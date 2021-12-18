def add_time(start, duration, starting_day = None):
  """
  Passed a start time, a duration in hours:minutes, calculates what the end time is in standard time
  If the starting day is passed, will also determine the day of the week.
  """

  day_of_week_dict = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
  }

  # convert back
  day_of_week_dict_inverse = {
    0: "Monday",
    1:"Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
  }

  if starting_day != None:
    starting_day = starting_day.lower()
    starting_day = starting_day.capitalize()
    day_of_the_week = day_of_week_dict.get(starting_day)

  # split time from PM/AM
  arr = start.split()
  meridian = arr[1]
  # assign pm and am assign time then split hours and minutes
  start_time = arr[0].split(":")
  start_hours = int(start_time[0])
  start_minutes = int(start_time[1])

  # convert start_time appropriately for calcs later
  if meridian == "PM":
    if start_hours != 12:
      start_hours += 12

  dur_time = duration.split(":")
  dur_hours = int(dur_time[0])
  dur_minutes = int(dur_time[1])

  total_hours = start_hours + dur_hours
  total_minutes = start_minutes + dur_minutes

  # does hour get carried over?
  if total_minutes >= 60:
    total_minutes -= 60
    total_hours += 1

  # does PM -> AM and vice versa need changed? Also calculates days passed.
  days = 0
  if total_hours >= 24:
    days = total_hours // 24
    total_hours = total_hours % 24
  if total_hours >= 12:
    if total_hours == 12:
      meridian = "PM"
    else:
      total_hours -= 12
      meridian = "PM"
  else:
    meridian = "AM"
  if total_hours == 0:
    total_hours = 12
    meridian = "AM"
  
  # days later calc
  if days == 0:
    days_later = ""
  if days == 1:
    days_later = " (next day)"
  if days > 1:
    days_later = f" ({days} days later)"
    
  # Determine what day of the week it is if needed.
  if starting_day != None:
    ending_day = day_of_week_dict_inverse.get((days + day_of_the_week) % 7)

  # convert total minutes to str and add 0 if ness
  total_minutes = str(total_minutes)
  if len(total_minutes) != 2:
    total_minutes = "0" + total_minutes

  if starting_day == None:
    new_time = str(total_hours) + ":" + total_minutes + " " + meridian + days_later
  else:
    new_time = str(total_hours) + ":" + total_minutes + " " + meridian + ", " + ending_day + days_later

  return new_time

# Test case Examples
# print(add_time("3:30 PM", "2:12"))
# print(add_time("11:55 AM", "3:12"))
# print(add_time("9:15 PM", "5:30"))
# print(add_time("3:30 PM", "2:12"))
# print(add_time("8:16 PM", "466:02"))
# print(add_time("3:30 PM", "2:12", "Monday"))
# print(add_time("8:16 PM", "466:02", "tuesday"))

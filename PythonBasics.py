
yourname = input("Dude! What is your name? ")
minutes = int(input("Enter minutes: "))
hours = minutes / 60
minutes_remaining = 0
print("FYI" , yourname, ":", minutes, "minute(s) is", minutes/60, "hour(s) or", hours, "hour(s) plus", minutes_remaining, "minute(s).")

print("FYI {} : {} minute(s) is {:.3f} hour(s) or {} hour(s) plus {} minute(s)."
      .format(yourname, minutes, minutes/60, hours, minutes_remaining))
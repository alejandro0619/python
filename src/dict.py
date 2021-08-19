# seems pretty similar to Javascript's objects:

month_convertion = {
  "Jan": "January",
  "Feb": "February",
  "Mar": "March",
  "Apr": "April",
  "May": "May",
  "Jun": "June",
  "Jul": "July",
  "Aug": "August",
  "Sep": "September",
  "Oct": "October",
  "Nov": "November",
  "Dec": "December"
  }

#Access:
print(month_convertion["Aug"])
# Using get, if no element was found, I can pass a default data:
print(month_convertion.get("Luv", "Luvember"))
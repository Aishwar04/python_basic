from calendar import month


monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",   # keys in dictionary have to be unique
    "Apr": "April",   # keys can also be numeric
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions)

print(monthConversions.get("Dec"))


print(monthConversions.get("Luv","Not a valid key"))  # specify a default output when key is not in dictionary

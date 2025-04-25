from datetime import datetime
date_str1 = "2005-8-13"
date_str2 = "2025-04-24"
date1 = datetime.strptime(date_str1, "%Y-%m-%d")
date2 = datetime.strptime(date_str2, "%Y-%m-%d")
difference = date2 - date1
print("Number of days between the two dates:", difference.days)

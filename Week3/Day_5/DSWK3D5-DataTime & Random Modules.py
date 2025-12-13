# Telling time with python.
import datetime
from datetime import datetime
now=datetime.now()
print(now)

#Getting today's date only.
from datetime import date
today=date.today()
print(f"Today's",today)

#Calculating days to an event (practice).
from datetime import date
current_Day=date.today()
event=date(2025,12,25)

difference=event-current_Day
print(difference.days,"days to Christmas!")
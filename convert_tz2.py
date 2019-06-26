# adapted from: https://stackoverflow.com/questions/4770297/convert-utc-datetime-string-to-local-datetime

from datetime import datetime
from dateutil import tz

# METHOD 1: Hardcode zones:
tz_utc = tz.gettz("UTC")
tz_eastern = tz.gettz("America/New_York")

dt = datetime.now()

# Tell the datetime object that it's in UTC time zone since
# datetime objects are 'naive' by default
dt_utc = dt.replace(tzinfo=tz_utc)
print("UTC:", dt_utc)

# Convert time zone
dt_eastern = dt.astimezone(tz_eastern)
print("EASTERN:", dt_eastern)

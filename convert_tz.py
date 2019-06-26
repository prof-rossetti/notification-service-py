# adapted from:
#  + https://github.com/sdispater/pendulum
#  + https://stackoverflow.com/a/41352275/670433
#  + https://github.com/sdispater/pendulum/issues/29#issuecomment-241231221
#  + https://pendulum.eustace.io/
#  + https://github.com/sdispater/pendulum/search?q=New_York&unscoped_q=New_York

from datetime import datetime
import pendulum # FYI THIS IS A PACKAGE AND NEEDS TO BE IMPORTED

# STEP 1: WE'VE GOT A TWEET'S CREATED_AT ATTRIBUTE,
# ... WHICH IS A TIMEZONELESS DATETIME
# ... BUT WE KNOW ITS IN UTC BECAUSE OF THE TWEET'S ______ ATTRIBUTE
dt = datetime.now() # (timezoneless)
print("---------")
print("DATETIME (ZONELESS)", dt) #> 2019-06-25 01:37:00.769187

# STEP 2: CONVERT THE DATETIME INTO A PENDULUM TIME INSTANCE,
# ... WHICH WILL MAKE TIMEZONE CONVERSIONS EASIER
# ... WE CAN BE COMFORTABLE CONVERTING TO UTC WHEN THE TWEET'S ______ ATTRIBUTE
pi = pendulum.instance(dt)
print("---------")
print("PENDULUM INSTANCE (UTC)", pi) #> 2019-06-25T01:37:00.769187+00:00
print(pi.tz) #> Timezone('UTC')

# STEP 3: CONVERT TO A DIFFERENT TIMEZONE
eastern = pi.in_timezone("America/New_York")
print("---------")
print("PENDULUM INSTANCE (EASTERN)", eastern) #> 2019-06-24T21:37:00.769187-04:00
print(eastern.tz) #> Timezone('America/New_York')


#> ---------
#> DATETIME (ZONELESS) 2019-06-25 01:52:08.062544
#> ---------
#> PENDULUM INSTANCE (UTC) 2019-06-25T01:52:08.062544+00:00
#> Timezone('UTC')
#> ---------
#> PENDULUM INSTANCE (EASTERN) 2019-06-24T21:52:08.062544-04:00
#> Timezone('America/New_York')

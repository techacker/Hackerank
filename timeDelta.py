# Time Delta
# When users post an update on social media,such as a URL, image, status update etc.,
# other users in their network are able to view this new post on their news feed.
# Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
# Since sometimes posts are published and viewed in different time zones, this can be confusing.
# You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
# Day dd Mon yyyy hh:mm:ss +xxxx
# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

# Sample timestamps:
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

import datetime

def time_delta(t1, t2):
    # Use strptime(date_string, format) method
    # datetime.datetime.strptime('TimeStamp String', 'format string')
    t1 = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return int(abs(datetime.timedelta.total_seconds(t1 - t2)))

n = int(input())
for _ in range(n):
    t1 = input()
    t2 = input()
    delta = time_delta(t1, t2)
    print(delta)

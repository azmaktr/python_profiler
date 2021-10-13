import datetime
from time import process_time
from dateutil import parser

dt_now = datetime.datetime.now()
SAMPLES = 100000
dt_objs = []
dt_unix_objs = []

for i in range(SAMPLES):
    dt = dt_now + datetime.timedelta(seconds=(i+1)*60)

    dt_objs.append(dt.replace(tzinfo=None).isoformat(
        timespec="milliseconds") + "Z")

    dt_unix_objs.append(datetime.datetime.timestamp(dt))


def profiler(method, list):
    t = process_time()
    method(list)
    print(f"took: {process_time() - t}")


def is_tz_aware(dt):
    dt = dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None


def profile_iso_parse(list):
    for l in list:
        datetime.datetime.fromisoformat(l.replace("Z", ""))


def profile_dateutil(list):
    for l in list:
        parser.parse(l)


def profile_strptime(list):
    for l in list:
        datetime.datetime.strptime(l, "%Y-%m-%dT%H:%M:%S.%fZ")


def profile_iso_parse(list):
    for l in list:
        datetime.datetime.fromisoformat(l.replace("Z", ""))


def profile_unix_timestamp(list):
    for l in list:
        datetime.datetime.fromtimestamp(l)


print(f"profiling over {SAMPLES} datetime strings")

print(f"Profiling {profile_iso_parse.__name__}:")
profiler(profile_iso_parse, dt_objs)


print(f"Profiling {profile_strptime.__name__}:")
profiler(profile_strptime, dt_objs)


print(f"Profiling {profile_dateutil.__name__}:")
profiler(profile_dateutil, dt_objs)

print(f"Profiling {profile_unix_timestamp.__name__}:")
profiler(profile_unix_timestamp, dt_unix_objs)

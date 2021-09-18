import datetime
from time import process_time
from dateutil import parser

dt_now = datetime.datetime.now()
SAMPLES = 10000
dt_objs = []

for i in range(SAMPLES):
    dt_objs.append((dt_now + datetime.timedelta(seconds=(i+1)*60)
                    ).replace(tzinfo=None).isoformat(timespec="milliseconds") + "Z")


def profiler(method, list):
    t = process_time()
    method(list)
    print(f"took: {process_time() - t}")


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


print(f"Profiling {profile_iso_parse.__name__}:")
profiler(profile_iso_parse, dt_objs)


print(f"Profiling {profile_strptime.__name__}:")
profiler(profile_strptime, dt_objs)


print(f"Profiling {profile_dateutil.__name__}:")
profiler(profile_dateutil, dt_objs)

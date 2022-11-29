def date_to_JD(year: int, month: int, day: int, time=0) -> float:
    a = int((14 - month) / 12)
    y = (year + 4800 - a)
    m = month + 12 * a - 3
    h = int(time)
    minutes = int(time - h) * 60
    sec = ((time - h) * 60 - int(minutes)) * 60
    jdn = day + int((153 * m + 2) / 5) + 365 * y + int(y / 4) - int(y / 100) + int(y / 400) - 32045
    jd = jdn + (h - 12) / 24 + minutes / 1440 + sec / 86400

    return jd






def time_dec(t:str)->float:
    t = t.split(":")
    a = float(t[0])
    b = float(t[1])
    c = float(t[2])
    d = (b/60)
    e = (c/3600)
    k = a+d+e
    return k


def time_sep(str_sep:float)-> str:
    a = int(str_sep)
    d = str_sep - a
    e = d * 60
    r = int(e)
    s = e - r
    g = (s * 60)
    str_time = str(a) + ":" + str(r) + ":" + str(g)
    return str_time





def UT_to_GST (year:int, month:int, day:int, ut_time:float) -> float:
    JD = date_to_JD(year, month, day)
    S = JD - 2451545
    T = S/36525
    T0 = 6.697374558 + (2400.051336 * T) + (0.000025862 * (T**2))
    T0 = T0 % 24
    if T0 < 0:
        T0 = T0 + 24
    star_time = ut_time * 1.002737909
    GST = T0 + star_time
#     GST is Greenwhich sideral time
    if GST > 24:
        GST = GST - 24
    return GST

# print(time_sep(UT_to_GST(1980,4,22,time_dec("14:36:51.67"))))

# GST is Greenwich sidereal time

def GST_to_LST(GST, longitude:float)->float:
    longitude = longitude/15
    LST = GST + longitude
    if LST > 24:
        LST = LST - 24
    elif LST < 0:
        LST = LST + 24

    return LST


# LT is local time, UT is Universal time

def LT_to_UT(lt_time:float, time_zone:float )-> float:
    lt_time = lt_time - time_zone
    if lt_time > 24:
        lt_time = lt_time - 24
    elif lt_time < 0:
        lt_time + 24
    return lt_time
# print(time_sep(LT_to_UT(time_dec("12:25:35"), 6)))


# next function


def UT_to_LT(ut_time:float, time_zone:float )->float:
    ut_time = ut_time + time_zone
    if ut_time > 24:
        ut_time = ut_time - 24
    elif ut_time < 0:
        ut_time + 24
    return ut_time


# next function

def LT_to_GST(year:int, month:int, day:int, time:float, time_zone:float) ->float:
    UT = time - time_zone
    if UT < 0:
        day = day - 1
        UT = UT + 24
    elif UT > 24:
        day = day + 1
        UT = UT - 24
    GST = UT_to_GST(year,month, day, UT)
    return GST
# print((LT_to_GST(2022, 11, 22, time_dec("18:37:00"), 6)))

def LT_to_LST(year:int, month:int, day:int, LT:float, time_zone:float, longitute:float) ->float:
    ut_time = LT - time_zone
    if ut_time > 24:
        ut_time = ut_time - 24
        day = day + 1
    elif ut_time < 0:
        ut_time + 24
        day = day - 1
    GST = UT_to_GST(year, month, day, ut_time)
    LST = GST + longitute/15
    if LST > 24:
        LST = LST - 24
    elif LST < 0:
        LST + 24
    return LST

print(time_sep(LT_to_LST(2022, 11, 22, time_dec("18:37:00"), 6, 76.97)))








































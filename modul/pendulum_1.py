import pendulum
now=pendulum.now()
print("now",now)
london=pendulum.now("Europe/London")
print('----'*10)
print("london",london)
print('----'*10)
print("yesterday",pendulum.yesterday())
print("today",pendulum.today())
print("tomorrow",pendulum.tomorrow())
print('----'*10)
dt1=pendulum.datetime(2020,7,28)
dt2=pendulum.datetime(2020,12,22)
d=dt1.diff_for_humans(dt2)
d2=dt2-dt1
print("in_hours",d2.in_hours())
print("in_months",d2.in_months())
print("in_days",d2.in_days())
print("for_humans",d)
print('----'*10)
dt3= pendulum.datetime(2020, 7, 28, 15,30)
print("cookie",dt3.to_cookie_string())
print("iso",dt3.to_iso8601_string())
print("rfc",dt3.to_rfc822_string())




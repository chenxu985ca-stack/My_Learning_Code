# 天气预报出行
distance_mi = 10
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True

if distance_mi == 0:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif 1 < distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
else:
    print(False)

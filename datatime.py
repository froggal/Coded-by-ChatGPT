import datetime

# 현재 시간 구하기
now = datetime.datetime.now()

# 현재 연도, 월, 일 출력
print("Current Year:", now.year)
print("Current Month:", now.month)
print("Current Day:", now.day)

# 현재 요일 출력
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Current Day of Week:", days[now.weekday()])

# 현재 시간 출력
print("Current Time:", now.time())

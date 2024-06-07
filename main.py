import time
import random

say = ["Не буди лихо, пока оно тихо",
        "Друг познается в беде",
        "В тихом омуте черти водятся",
        "В гостях хорошо, а дома лучше"]

print("na start")
time.sleep(2)
print("wnimanie")
time.sleep(1)
print("marsh")
now_say = say[random.randint(0, 3)]
print(now_say)
start_time = time.time()
input = input()
finish_time = time.time()
print(len(now_say), "simvolov za", (finish_time-start_time), "\n eto ", (len(now_say)/(finish_time-start_time)), "simvolov v sek")
errors = 0
for x in range(0, len(now_say)):
    if x < len(input):
        if input[x] == now_say[x]:
            pass
        else:
            errors += 1
            print('vi napisali "', input[x], '" vmesto "', now_say[x], '"')
    else:
            print('vi napisali " - "', 'vmesto "', now_say[x], '"')
if errors == 0:
    print("vi ne oshiblis")

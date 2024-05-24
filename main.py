import re
import time

start_time = time.time()

pattern = re.compile('\d: (.*) killed (.*) by (.*)|:\d+ (InitGame)')

for line in open('qgames.log', 'r'):
    result = pattern.findall(line)
    if result and result[0]:
        # print(result[0])
        killer, victim, mean, initGame = result[0]

        if initGame:
            # print("initGame")
            continue

        # print(f'killer: {killer}, victim: {victim}, mean: {mean}')

print("--- %s seconds ---" % (time.time() - start_time))
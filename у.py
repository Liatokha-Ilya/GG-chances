import numpy as np
result = []
foggy, happy = 0, 0

for i in range(10000000):
    score = np.random.rand()
    foggy_win = int(score > 0.78)
    foggy = foggy + foggy_win
    happy = happy + 1 - foggy_win

    if (happy == 3) or (foggy == 3):
        if happy == 3:
            result.append(0)
        else:
            result.append(1)
        foggy, happy = 0, 0

print(np.array(result).mean())
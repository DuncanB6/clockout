
import random

from main import set_to_current_time

for _ in range(100):
    current_angle = random.randint(0, 4319)
    real_angle = random.randint(0, 4319)
    print(current_angle, real_angle)
    diff, direction = set_to_current_time(None, current_angle, real_angle)
    print(diff, direction)
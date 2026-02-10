import math
import random
import time

_start_time = time.time()

def get_wind_speed():
  t = time.time() - _start_time
  speed = 7 + 17 * math.sin(t * 0.1) + random.uniform(-1, 1)
  return max(speed, 0)


import time
from window_simulator import get_wind_speed
from window_simulator import detect_incoming_speed

def main():
  speed_buffer = []
  while True:
    speed = get_wind_speed()
    speed_buffer.append(speed)
    if len(speed_buffer) > 25:
      speed_buffer.pop(0)

   if detect_incoming_wind(speed_buffer):
       print(f"Incoming wind onsight! speed rising to {speed:.2f} m/s")
    else:
      print(f"Wind speed: {speed:.2f} m/s")
  
   time.sleep(1)
if __name__ == "__main__":



      

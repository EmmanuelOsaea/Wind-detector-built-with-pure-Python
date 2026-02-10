def detect_incoming_wind(speed_buffer, thresold=14):
if len(speed_buffer) < 7:
   return False
 recent = speed_buffer[-7:]
 rising = all (a < b for a, b in zip(recent, recent[1:]))
 near_thresold = recent[-1] >= thresold * 0.8
return rising and near_thresold

def smooth_data(data, alpha =0.1):
  smoothed = []
  last = data[0]
  for point in data:
     last = last + alpha * (point - last)
   smoothed.append(last) 
return smoothed

import unittest
from wind_detector import detect_incoming_wind

class TestWindDetector(unittest.TestCase);
def test_detect_incoming_wind(self);
rising_data = [7, 9, 11, 13, 15]
self.assertTrue(detect_incoming_wind(rising_data, thresold=14))

non_rising_data = [7, 8, 7, 9, 10]
self assertFalse(detect_incoming_wind(non_rising_data, thresold=14))

if __name__ == "__main__":
  unittest.main()

import unittest

class BowlingTest(unittest.TestCase):

     def test_result_of_no_pins(self):
        test_result = calculate_total_score("")
        print(self._testMethodName)
        print(test_result)
        assert test_result == 0

     def test_result_of_one_roll(self):
        test_result = calculate_total_score("1")
        print(self._testMethodName)
        print(test_result)
        assert test_result == 1

     def test_result_of_double_roll(self):
         test_result = calculate_total_score("71")
         print(self._testMethodName)
         print(test_result)
         assert test_result == 8

     def test_result_of_strike(self):
          test_result = calculate_total_score("X")
          print(self._testMethodName)
          print(test_result)
          assert test_result == 10
          
     def test_result_of_spare(self):
          test_result = calculate_total_score("5/")
          print(self._testMethodName)
          print(test_result)
          assert test_result == 10

     def test_dash_is_zero(self):
          test_result =  calculate_total_score("-2")
          print(self._testMethodName)
          print(test_result)
          assert test_result == 2

     def test_series_of_two_scores(self):
          test_result = calculate_total_score("45 -7")
          print(self._testMethodName)
          print(test_result)
          assert test_result == 16
          
     def test_series_of_five_scores(self):
          test_result = calculate_total_score("8- 42 9- 16 44")
          print(self._testMethodName)
          print(test_result)
          assert test_result == 38

     def test_series_of_ten_scores(self):
          test_result = calculate_total_score("6- 53 -2 81 34 61 18 33 52 -1")
          print(self._testMethodName)
          print(test_result)
          assert test_result == 62
    
     # @unittest.skip
     def test_series_including_strike(self):
          test_result = calculate_total_score("41 X -6")
          print(self._testMethodName)
          print(test_result)
          assert test_result == 27
     
     @unittest.skip
     def test_series_including_two_strikes(self):
          test_result = calculate_total_score("43 X X 71 42") 
          print(self._testMethodName)
          print(test_result)
          assert test_result == 59

     @unittest.skip
     def test_series_including_spare(self):
          test_result = calculate_total_score("35 4/ 34")
          print(self._testMethodName)
          print(test_result)
          assert test_result == 28

     @unittest.skip
     def test_series_including_final_round_bonuses(self):
          print(self._testMethodName)
          assert calculate_total_score("00 00 00 5/3") == 13
          assert calculate_total_score("00 00 00 5/X") == 20
          assert calculate_total_score("00 00 00 XX7") == 27
          assert calculate_total_score("00 00 00 X34") == 17
          assert calculate_total_score("00 00 00 X7/") == 20
          assert calculate_total_score("00 00 00 X7/") == 30

# - - - - - - - -

def calculate_frame_score(score):
     score = score.replace("-", "0")
     if len(score) == 0:
               return 0
     if score == "X":
               return 10
     if len(score) == 1 and score.isnumeric():
               return int(score)
     elif score.isnumeric():
          this_frame_score = 0
          for digit in score:
                    this_frame_score += int(digit)
          return this_frame_score
     if len(score) == 2 and score[1] == "/":
          return 10


def calculate_total_score(series):
     list_of_frames = series.split()
     total_score = 0

     for frame in list_of_frames:
          total_score += calculate_frame_score(frame)
     
     for (index, score) in enumerate(list_of_frames[:-1]):
          next_roll = list_of_frames[index + 1][0]
          next_frame_score = calculate_frame_score(list_of_frames[index + 1])
          if score == 'X':
                total_score += next_frame_score
          if score.endswith('/'):
                total_score += next_roll
                
     return total_score

if __name__ == '__main__':
     unittest.main()
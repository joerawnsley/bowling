import unittest

class BowlingTest(unittest.TestCase):

     def check_result_and_print_output(self, input_string, expected_total):
          test_result = calculate_total_score(input_string)
          print(self._testMethodName)
          print("should be", expected_total)
          print("returned", test_result)
          assert test_result == expected_total
  
     def test_result_of_one_roll(self):
          self.check_result_and_print_output("1", 1)
          
     def test_result_of_double_roll(self):
          self.check_result_and_print_output("71", 8)
     
     def test_result_of_strike(self):
          self.check_result_and_print_output("X", 10)
     
     def test_result_of_spare(self):
          self.check_result_and_print_output("5/", 10)
     
     def test_dash_is_zero(self):
          self.check_result_and_print_output("-2", 2)
     
     def test_series_of_two_scores(self):
          self.check_result_and_print_output("45 -7", 16)
     
     def test_series_of_five_scores(self):
          self.check_result_and_print_output("8- 42 9- 16 44", 38)
     
     def test_series_of_ten_scores(self):
          self.check_result_and_print_output("6- 53 -2 81 34 61 18 33 52 -1", 62)
     
     def test_series_including_strike(self):
          self.check_result_and_print_output("41 X -6", 27)

     def test_series_including_two_strikes(self):
          self.check_result_and_print_output("43 X X 71 42", 59)
     
     @unittest.skip
     def test_series_including_spare(self):
          self.check_result_and_print_output("35 4/ 34", 28)
     
     @unittest.skip
     def test_series_including_final_round_bonuses(self):
          self.check_result_and_print_output("00 00 00 5/3", 0)
     
     @unittest.skip
     def test_series_including_final_round_bonuses(self):
          self.check_result_and_print_output("00 00 00 5/X", 0)
     
     @unittest.skip
     def test_series_including_final_round_bonuses(self):
          self.check_result_and_print_output("00 00 00 XX7", 0)
     
     @unittest.skip
     def test_series_including_final_round_bonuses(self):
          self.check_result_and_print_output("00 00 00 X34", 0)
     
     @unittest.skip
     def test_series_including_final_round_bonuses(self):
          self.check_result_and_print_output("00 00 00 X7/", 0)
     
     @unittest.skip
     def test_series_including_final_round_bonuses(self):
          self.check_result_and_print_output("00 00 00 XXX", 0)

class Frame:
     def __init__(self, scores, index):
          self.frameTotal = calculate_frame_total(scores)
          self.firstRoll = scores[0]
          self.index = index
           

def calculate_frame_total(score):
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

def convert_scorestring_to_frames(scorestring):
     frame_strings = scorestring.split()
     frame_objects = []
     for i, frame in enumerate(frame_strings):
          frame_objects.append(Frame(frame, i))
     print(frame_objects)
     return frame_objects
          


def calculate_total_score(series):
     list_of_frames = series.split()
     total_score = 0

     for frame in list_of_frames:
          total_score += calculate_frame_total(frame)
     
     for (index, score) in enumerate(list_of_frames[:-1]):
          next_roll = list_of_frames[index + 1][0]
          next_frame_score = calculate_frame_total(list_of_frames[index + 1])
          if score == 'X':
                total_score += next_frame_score
          if score.endswith('/'):
                total_score += next_roll
                
     return total_score

if __name__ == '__main__':
     unittest.main()
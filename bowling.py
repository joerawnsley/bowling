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
     
     # @unittest.skip
     def test_series_including_strike(self):
          self.check_result_and_print_output("41 X -6", 27)

     @unittest.skip
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
          self.firstRoll = scores[0]
          self.index = index
          self.scores = scores.replace("-", "0")
          self.is_a_strike = False
          
     def total(self):
          if len(self.scores) == 0:
               return 0
          if self.scores == "X":
                    self.is_a_strike = True
                    return 10
          if len(self.scores) == 1 and self.scores.isnumeric():
                    return int(self.scores)
          elif self.scores.isnumeric():
               this_frame_score = 0
               for digit in self.scores:
                         this_frame_score += int(digit)
               return this_frame_score
          if len(self.scores) == 2 and self.scores[1] == "/":
               return 10
     
     def first_roll(self, scores):
          pass


def convert_scorestring_to_frames(score_series):
     frame_strings = score_series.split()
     frame_objects = []
     for i, frame in enumerate(frame_strings):
          frame_objects.append(Frame(frame, i))
     print(frame_objects)
     return frame_objects
          


def calculate_total_score(score_series):
     list_of_frames = convert_scorestring_to_frames(score_series)
     total_score = 0

     for frame in list_of_frames[:-1]:
          total_score += frame.total()
          if frame.is_a_strike:
               total_score += list_of_frames[frame.index + 1].total()
     
     total_score += list_of_frames[-1].total()
     
     return total_score

if __name__ == '__main__':
     unittest.main()
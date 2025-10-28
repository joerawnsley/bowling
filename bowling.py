import unittest

class BowlingTest(unittest.TestCase):

     def test_result_of_no_pins(self):
        print(self._testMethodName)
        assert calculate_total_score("") == 0

     def test_result_of_one_roll(self):
        print(self._testMethodName)
        assert calculate_total_score("1") == 1

     def test_result_of_double_roll(self):
         print(self._testMethodName)
         assert calculate_total_score("71") == 8
     # originally, I wrote this test with 4 and 7, adding up to 11, checked it failed, and wrote the code to pass the test. I then realised that it isn't possible to get a 4 and a 7 so I changed the test to 7 and 1. It still passed but I think this goes against the TDD principle because the test should fail the first time I run it?

     def test_result_of_strike(self):
          print(self._testMethodName)
          assert calculate_total_score("X") == 10
          
     def test_result_of_spare(self):
          print(self._testMethodName)
          assert calculate_total_score("5/") == 10

     def test_dash_is_zero(self):
          print(self._testMethodName)
          print(self._testMethodName)
          assert calculate_total_score("-2") == 2

     def test_series_of_two_scores(self):
          print(self._testMethodName)
          assert calculate_total_score("45 -7") == 16
          
     
     
     # after passing the above test, I wanted to add some more tests to check if it still works for a longer series of say three scores or ten scores. If I add these tests now, I would expect them to pass - if they do, is it bad that they passed straight away, and how do I avoid that situation?

     def test_series_of_five_scores(self):
          print(self._testMethodName)
          assert calculate_total_score("8- 42 9- 16 44") == 38

     def test_series_of_ten_scores(self):
          print(self._testMethodName)
          assert calculate_total_score("6- 53 -2 81 34 61 18 33 52 -1") == 62
    
     # the above tests passed first time as expected

     def test_series_including_strike(self):
          print(self._testMethodName)
          assert calculate_total_score("41 X -6") == 27
     
     

     # another question is should it be one test at a time? I wrote this test and the nexttest at the same time, then realised that perhaps I should do them one at a time to follow TDD principles

     def test_series_including_two_strikes(self):
          print(self._testMethodName)
          assert calculate_total_score("43 X X 71 42") == 59

     def test_series_including_spare(self):
          print(self._testMethodName)
          assert calculate_total_score("35 4/ 34") == 28


# - - - - - - - -

carry_over = 0

def calculate_frame_score(score):
     score = score.replace("-", "0")
     global carry_over
     if len(score) == 0:
               return 0
     if score == "X":
               this_frame_score = carry_over + 10
               carry_over = 10
               return this_frame_score
     if len(score) == 1 and score.isnumeric():
               carry_over = int(score)
               return int(score)
     if len(score) == 2 and score.isnumeric():
          this_frame_score = 0
          for digit in score:
                    this_frame_score += int(digit)
          carry_over = this_frame_score
          return this_frame_score
     if len(score) == 2 and score[1] == "/":
          this_frame_score = 10
          carry_over = this_frame_score
          return this_frame_score


def calculate_total_score(series):
     list_of_frames = reversed(series.split())
     total_score = 0
     global carry_over
     carry_over = 0
     for frame in list_of_frames:
          total_score += calculate_frame_score(frame)
          print("carry over", carry_over)
     print("total score", total_score)
     return total_score

if __name__ == '__main__':
     unittest.main()
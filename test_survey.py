import unittest
from survey import AnonymousSurvey

class TestAnnymousSurvey(unittest.TestCase):
    """Tests or the class 'AnonymousSurvey'."""

    def setUp(self):
        question = "What was your first language?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Hebrew']

    def test_store_single_response(self):
        """Test that a single repsonse is stored."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
       

    def test_store_three_responses(self):
        """Test if you save 3 responses."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:   
            self.assertIn(response, self.my_survey.responses)
        

if __name__ == '__main__':
    unittest.main()
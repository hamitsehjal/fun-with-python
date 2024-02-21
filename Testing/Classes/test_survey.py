import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will available to all the test functions"""
    language_survey=AnonymousSurvey("Which language do you speak?")
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly"""
    response = "English"
    language_survey.store_responses(response)
    assert response in language_survey.responses 

def test_store_three_responses(language_survey):
    """Test that three responses are stored properly"""
    responses=['English','Hindi','Punjabi']
    for response in responses:
        language_survey.store_responses(response) 
    
    for response in responses:
        assert response in language_survey.responses

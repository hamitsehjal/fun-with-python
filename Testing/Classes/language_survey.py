from survey import AnonymousSurvey

# Define a question, and make a survey
question = "what language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the Questions, and store the responses
language_survey.show_question()
print("Enter 'q' at any time to QUIT")

while True:
    response = input("Language:\t")
    if response == 'q':
        break
    language_survey.store_responses(response)

language_survey.show_results()

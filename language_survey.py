from survey import AnonymousSurvey

# Define a question and make a survey
question = "What is your first language?"
my_survey = AnonymousSurvey(question)

# Show the question and store response to it
my_survey.show_question()
print(f"Enter 'q' anytime to quit.")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
# Show responses
print(f"\nThanks for participating in our survey.")
my_survey.show_result()
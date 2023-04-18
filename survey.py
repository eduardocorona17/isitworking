class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    def __init__(self, question):
        "Store a question and prepareto store responses."
        self.question = question
        self.responses = []

    def show_question(self):
        """Show survey question."""
        print(self.question)
    
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_result(self):
        """Show results from the survey."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
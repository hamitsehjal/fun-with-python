"""Class that helps administer anonymours surveys"""

class AnonymousSurvey:
    """Collect anonymous responses to survey Questions"""
    
    def __init__(self,question):
        """Store a question, and prepare to store its responses"""
        self.question=question
        self.responses=[]

    def show_question(self):
        """Show the Survey Question"""
        print(self.question)
    
    def store_responses(self,response):
        """Store a single response to the survery"""
        self.responses.append(response)

    def show_results(self):
        """Show all the responses that have been give"""
        for response in self.responses:
            print(f"- {response}") 

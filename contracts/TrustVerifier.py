"""
GenAI Trust Assistant
GenLayer Intelligent Contract Prototype

This contract stores AI verification results
and generates trust levels.
"""


class TrustVerifier:

    def __init__(self):
        self.records = []


    def submit_verification(self, content, score):

        result = {
            "content": content,
            "trust_score": score,
            "status": self.calculate_status(score)
        }

        self.records.append(result)

        return result


    def calculate_status(self, score):

        if score >= 80:
            return "Verified"

        elif score >= 50:
            return "Needs Review"

        else:
            return "Low Confidence"


    def get_verification_history(self):

        return self.records

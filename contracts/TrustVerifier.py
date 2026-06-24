"""
GenAI Trust Assistant
GenLayer Intelligent Contract

AI verification workflow using decentralized validation logic.
"""


class TrustVerifier:

    def __init__(self):
        self.records = []


    def verify_ai_content(self, content, validator_results):

        consensus_score = self.calculate_consensus(
            validator_results
        )

        result = {
            "content": content,
            "validator_results": validator_results,
            "trust_score": consensus_score,
            "status": self.get_status(consensus_score)
        }

        self.records.append(result)

        return result


    def calculate_consensus(self, validator_results):

        if len(validator_results) == 0:
            return 0

        total = sum(validator_results)

        return total // len(validator_results)


    def get_status(self, score):

        if score >= 80:
            return "Verified"

        elif score >= 50:
            return "Needs Review"

        else:
            return "Low Confidence"


    def get_verification_history(self):

        return self.records

class PlannerAgent:
    def plan(self, query: str):
        query_lower = query.lower()

        if "compare" in query_lower:
            return {
                "type": "comparison",
                "sections": [
                    "Fully managed RAG options",
                    "Custom RAG architectures"
                ],
                "multi_pass": True
            }

        return {
            "type": "lookup",
            "sections": ["Retrievers"],
            "multi_pass": False
        }

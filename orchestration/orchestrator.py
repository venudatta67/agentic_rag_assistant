class Orchestrator:
    def __init__(self, planner, retriever, synthesizer):
        self.planner = planner
        self.retriever = retriever
        self.synthesizer = synthesizer

    def run(self, query):
        plan = self.planner.plan(query)
        all_passages = []

        for section in plan["sections"]:
            results = self.retriever.retrieve(query, section)
            all_passages.extend(results)

        return self.synthesizer.synthesize(query, all_passages)

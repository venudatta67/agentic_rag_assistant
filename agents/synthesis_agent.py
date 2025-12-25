class SynthesisAgent:
    def synthesize(self, query, passages):
        if not passages:
            return "This information is not available in the provided AWS RAG guide."

        answer = "Answer:\n\n"
        for p in passages:
            answer += f"- {p['text'][:300]}...\n"
            answer += f"  (Source: {p['section']}, page {p['page']})\n\n"

        return answer

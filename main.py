from ingestion.pdf_loader import load_pdf
from ingestion.chunker import semantic_chunk
from ingestion.embedder import Embedder
from ingestion.indexer import VectorIndex
from agents.planner_agent import PlannerAgent
from agents.retrieval_agent import RetrievalAgent
from agents.synthesis_agent import SynthesisAgent
from orchestration.orchestrator import Orchestrator

pages = load_pdf("data/retrieval-augmented-generation-options.pdf")
chunks = semantic_chunk(pages)

embedder = Embedder()
embeddings = embedder.embed([c["text"] for c in chunks])

index = VectorIndex(dim=len(embeddings[0]))
index.add(embeddings, chunks)

planner = PlannerAgent()
retriever = RetrievalAgent(index, embedder)
synthesizer = SynthesisAgent()

app = Orchestrator(planner, retriever, synthesizer)

print(app.run("Compare fully managed RAG options with custom architectures"))

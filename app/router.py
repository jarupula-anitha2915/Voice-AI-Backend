import json
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)

kb_embeddings = {k: model.encode(v, convert_to_tensor=True) for k, v in knowledge_base.items()}

def get_relevant_section(query):
    query_embedding = model.encode(query, convert_to_tensor=True)
    best_match = max(kb_embeddings.items(), key=lambda x: util.pytorch_cos_sim(query_embedding, x[1]))
    return knowledge_base[best_match[0]]
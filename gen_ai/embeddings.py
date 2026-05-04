"""
Module 1 — Concept 2: Embeddings

🧠 Problem Statement पहले समझते हैं
Tokenization के बाद हमारे पास integers हैं — जैसे [9906, 11, 1917]।
लेकिन model को meaning चाहिए, सिर्फ numbers नहीं।

9906 और 9907 numerically close हैं — लेकिन क्या वो semantically भी close हैं? नहीं। तो model को कैसे पता चलेगा कि "king" और "queen" related हैं, लेकिन "king" और "database" नहीं?
यहाँ Embeddings आते हैं।

📐 Embedding क्या है?
एक embedding एक high-dimensional float vector है जो किसी token या text की meaning को represent करता है।
"""

'''
Step 1: Package install / upgrade करो
    $ pip install --upgrade openai
    Version check करो:
    $ pip show openai
    # Version: 1.x.x होनी चाहिए — यह नई SDK है
Step 2: अगर API key नहीं है तो FREE alternative use करो
    # pip install sentence-transformers
    from sentence_transformers import SentenceTransformer
    
    model = SentenceTransformer("all-MiniLM-L6-v2")  # local, free, no API key
🎯 Recommended Path — sentence-transformers use करो
    चूँकि आप सीख रहे हैं, OpenAI API key की ज़रूरत नहीं। नीचे का code directly run होगा:
    $ pip install sentence-transformers numpy
    
'''
from itertools import combinations
import numpy as np
from sklearn.preprocessing import normalize

'''
# pip install openai numpy
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY")
def get_embedding(text: str) -> np.ndarray:
    # # Using openai library
    response = client.embeddings.create(
        model="text-embedding-3-small",  # 1536 dimensions
        input=text
    ) 
    return np.array(response.data[0].embedding)


API key न हो तो sentence-transformers library use करें — यह free और local है:

'''
# pip install sentence-transformers numpy
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")  # lightweight, 384 dimensions
def get_embedding(text: str) -> np.ndarray:
    return model.encode(text)


# # Using sentence-transformers library
def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

if __name__ == "__main__1":
    ########################################################################################################################
    ###########                                          Sample Example                                          ###########
    ########################################################################################################################
    # Test words
    words = ["king", "queen", "man", "woman", "database", "Python"]
    embeddings = {word: get_embedding(word) for word in words}

    # Pairwise similarity
    pairs = [
        ("king", "queen"),      # high similarity expected
        ("king", "man"),        # medium
        ("king", "database"),   # low
        ("Python", "database"), # medium — both tech terms
    ]

    for w1, w2 in pairs:
        score = cosine_similarity(embeddings[w1], embeddings[w2])
        print(f"{w1:10} ↔ {w2:10} : {score:.4f}")

    '''
    OUTPUT:

    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    Loading weights: 100%|██████████| 103/103 [00:00<00:00, 13535.95it/s]
    
    king       ↔ queen      : 0.6807   ← high
    king       ↔ man        : 0.3216   ← medium
    king       ↔ database   : 0.1919   ← low
    Python     ↔ database   : 0.3022   ← medium (tech domain)
    
    '''

if __name__ == "__main__":
    ########################################################################################################################
    # --- आपका Challenge ---
    # नीचे दिए sentences को embed करो और similarity निकालो।
    # फिर predict करो — कौन सा pair सबसे similar होगा BEFORE running?

    #   Task 1: हर possible pair की similarity निकालो
    #   Task 2: Top 3 most similar pairs print करो
    #   Task 3: सोचो — अगर user ने search किया "memory issue in server",
    #            तो इन 6 sentences में से कौन सा सबसे relevant होगा?
    #            Embedding similarity से verify करो।
    ########################################################################################################################
    sentences = [
        "The database crashed due to memory overflow.",
        "The server ran out of RAM and went down.",
        "I love eating pizza on weekends.",
        "My cat sleeps on the keyboard.",
        "Python is great for backend development.",
        "Django and FastAPI are web frameworks.",
    ]

    embeddings = model.encode(sentences)

    # --- Task 1: all pair similarities ---
    pairs = []
    for (i, j) in combinations(range(len(sentences)), 2):
        sim = cosine_similarity(embeddings[i], embeddings[j])
        pairs.append((i, j, sim))
    print("Task1. pairs: ", pairs)

    # --- Task 2: Top 3 most similar pairs ---
    pairs_sorted = sorted(pairs, key=lambda x: x[2], reverse=True)

    print("Task 2. Top three similar pairs:\n")
    c=1
    for i, j, sim in pairs_sorted[:3]:
        print(f"    {c}.    {sentences[i]}  <-->  {sentences[j]}")
        print(f"         Similarity: {sim:.4f}\n")
        c=c+1

    # --- Task 3: query similarity ---
    search_query = "memory issue in server"
    query_embedding = model.encode(search_query) # search_query को भी embed करो

    print(f"Task 3.1.  🔍 Search-Query: '{search_query}'\n")

    scores = []
    # search_query vector को हर sentence vector से compare करो
    for i, emb in enumerate(embeddings):
        sim = cosine_similarity(query_embedding, emb)
        scores.append((i, sim))

    # similarity के basis पर rank करो
    scores.sort(reverse=True)
    print(f"Task 3.2.  Rank with Search-Query: ")
    for rank, (score, sentence) in enumerate(scores, 1):
        print(f"    Rank {rank} | Score: {score:.4f} | {sentence}")

    best_match = max(scores, key=lambda x: x[1])
    best_match_result = sentences[best_match[0]]

    print(f"\nTask 3.3.  Best match for search_query ('{search_query}'):")
    print(f"    '{search_query}' <--> ", f"'{best_match_result}'")
    print(f"    Similarity: {best_match[1]:.4f}")


"""
OUTPUT:

    pairs:  [(0, 1, np.float32(0.659858)), (0, 2, np.float32(0.014092404)), (0, 3, np.float32(0.0854517)), (0, 4, np.float32(0.044606596)), (0, 5, np.float32(0.05225835)), (1, 2, np.float32(-0.031092595)), (1, 3, np.float32(0.0476429)), (1, 4, np.float32(0.09675061)), (1, 5, np.float32(0.081511825)), (2, 3, np.float32(0.17983006)), (2, 4, np.float32(-0.0036266008)), (2, 5, np.float32(0.050970726)), (3, 4, np.float32(0.010780789)), (3, 5, np.float32(7.737428e-06)), (4, 5, np.float32(0.49948275))]
    Top 3 similar pairs:
    
        The database crashed due to memory overflow.  <-->  The server ran out of RAM and went down.
        Similarity: 0.6599
    
        Python is great for backend development.  <-->  Django and FastAPI are web frameworks.
        Similarity: 0.4995
    
        I love eating pizza on weekends.  <-->  My cat sleeps on the keyboard.
        Similarity: 0.1798
    
    🔍 Query: 'memory issue in server'
    
    Rank 1 | Score: 5.0000 | 0.05740510672330856
    Rank 2 | Score: 4.0000 | 0.07640258222818375
    Rank 3 | Score: 3.0000 | 0.022985568270087242
    Rank 4 | Score: 2.0000 | -0.02267851121723652
    Rank 5 | Score: 1.0000 | 0.543595552444458
    Rank 6 | Score: 0.0000 | 0.4560445249080658

   
    Best match for query:
    
    The server ran out of RAM and went down.
    Similarity: 0.5436






💡 Task 3 का Core Insight
    यहाँ जो हो रहा है वो समझना बहुत ज़रूरी है:
    Query:    "memory issue in server"
    Sentence: "The database crashed due to memory overflow."
    
    इन दोनों में एक भी common word नहीं — लेकिन similarity score high है।
    यह keyword search नहीं है — यह semantic search है। Model को पता है कि "memory issue" और "memory overflow" same concept हैं, 
    और "server" और "database" related domain हैं।

    यही वो moment है जो traditional SQL LIKE '%memory%' queries से fundamentally अलग है।
    
    

"""
"""
Module 1 — LLM Fundamentals (The Core Architecture)
आज हम शुरू करेंगे Tokens और Embeddings से।

एक Python developer के रूप में, आप जानते हैं कि मशीनें strings को सीधे process नहीं करतीं। LLMs में text process करने के दो मुख्य stages होते हैं:

1. Tokenization: यह text को छोटे meaningful units (Tokens) में तोड़ता है। यह सिर्फ split(' ') नहीं है; यह sub-word level पर काम करता है।

2. Embeddings: यह सबसे महत्वपूर्ण हिस्सा है। हर Token को एक high-dimensional vector (numbers की list) में convert किया जाता है।

Logic: "King" और "Queen" के vectors mathematical space में एक-दूसरे के करीब होंगे, जबकि "Apple" का vector उनसे दूर होगा।

Architectural Flow:
Input Text -> Tokenizer -> Input IDs -> Embedding Model -> Vectors (Arrays of Floats)

जब आप query करते हैं, तो system mathematically 'Cosine Similarity' का उपयोग करके सबसे मिलते-जुलते vectors ढूंढता है।


Module 1 — Concept 1: Tokenization

"""






# pip install tiktoken
import tiktoken

# GPT-4 का tokenizer load करो
enc = tiktoken.get_encoding("cl100k_base")  # GPT-4, Claude जैसे models का encoding

def analyze_tokens(text: str) -> dict:
    tokens = enc.encode(text)
    decoded = [enc.decode([t]) for t in tokens]
    cost_estimate = (len(tokens) / 1000) * 0.01

    return {
        "text": text,
        "token_count": len(tokens),
        "token_pieces": decoded, # Tokens
        "token_ids": tokens,
        "estimated_cost_usd": round(cost_estimate, 6)
    }

texts = [
    "king queen database",
    "Hello, world!",
    "Tokenization is fascinating.",
    "मैं Python developer हूँ।",   # Hindi text
    "def fibonacci(n): return n",  # Code

    "The quick brown fox",
    "Thequickbrownfox",
    "HELLO WORLD",
    "hello world",
    "print('hello world')",
    "मैं एक senior Python developer हूँ",
]

for text in texts:
    result = analyze_tokens(text)
    print(f"\n📝 Text          : '{result['text']}'")
    print(f"   Pieces/Tokens : {result['token_pieces']}")
    print(f"   IDs           : {result['token_ids']}")
    print(f"   Count         : {result['token_count']} tokens")
    print(f"   Cost          : ${result['estimated_cost_usd']}")
    print("---------------------------------------------------------")
"""
Output:
📝 Text          : 'Hello, world!'
   Pieces/Tokens : ['Hello', ',', ' world', '!']
   IDs           : [9906, 11, 1917, 0]
   Count         : 4 tokens
   Cost          : $4e-05
---------------------------------------------------------

📝 Text          : 'Tokenization is fascinating.'
   Pieces/Tokens : ['Token', 'ization', ' is', ' fascinating', '.']
   IDs           : [3404, 2065, 374, 27387, 13]
   Count         : 5 tokens
   Cost          : $5e-05
---------------------------------------------------------

📝 Text          : 'मैं Python developer हूँ।'
   Pieces/Tokens : ['म', '�', '�', 'ं', ' Python', ' developer', ' ह', '�', '�', '�', '�', '�', '�']
   IDs           : [88344, 12906, 230, 73414, 13325, 16131, 85410, 12906, 224, 5619, 223, 12906, 97]
   Count         : 13 tokens
   Cost          : $0.00013
---------------------------------------------------------

📝 Text          : 'def fibonacci(n): return n'
   Pieces/Tokens : ['def', ' fibonacci', '(n', '):', ' return', ' n']
   IDs           : [755, 76798, 1471, 1680, 471, 308]
   Count         : 6 tokens
   Cost          : $6e-05
---------------------------------------------------------

📝 Text          : 'The quick brown fox'
   Pieces/Tokens : ['The', ' quick', ' brown', ' fox']
   IDs           : [791, 4062, 14198, 39935]
   Count         : 4 tokens
   Cost          : $4e-05
---------------------------------------------------------

📝 Text          : 'Thequickbrownfox'
   Pieces/Tokens : ['The', 'quick', 'brown', 'fox']
   IDs           : [791, 28863, 65561, 15361]
   Count         : 4 tokens
   Cost          : $4e-05
---------------------------------------------------------

📝 Text          : 'HELLO WORLD'
   Pieces/Tokens : ['HEL', 'LO', ' WORLD']
   IDs           : [51812, 1623, 51991]
   Count         : 3 tokens
   Cost          : $3e-05
---------------------------------------------------------

📝 Text          : 'hello world'
   Pieces/Tokens : ['hello', ' world']
   IDs           : [15339, 1917]
   Count         : 2 tokens
   Cost          : $2e-05
---------------------------------------------------------

📝 Text          : 'print('hello world')'
   Pieces/Tokens : ['print', "('", 'hello', ' world', "')"]
   IDs           : [1374, 493, 15339, 1917, 873]
   Count         : 5 tokens
   Cost          : $5e-05
---------------------------------------------------------

📝 Text          : 'मैं एक senior Python developer हूँ'
   Pieces/Tokens : ['म', '�', '�', 'ं', ' �', '�', 'क', ' senior', ' Python', ' developer', ' ह', '�', '�', '�', '�']
   IDs           : [88344, 12906, 230, 73414, 15272, 237, 65804, 10195, 13325, 16131, 85410, 12906, 224, 5619, 223]
   Count         : 15 tokens
   Cost          : $0.00015
---------------------------------------------------------


Observations
============
✅ Observation 1 — 
    core pipeline -->  "Text → tokens → numeric IDs"
✅ Observation 2 — 
    No of tockens: Actually यह library पर नहीं, tokenizer algorithm + vocabulary पर depend करता है। 
    हर model का अपना trained tokenizer होता है:
    Model   TokenizerVocab Size
    ------- -------------- -----
    GPT-4   cl100k_base     ~100K
    Claude  Custom BPE      ~100K
    LLaMA   3SentencePiece  ~128K
    ------- -------------- -----
✅ Observation 3 — 
    1️Spaces token का हिस्सा होते हैं
        enc.encode("world")   # → [14957]
        enc.encode(" world")  # → [1917]  ← अलग ID!
        
     2 Hindi text ज़्यादा tokens consume करती है
        "I am a Python developer"    # → 5 tokens
        "मैं Python developer हूँ"  # → 7-8 tokens
        
        Hindi/non-Latin scripts को ज़्यादा tokens लगते हैं क्योंकि BPE vocabulary mostly English text पर trained है। इसका मतलब — multilingual apps में API cost ज़्यादा होगी।
    
    3️Code efficiently tokenize होता है
        "def fibonacci(n):"  # → ['def', ' fib', 'on', 'acci', '(', 'n', '):']
        Common keywords जैसे def, return, import अक्सर single tokens होते हैं क्योंकि training data में बहुत सारा code था।



🧠 एक Line में Summary
    Tokenization = text को integers में convert करना, जो model की vocabulary के indices हैं। यही LLM का "input format" है — string नहीं।


    
"""
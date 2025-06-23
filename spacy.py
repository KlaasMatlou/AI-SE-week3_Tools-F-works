import spacy
from spacy import displacy

# Load the pre-trained English model
nlp = spacy.load("en_core_web_sm")

# Sample text simulating an Amazon review
review_text = """
I recently bought the new AcmeUltra Laptop by Acme Inc., and its performance is outstanding!
The battery life, screen quality, and build are all top-notch. However, the customer support could be better.
"""

# Process the text with spaCy
doc = nlp(review_text)

# Extract and print named entities (e.g., product names, organizations)
print("Named Entities:")
for ent in doc.ents:
    print(f"{ent.text} - {ent.label_}")

# Rule-based sentiment analysis: a simple approach based on keyword presence
positive_keywords = ["outstanding", "top-notch", "excellent", "good"]
negative_keywords = ["bad", "poor", "could be better", "disappointing"]

# Lowercase conversion for matching
review_lower = review_text.lower()
sentiment = "Positive" if any(word in review_lower for word in positive_keywords) else "Negative"
print(f"\nSentiment: {sentiment}")

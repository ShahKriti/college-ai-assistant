import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nlp.page_reader import read_page

# Load question dataset
with open("data/questions.json") as f:
    questions = json.load(f)

# Flatten questions
all_questions = []
labels = []

for intent, qs in questions.items():
    for q in qs:
        all_questions.append(q)
        labels.append(intent)

# Create vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(all_questions)


def get_response(user_message):

    user_message = user_message.lower()

    user_vector = vectorizer.transform([user_message])

    similarity = cosine_similarity(user_vector, X)

    best_match = similarity.argmax()
    score = similarity[0][best_match]

    if score < 0.2:
        return "Sorry, I couldn't understand your question. Please ask about admissions, courses, departments or contact."

    intent = labels[best_match]

    if intent == "admissions":
        return read_page("admissions")[:500]

    elif intent == "courses":
        return read_page("courses")[:500]

    elif intent == "departments":
        return read_page("departments")[:500]

    elif intent == "contact":
        return read_page("contact")[:500]

    else:
        return "I am here to help with college information."
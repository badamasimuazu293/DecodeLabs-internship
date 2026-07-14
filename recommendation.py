import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("raw_skills.csv")

user_input = input(
    "Enter your skills separated by commas: "
)

documents = data["Skills"].tolist()
documents.append(user_input)

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

similarity = cosine_similarity(
    tfidf_matrix[-1],
    tfidf_matrix[:-1]
)

data["Score"] = similarity.flatten()

results = data.sort_values(
    by="Score",
    ascending=False
)

print("\nTop Recommendations:\n")

for i in range(3):
    print(
        f"{i+1}. {results.iloc[i]['Role']} "
        f"({results.iloc[i]['Score']:.2%})"
    )
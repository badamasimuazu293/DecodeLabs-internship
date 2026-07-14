import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

df = pd.read_csv('raw_skills.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():

    user_skills = request.form['skills']

    data = df['Skills'].tolist()
    data.append(user_skills)

    tfidf = TfidfVectorizer()

    vectors = tfidf.fit_transform(data)

    similarity = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    ).flatten()

    df['Score'] = similarity

    results = df.sort_values(
        by='Score',
        ascending=False
    ).head(3)

    return render_template(
        'result.html',
        results=results.to_dict('records')
    )

if __name__ == '__main__':
    app.run(debug=True)
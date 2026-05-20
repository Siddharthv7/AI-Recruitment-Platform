from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_resume_score(resume_text, job_description):

    text = [resume_text, job_description]

    cv = CountVectorizer()

    matrix = cv.fit_transform(text)

    similarity = cosine_similarity(matrix)[0][1]

    score = round(similarity * 100)

    return score
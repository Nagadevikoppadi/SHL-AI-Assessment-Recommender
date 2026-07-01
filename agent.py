from retriever import retrieve


def recommend_assessments(job_description):
    return retrieve(job_description)
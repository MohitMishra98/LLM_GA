import google.generativeai as genai
import os

GOOGLE_API_KEY = os.getenv("GOOGLEAPI_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini=1.0-pro")


#resource link https://ai.google.dev/tutorials/python_quickstart#use_embeddings

content = genai.embed_content(
    model="models/embedding-001",
    content="what will be the embedding of this line",
    task_type="retrieval_document",
    title="Embedding of single string"
)

# A list of inputs will give A list of vectors output

#print(content)

print(str(content['embedding'])[:50], '... TRIMMED]')

content = genai.embed_content(
    model="models/embedding-001",
    content=["what will be the embedding of this line",
             "what will be the embedding of this new line"],
    task_type="retrieval_document",
    title="Embedding of single string"
)

print(content)
print(type(content))
print(content["embedding"])

print(f"this is list1 {content["embedding"][0]}\nthis is list2 {content["embedding"][1]}")

#when we pass an list of inputs the outputs is a dict with key "embedding" and value is list that contains
#list of lists

#eg dict = {"embedding":[["embeddings of query 1"],["embeddings of query 2"]]}
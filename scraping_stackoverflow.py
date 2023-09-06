import requests
from bs4 import BeautifulSoup
import json


questions_data = {
    "questions": []
}

res = requests.get("https://stackoverflow.com/questions/tagged/pandas?sort=Newest&filters=NoAnswers&edited=true&page={}".format(1))
soup = BeautifulSoup(res.text, "html.parser")

questions = soup.select(".s-post-summary")

for que in questions:
    q = que.select_one('.s-link').getText()
    vote_count = que.select_one('.s-post-summary .s-post-summary--stats-item__emphasized').getText()
    views = que.select_one('.s-post-summary--stats-item ').attrs['title']
    tags = [i.getText() for i in (que.select('.post-tag'))]
    questions_data['questions'].append({
        "question": q,
        "views": views,
        "vote_count": vote_count,
        "tags": tags
    })


json_data = json.dumps(questions_data, indent=4)
print(json_data)

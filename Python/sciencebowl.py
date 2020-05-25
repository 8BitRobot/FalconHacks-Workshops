import requests

LINK = "https://www.quizdb.org/api/search?search%5Bquery%5D=&search%5Bfilters%5D%5Bcategory%5D%5B%5D=17&search%5Bfilters%5D%5Bsearch_type%5D%5B%5D=Question&search%5Bfilters%5D%5Bsearch_type%5D%5B%5D=Answer&search%5Bfilters%5D%5Bdifficulty%5D%5B%5D=regular_high_school&search%5Bfilters%5D%5Bdifficulty%5D%5B%5D=easy_high_school&search%5Bfilters%5D%5Bsubcategory%5D%5B%5D=36&search%5Bfilters%5D%5Bsubcategory%5D%5B%5D=14&search%5Bfilters%5D%5Bsubcategory%5D%5B%5D=5&search%5Bfilters%5D%5Bsubcategory%5D%5B%5D=23&search%5Bfilters%5D%5Bsubcategory%5D%5B%5D=26&search%5Bfilters%5D%5Bsubcategory%5D%5B%5D=10&search%5Bfilters%5D%5Bsubcategory%5D%5B%5D=37&search%5Bfilters%5D%5Bsubcategory%5D%5B%5D=18&search%5Bfilters%5D%5Bquestion_type%5D%5B%5D=Tossup&search%5Bfilters%5D%5Bquestion_type%5D%5B%5D=Bonus&search%5Blimit%5D="
COUNT = 15

r = requests.get(LINK + str(count))

for question in r.json()["data"]["tossups"]:
    key = question["text"]
    value = question["answer"].split("[")[0].split("&lt")[0]
    questions[key] = value

for question in questions:
	print("QUESTION: " + question)
	print("ANSWER: " + questions[question])
	print()

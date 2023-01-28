import requests

#unique key for dev only
Api_key = "a254022442be4056a0da64e76a0ab2a5"
country = 'in'

#creating function to get the key form the news api
def get_news(Response = 'title',Country=country,API_key=Api_key):
    #issues : Second time why date arrises
    main_url = f"https://newsapi.org/v2/top-headlines?country={Country}&apiKey={API_key}"
    obtained_news = requests.get(main_url).json()
    l = obtained_news["articles"]
    count = 0
    res = []
    for i in l:
        count += 1
        res.append(i[Response])
    return res
# Shorty-Web-app

# **ACKNOWLEDGEMENT**

Apart from the efforts of me, the success of any project depends largely
on

the encouragement and guidelines of many others. I take this opportunity
to express my gratitude to the people who have been instrumental in the
successful completion of this project.

I express my heartfelt gratitude to my parents for constant
encouragement while carrying out this project.

I gratefully acknowledge the contribution of the individuals who
contributed in

bringing this project up to this level, who continues to look after me
despite my flaws. I express my deep sense of gratitude to the luminary
The Principal, Kendriya Vidyalaya Barrackpore(Army) has been
continuously motivating and extending their helping hand to us.

I am overwhelmed to express my thanks to The Administrative Officer for
providing me with infrastructure and moral support while carrying out
this project in the school.

My sincere thanks to Mr. Anil Yadav, Master In-charge, A guide, Mentor
all

The above friend, who critically reviewed my project and helped in
solving each and every problem, occurred during implementation of the
project.

The guidance and support received from all the members who contributed
and who are contributing to this project, was vital for the success of
the project. I am grateful for their constant support and help.

# **PROJECT REPORT ON NEWS WEBSITE (Shorty)**

## **INTRODUCTION**

This Shorty is developed with a view of providing news in the form of a
short article. Due to our fast paced lifestyle we aren't able to keep
notified about our country. This project helps the user to read the news
in a short amount of time and if he/she wants to read more of it then
they can visit the target website where the news is being uploaded.This
project may help both the students as well as people of different ages
to read news in most fast and easy way.

## 

## 

## 

## 

## 

## 

## 

## 

## **OBJECTIVES OF THE PROJECT**

The objective of the project is to use less time to read the news of our
country and in the most efficient way.

1.  Reduces time of the user

2.  They can choose countries (Currently India,USA,UK is available)

3.  SHows both full and short format of the news

4.  Can be accessed through any smart devices i.e laptop , mobile or tab

## 

## **LIMITATIONS**

Since this project is currently is not being hosted online or in any
website service provider so there are multiple limitations to this
project right now

1.  The server is offline so we have to launch it offline only

2.  Cannot cover the entire news since I tried to create this with the
    > NEWS API and we can get a limited amount of feed at once.

## 

## 

## **PROPOSED SYSTEM**

Nowadays due to our fast paced lifestyle we aren't able to read
newspapers or watch news channels regularly, due to which we are not
aware of what is going on in our country and society. So to spread more
awareness we must know what\'s going on in our surroundings.

Sometimes it is kinda hard to get the newspaper everywhere with us or we
cant watch Tv channels everywhere. So SHORTY helps us to keep track of
our locality and country by providing exotic news to our users in a
short and efficient way which I call as Feed. Each Feed contains the
heading as well as the few lines of the articles posted on their
respective websites.

This program helps users both to save money and time.Not only that we
can also add new countries so that users can choose their countries
accordingly.

Since currently the website is not hosted online so we have to use a
local server only.

## **SYSTEM DEVELOPMENT LIFE CYCLE (SDLC)**

The systems development life cycle is a project management technique
that divides complex projects into smaller, more easily managed segments
or phases. Segmenting projects allows managers to verify the successful
completion of project phases before allocating resources to subsequent
phases

Software development projects typically include initiation, planning,
design, development, testing, implementation, and maintenance phases.
However, the phases may be divided differently depending on the
organisation involved For example, initial project activities might be
designated as request, requirements-definition, and planning phases, or
jpation, concept-development, and planning phases. End users of the
system under development should be involved in reviewing the output of
each phase to ensure the system is being built to deliver the needed
functionality.

# **SYSTEM IMPLANTATION**

Before installing please check the requirements section to get a
detailed view of the utilised hardware and softwares.

## 

## 

## **HARDWARE REQUIREMENTS**

1.  Processor: Dual core and above

2.  Storage: 10 MB

3.  Memory: 1024 MB / 1 GB

## **SOFTWARE REQUIREMENTS**

1.  Operating System: Windows 10 or above

2.  Platform: Visual Studio Code

3.  Database: MySQL 8.0

4.  Language: Python 3.9.2

5.  Any web browser like google chrome , internet explorer etc

## **PYTHON MODULES REQUIREMENTS**

1.  MySql.connector

2.  Django

# **DIRECTORY DISTRIBUTION**

Since I used Django while creating my project, we first need to
understand the directory distribution of the project folder.

Django creates multiple tables for basic running of the website so,
according to the diagram the only database which our program will store
and retrieve data is from **newsfeed_country .**

Now in the table **newsfeed_country** has two attributes one is called
CName and CCode which defines the countries name and countries
alpha-2-code respectively and the id attribute is created by the django
so to create the Primary key attribute out of it since during the
declaration I didn't created or mentioned the Primary key table.


Currently during the development I have managed to provide features of
three countries only like INDIA,USA,UK but at any instance the new
Countries can be added using CName and

We can add new countries by writing the **SQL command**

```sql
  -----------------------------------------------------------------------
  INSERT INTO newsfeed_country (CName,CCode) VALUES
  (\<CountryName1\>,\<CountryCode1\>),\
  (\<CountryName2\>,\<CountryCode2\>),\
  \...\...\...\...\... ;
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------
```

Here are the database credentials which I been using during the the
development process but we can change it by navigating to the **SHORTYV2
\> shortyv2 \> setting.py**


# **PYTHON MODULES USED**

## **Django**

Django is a free and open-source, Python-based web framework that
follows the model--template--views (MTV) architectural pattern.It is
maintained by the Django Software Foundation (DSF), an independent
organisation established in the US as a non-profit.

Django\'s primary goal is to ease the creation of complex,
database-driven websites. The framework emphasises reusability and
\"pluggability\" of components, less code, low coupling, rapid
development, and the principle of don\'t repeat yourself. Python is used
throughout, even for settings, files, and data models. Django also
provides an optional administrative create, read, update and delete
interface that is generated dynamically through introspection and
configured via admin models.


## **News (My module)**

This module holds only one function since in this project the main
working of the website is to retrieve data from API and clean it
according to our use. The get_news function retrieves the data from the
api and cleans and returns the required format as provided by the user
which is given in the form of response in the parameters.

```python
import requests


#unique key for dev only
Api_key = "a254022442be4056a0da64e76a0ab2a5"
country = 'in'


#creating function to get the key form the news api
def get_news(Response = 'title',Country=country,API_key=Api_key):
    #issues : Second time why date arises
    main_url =   f"https://newsapi.org/v2/top-headlines?country={Country}&apiKey={API_key}"
    obtained_news = requests.get(main_url).json()
    l = obtained_news["articles"]
    count = 0
    res = []
    for i in l:
        count += 1
        res.append(i[Response])
    return res
```

# **HOW TO INSTALL**

Since it\'s a website and has multiple files and multiple computers
nowadays don\'t have CD drivers, I thought it would be wise to store the
source file in github.

Visit this link to download the zip file of the Project.Then follow the
process

**Code \> Download Zip \> Extract the file.**


# **SOURCE CODE**

Django creates multiple files all by itself but we have to work on the
working of the **views.py (Newsfeed)** file because it\'s the main file
which works on the background of the server to process data and display
it on the website.

```python
from django.shortcuts import render
from .models import Country
from Mymodules import News
# Create your views here.
def Page(request):
   
    if request.method == "POST":
        a = request.POST.get('_country') #getting code back
       
        #getting news data using my module
        Ndata = News.get_news(Country=a) #title list
        Cdata = News.get_news(Country=a,Response="content") #content list
        Urldata = News.get_news(Country=a,Response="url") #url list
        urlToImage = News.get_news(Country=a,Response="urlToImage") #getting image from the get news function


        #Creating proper objects for the job [["Title","content","url for more details","image url"].....]
        Obj = []
        for i in Ndata:
            cache = []
            cache.append(i)
            loc = Ndata.index(i)
            cache.append(Cdata[loc])
            cache.append(Urldata[loc])
            cache.append(urlToImage[loc])
            Obj.append(cache)


        return render(request,"main.html",{
            "NewsFeeds": Obj,
            "Country":Country.objects.all()
        })


   
    #getting news data using my module
    Ndata = News.get_news(Country='in') #title list
    Cdata = News.get_news(Country='in',Response="content") #content list
    Urldata = News.get_news(Country='in',Response="url") #url list
    urlToImage = News.get_news(Country='in',Response="urlToImage") #getting image from the get news function


    #Creating proper objects for the job [["Title","content","url for more details","image url"].....]
    Obj = []
    for i in Ndata:
        cache = []
        cache.append(i)
        loc = Ndata.index(i)
        cache.append(Cdata[loc])
        cache.append(Urldata[loc])
        cache.append(urlToImage[loc])
        Obj.append(cache)


    return render(request,"main.html",{
        "NewsFeeds": Obj,
        "Country":Country.objects.all()
    })
```


## **BIBLIOGRAPHY**

1\. google.com

2\. stackoverflow.com

3\. python.org

4\.https://dev.mysql.com/doc/

5\.https://docs.djangoproject.com/en/4.1/

6\.https://newsapi.org/docs

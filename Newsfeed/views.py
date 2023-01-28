from django.shortcuts import render
from .models import Country
from Mymodules import News
# Create your views here.
def Page(request):
    
    if request.method == "POST":
        a = request.POST.get('_country') #getting code back 
        
        #getting news datas using mymodule 
        Ndata = News.get_news(Country=a) #title list
        Cdata = News.get_news(Country=a,Response="content") #content lsit
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

    
    #getting news datas using mymodule 
    Ndata = News.get_news(Country='in') #title list
    Cdata = News.get_news(Country='in',Response="content") #content lsit
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


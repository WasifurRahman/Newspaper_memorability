import json
from pprint import pprint
import NewsItem

jsonLimit = 10
allNewsItems = []

def create_news_item(singleNews):
    newsCrawledDate = singleNews['news_crawled_date']['$date']
    newsMLTags = singleNews['news_ml_tags']
    newspaperURL = singleNews['newspaper_url']
    newsURL = singleNews['news_url']  
    newsHeadline = singleNews['news_headline']
    newsReporters = singleNews['news_reporters']
    newsOriginalTags  = singleNews['news_original_tags']
    newsText = singleNews['news_text']
    newsNerTags = singleNews['news_ner_tags']
    newsPublishDate = singleNews['news_publish_date']['$date']
    newsNaiveTags = singleNews['news_naive_tags']
    newsImageURLs = singleNews['news_image_urls']
    newsLocation = singleNews['news_location']
    newsPaperName = singleNews['newspaper_name']
    newsKeyWords = singleNews['news_keywords']
    newsID = singleNews['_id']['$oid']
    isNegative = singleNews['is_negative']
    newNews = NewsItem.NewsItem(newsCrawledDate, newsMLTags, newspaperURL,newsURL,newsHeadline,newsReporters,newsOriginalTags,newsText,newsNerTags,newsPublishDate,newsNaiveTags,newsImageURLs,newsLocation,newsPaperName,newsKeyWords,newsID,isNegative)
    
    allNewsItems.append(newNews)
    

if __name__ == "__main__":
    #print "Hello World"
    
    #with open('bd_news_dhaka_tribune.json', 'r') as f:
    #    x = json.loads(f.read()) 
    jsonCount = 0
    allNewsJson = []
    for line in open('bd_news_dhaka_tribune.json', 'r'):
        oneJson = json.loads(line)
        print (oneJson)
        allNewsJson.append(oneJson);
        jsonCount+=1;
        
        if(jsonCount == jsonLimit):
            break
     
        #pprint(data)
    
    for singleNews in allNewsJson:
        # @type singleNews 
        
        allKeys =  singleNews.keys()
         
        for key in allKeys:
             print(key)
            #revisedKey = key.encode('utf8')
#             value = singleNews[key]
#              
#             if isinstance(value, str):
#                 value = value.encode('utf8')
#              
#              
#             print (key,type(value),value)
        create_news_item(singleNews)
        
        for eachItem in allNewsItems:
            print(str(eachItem))

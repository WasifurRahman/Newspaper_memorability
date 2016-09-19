'''
Created on Sep 19, 2016

@author: wasif
'''
class NewsItem:
    def __init__(self, newsCrawledDate, newsMLTags, newspaperURL,newsURL,newsHeadline,newsReporters,newsOriginalTags,newsText,newsNerTags,newsPublishDate,newsNaiveTags,newsImageURLs,newsLocation,newsPaperName,newsKeyWords,newsID,isNegative):
        self.newsCrawledDate =  newsCrawledDate
        self.newsMLTags = newsMLTags
        self.newspaperURL = newspaperURL
        self.newsURL = newsURL
        self.newsHeadline = newsHeadline
        self.newsReporters = newsReporters
        self.newsOriginalTags = newsOriginalTags
        self.newsText = newsText
        self.newsNerTags = newsNerTags
        self.newsPublishDate = newsPublishDate
        self.newsNaiveTags = newsNaiveTags 
        self.newsImageURLs = newsImageURLs
        self.newsLocation = newsLocation
        self.newsPaperName = newsPaperName
        self.newsKeyWords = newsKeyWords
        self.newsID = newsID
        self.isNegative = isNegative 
        
        
        
    def get_news_crawled_date(self):
        return self.__newsCrawledDate


    def get_news_mltags(self):
        return self.__newsMLTags


    def get_newspaper_url(self):
        return self.__newspaperURL


    def get_news_url(self):
        return self.__newsURL


    def get_news_headline(self):
        return self.__newsHeadline


    def get_news_reporters(self):
        return self.__newsReporters


    def get_news_original_tags(self):
        return self.__newsOriginalTags


    def get_news_text(self):
        return self.__newsText


    def get_news_ner_tags(self):
        return self.__newsNerTags


    def get_news_publish_date(self):
        return self.__newsPublishDate


    def get_news_naive_tags(self):
        return self.__newsNaiveTags


    def get_news_image_urls(self):
        return self.__newsImageURLs


    def get_news_location(self):
        return self.__newsLocation


    def get_news_paper_name(self):
        return self.__newsPaperName


    def get_news_key_words(self):
        return self.__newsKeyWords


    def get_news_id(self):
        return self.__newsID


    def get_is_negative(self):
        return self.__isNegative


    def set_news_crawled_date(self, value):
        self.__newsCrawledDate = value


    def set_news_mltags(self, value):
        self.__newsMLTags = value


    def set_newspaper_url(self, value):
        self.__newspaperURL = value


    def set_news_url(self, value):
        self.__newsURL = value


    def set_news_headline(self, value):
        self.__newsHeadline = value


    def set_news_reporters(self, value):
        self.__newsReporters = value


    def set_news_original_tags(self, value):
        self.__newsOriginalTags = value


    def set_news_text(self, value):
        self.__newsText = value


    def set_news_ner_tags(self, value):
        self.__newsNerTags = value


    def set_news_publish_date(self, value):
        self.__newsPublishDate = value


    def set_news_naive_tags(self, value):
        self.__newsNaiveTags = value


    def set_news_image_urls(self, value):
        self.__newsImageURLs = value


    def set_news_location(self, value):
        self.__newsLocation = value


    def set_news_paper_name(self, value):
        self.__newsPaperName = value


    def set_news_key_words(self, value):
        self.__newsKeyWords = value


    def set_news_id(self, value):
        self.__newsID = value


    def set_is_negative(self, value):
        self.__isNegative = value


    def del_news_crawled_date(self):
        del self.__newsCrawledDate


    def del_news_mltags(self):
        del self.__newsMLTags


    def del_newspaper_url(self):
        del self.__newspaperURL


    def del_news_url(self):
        del self.__newsURL


    def del_news_headline(self):
        del self.__newsHeadline


    def del_news_reporters(self):
        del self.__newsReporters


    def del_news_original_tags(self):
        del self.__newsOriginalTags


    def del_news_text(self):
        del self.__newsText


    def del_news_ner_tags(self):
        del self.__newsNerTags


    def del_news_publish_date(self):
        del self.__newsPublishDate


    def del_news_naive_tags(self):
        del self.__newsNaiveTags


    def del_news_image_urls(self):
        del self.__newsImageURLs


    def del_news_location(self):
        del self.__newsLocation


    def del_news_paper_name(self):
        del self.__newsPaperName


    def del_news_key_words(self):
        del self.__newsKeyWords


    def del_news_id(self):
        del self.__newsID


    def del_is_negative(self):
        del self.__isNegative

    newsCrawledDate = property(get_news_crawled_date, set_news_crawled_date, del_news_crawled_date, "newsCrawledDate's docstring")
    newsMLTags = property(get_news_mltags, set_news_mltags, del_news_mltags, "newsMLTags's docstring")
    newspaperURL = property(get_newspaper_url, set_newspaper_url, del_newspaper_url, "newspaperURL's docstring")
    newsURL = property(get_news_url, set_news_url, del_news_url, "newsURL's docstring")
    newsHeadline = property(get_news_headline, set_news_headline, del_news_headline, "newsHeadline's docstring")
    newsReporters = property(get_news_reporters, set_news_reporters, del_news_reporters, "newsReporters's docstring")
    newsOriginalTags = property(get_news_original_tags, set_news_original_tags, del_news_original_tags, "newsOriginalTags's docstring")
    newsText = property(get_news_text, set_news_text, del_news_text, "newsText's docstring")
    newsNerTags = property(get_news_ner_tags, set_news_ner_tags, del_news_ner_tags, "newsNerTags's docstring")
    newsPublishDate = property(get_news_publish_date, set_news_publish_date, del_news_publish_date, "newsPublishDate's docstring")
    newsNaiveTags = property(get_news_naive_tags, set_news_naive_tags, del_news_naive_tags, "newsNaiveTags's docstring")
    newsImageURLs = property(get_news_image_urls, set_news_image_urls, del_news_image_urls, "newsImageURLs's docstring")
    newsLocation = property(get_news_location, set_news_location, del_news_location, "newsLocation's docstring")
    newsPaperName = property(get_news_paper_name, set_news_paper_name, del_news_paper_name, "newsPaperName's docstring")
    newsKeyWords = property(get_news_key_words, set_news_key_words, del_news_key_words, "newsKeyWords's docstring")
    newsID = property(get_news_id, set_news_id, del_news_id, "newsID's docstring")
    isNegative = property(get_is_negative, set_is_negative, del_is_negative, "isNegative's docstring")

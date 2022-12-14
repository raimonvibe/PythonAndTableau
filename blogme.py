import pandas
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Reading excel for xlsx files

data = pandas.read_excel('articles.xlsx')

# Summary of the data

data.describe()

# Summary of the columns
data.info()

# Counting the number of articles per source
# Format of groupby: dataFrame.groupby(['column_to_group'])['column_to_count'].count()
# count() counts the total of occurrences
data.groupby(['source_id'])['article_id'].count()

# Number of reaction by publisher
# sum() counts the items
data.groupby(['source_id'])['engagement_reaction_count'].sum()

# Dropping column on axis = 1 : dropping a column

data = data.drop('engagement_comment_plugin_count' , axis = 1)

# Creating a keyword flag

keyword = 'crash'

# # Lets create a for loop to isolate each title row
# # Because there's a Nan value in column number:  ; We have to apply a try and except statement
# length = len(data)
# keyword_flag = []
# for item in range(0, length):
#     heading = data['title'][item]
#     try:     
#         if keyword in heading:
#             flag = 1
#         else:
#             flag = 0
#     except:
#         flag = 0
#     keyword_flag.append(flag)

    
# Creating a function

def keywordFlag(keyword):
    
    length = len(data)
    keyword_flag = []
    for item in range(0, length):
        heading = data['title'][item]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
        
keywordflag = keywordFlag('murder')

# Creating a new column in data DataFrame

data['keyword_flag'] = pandas.Series(keywordflag)

# SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]

sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

# Adding a for loop to extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length = len(data)
for item in range(0, length):
    try:
        text = data['title'][item]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)


# Transforming result to Series to add to the dataFrame

title_neg_sentiment = pandas.Series(title_neg_sentiment)
title_pos_sentiment = pandas.Series(title_pos_sentiment)
title_neu_sentiment = pandas.Series(title_neu_sentiment)

# Adding the columns

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment


# Writing data as xlsx file

data.to_excel('blogme_clean.xlsx', sheet_name = 'blogmedata', index = False)










    
        



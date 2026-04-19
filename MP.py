import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("E:/MBA/Sem 4/Mini Project/Reviews.csv")


print(data.columns)


reviews = data['Text']


positive_words = ["good", "great", "excellent", "amazing", "love", "nice", "best"]
negative_words = ["bad", "poor", "worst", "hate", "terrible", "awful", "not"]


def get_sentiment(review):
    review = str(review).lower()
    if any(word in review for word in positive_words):
        return "Positive"
    elif any(word in review for word in negative_words):
        return "Negative"
    else:
        return "Neutral"


data['Sentiment'] = reviews.apply(get_sentiment)


sentiment_count = data['Sentiment'].value_counts()
print(sentiment_count)


sentiment_count.plot.pie(autopct='%1.1f%%')
plt.title("Sentiment Distribution")
plt.ylabel("")
plt.show()


sentiment_count.plot(kind='bar')
plt.title("Sentiment Count")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

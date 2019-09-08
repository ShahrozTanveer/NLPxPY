from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
TEXT = """Hello Mr. Sam, how are you doing today? The weather is great, and Money heist is awesome. You shouldn't eat pancakes. The sky is pinkish-blue."""
TokenizedWords=word_tokenize(TEXT)
StopWords=set(stopwords.words("english"))
FilteredWord=[word for word in TokenizedWords if word not in StopWords]
print("====FilteredWord====")
print(FilteredWord)
print("====TokenizedWords====")
print(TokenizedWords)

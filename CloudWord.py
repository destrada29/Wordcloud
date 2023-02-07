# Import the required libraries
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
import re
import pandas as pd
import numpy as np
import nltk
import os

# Download the necessary NLTK corpora
nltk.download('punkt')
nltk.download('stopwords')

# Open the text file and read its contents into the variable "s"
s = open("set your lyrics")
s = s.read()
print(s)

# Remove any punctuation from the text
out = re.sub(r'[^\w\s]', '', s)
print(out)

# Tokenize the words in the text
ice = word_tokenize(out)
ice

# Create a set of English stopwords and add additional words to it
a = set(stopwords.words("english"))
a.add('I')
a.add('Would')
a.add('got')
a.add('Im')
a.add('em')
a.add('get')
a.add('aint')

# Create a set of Spanish stopwords
b = set(stopwords.words("spanish"))

# Remove the stopwords from the tokenized text
stopwords = [x for x in ice if x not in a and x not in b]
print(stopwords)

# Calculate the frequency distribution of the remaining words
fdist = FreqDist(stopwords)
print(fdist)

# Get the 30 most common words in the frequency distribution
fdist1 = fdist.most_common(30)
print(fdist1)

# Load the image mask for the wordcloud
mask = Image.open("CloudWords\nube.png")
mask = np.array(mask)

# Convert all pixel values of 1 and 2 to 255
mask[mask == 1] = 255
mask[mask == 2] = 255

# Convert the list of remaining words to a string and remove any punctuation
stopwords = str(stopwords)
stopwords = re.sub(r'[^\w\s]', '', stopwords)

# Generate the wordcloud using the input text and the image mask
wordcloud = WordCloud(background_color="white", max_words=50, mask=mask,
                      contour_color='black', contour_width=3).generate(stopwords)

# Display the generated wordcloud
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

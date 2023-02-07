# Lyrics Wordcloud

A Python script to create a wordcloud from a text file containing lyrics.

## Requirements

- PIL
- wordcloud
- matplotlib
- nltk
- pandas
- numpy

## Usage

1. Download the necessary NLTK corpora by running the following code:

```python
nltk.download('punkt')
nltk.download('stopwords')
```

2. Replace the text file path in line 22 with your desired file path:

```python
s = open("set your lyrics")
```

3. Replace the image mask file path in line 66 with your desired file path:

```python
mask = Image.open("CloudWords\nube.png")
```

4. Run the script to generate the wordcloud.

## License

This project is Open source

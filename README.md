# BERToneIndicators

**Introduction**

Tone indicators (written as /tone) are a tool used to reduce ambiguity,
conveying information that is generally lost online. The literal text of informal communication like a tweet is often insufficient to determine the meaning, which relies on much a larger, inaccessible context. Tone indicators attempt to address this issue.
Using data from Twitter, we built a BERT model to classify the tone indicator tag associated with a sentence. We then analyzed the various attention heads to gain semantic insight into which sets of words or other linguistic features are most associated with certain tone indicators.

**Dataset**

Using the Twitter API, we scraped over 1.5 million tweets between January and March of 2022. The language of each tweet was determined using langdetect, which also cleans excess emojis. The end result was a subset of approximately 150,000 tweets.
We also obtained a training set consisting of a separate and smaller scrape of tweets from 3 random days in February of 2022. All data in the training set was labeled with the emotional tag that it contained using one-hot encoding. All tags were stripped out and replaced with white space in the test set.

**Usage**

The BERT model with custom architecture is available in `BERT.ipynb` or alternatively `BERT.py` and the Naive Bayes classifier is available in `Baseline_Naive_Bayes.ipynb` . Additionally, a visualization of the BERT model architecture is available in the documents folder.

**Results**

Results are summarized on a poster in the documents directory.

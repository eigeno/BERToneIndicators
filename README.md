# cs4995-srnlp

**Idea** 

Train a BERT model on data from twitter to learn syntactic & semantic relations between language & tone indicator tags. 

**What are tone indicators**

Tone indicators are shorthand for words used to convey tone, which the Cambridge Dictionary defines as "a quality in the voice that expresses the speaker's feelings or thoughts". The tone of someone's voice can be joking, or serious; it can be teasing, or threatening. It can be negative, positive, or neutral. It can be sexually suggestive, or entirely friendly. Tone can do so much to change the meaning and implications of a sentence.

Some examples of tone indicators are "/j", "/s", "/srs", "/p", "/r", "/ly", "neg", "pos", "/gen" and "/c". Though there are many others, these are the ones that are most commonly used and needed for clarity of communication. The intended use of tone indicators is in text, and they are prevalent on social media where miscommunication is rife, and posts and messages are often misinterpreted.

**What is BERT** 

BERT is at its core a transformer language model with a variable number of encoder layers and self-attention heads. A transformer is a deep learning model that adopts the mechanism of self-attention, differentially weighting the significance of each part of the input data.

**The data** 

We scraped twitter for any tweets containing strings matching 5 commonly used tone indicators `/srs /nbh /hyp /pos /neg` over the span of three months, which yielded approximately 1.5 million tweets in the raw dataset. After filtering for quality, we ended up with a dataset of approximately 150,000 tweets that the model was trained on. 

The breakdown of the data per label is 
``` 
srs    51329
nbh     4080
hyp      105
pos    78147
neg    14146
```

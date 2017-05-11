Project 7 - Clustering Programming Posts on Reddit
--

**Problem:**

To attempt to cluster reddit posts from various subreddits and find any interesting insights from the clusters.

**Data:**

I was quite selective with the features in the dataset. All the null values were dropped, and the final features that were used in our analysis were Number of comments, Score, Text, and Title. I separated all the texts and titles into different dataframes for further Natural Language Processing(NLP) analysis. 

**Modelling:**

For titles, I used TFIDF Vectorizer with default stop words and ngrams of 1 and 2. This left me with 100,767 features. I used TruncatedSVD to perform dimensionality reduction, and due to CPU limitations, I could only run a TruncatedSVD of 50 components, with 5.4% of the variance explained. I then used Agglomerative Clustering with 2 clusters to create my predictions. With the help of t-SNE, I graphed the clusters with matplotlib. 

For text, I used TFIDF Vectorizer with default stop words and ended up with 61,315 features. I could only run TruncatedSVD up to 50 components with 31.7% of the variance explained without my Jupyter Notebook loading forever. I tested Agglomerative Clustering with different number of clusters. 4-5 clusters seemed to have the best results. This is due to separate clusters of [removed] and [deleted] posts, and then have the other remaining texts split into 2-3 clusters. 

**Findings:**

The results weren't clear visually, so I looked into the original data to see if I could detect any patterns. For titles, one cluster seemed to have titles that relate to improving/optimizing/setting up software/hardware, while the other cluster had titles that relate to requesting help for specific errors.

For text, with 4 clusters chosen, I could identify clusters of [removed] posts, [deleted] posts, popular posts (high score and number of comments), and unpopular posts. I decided to see if I could further cluster the regular posts with 5 clusters. With 5 clusters chosen, we have [removed] posts, [deleted] posts, one cluster of popular posts that are more learning oriented, one cluster of less popular posts that are more tech support related, and a last cluster of less popular posts related to learning. 

From the visualizations in the Jupyter Notebook, we can see that the main clusters are hard to distinguish. Although we were able to cluster very basic types of posts together, we could have done further analysis by including additional features such as time, comments, score etc. into our clustering model. Additionally, if I waited long enough for TruncatedSVD to load with more components, I may have gotten a more accurate group of clusters. 
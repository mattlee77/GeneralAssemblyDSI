# Project 7 -- Clustering Programming Posts on Reddit

Congratulations on making it halfway through the course! Project 7 is an optional task that you can attempt if you want to really dive deep on unstructured machine learning and PCA.

## Your Task

You are tasked with clustering posts on Reddit (just within subreddits dedicated to computer science and development). We would like to know if we can cluster similar types of posts together for some sort of future analysis -- are you up to the task?

## The Data

Within this repository you will find a csv containing all posts made to a specific set of subreddits (message boards) during the month of December, along with some additional data (the number of upvotes from the community, the number of comments made on the post, etc.) While reddit allows you to submit a link in place of text, this data has been subset to only self-posts (posts where the writer has submitted text instead of a link elsewhere). 

## Requirements

Submit your code (`results.py` / `results.ipynb`) and a summary (`executive_summary.md`) via pull request. We expect to see, at a minimum:

- Use of NLP techniques to create new features from the title and body of the post
- Use of a dimensionality reduction technique (PCA or TruncatedSVD)
- Use of an unstructured classification technique (K-Means, etc.) to cluster posts together
- A discussion of why you chose the number of clusters that you did 
- Visualizations that show your data and the clusters you have decided on (potentially using t-SNE)
- A discussion of the dynamics of your clusters -- what distinguishes one set of clusters from others?

You will be evaluated on the following:

1. Your application of NLP techniques to the question
2. Your use of dimensionality reduction techniques to the data
3. Your clustering technique, including how you chose your ultimate number of clusters
4. Your visualization of the clusters (a powerful communication technique as well!)
5. Your (brief!) write up in `executive_summary.md` including a description of at least one or two of your clusters and what makes them distinct (high number of words in the body text? Only Python posts? etc.) **Note**: You may need to go back and look at the raw data with the cluster labels applied as PCA-transformed columns may not be informative)

# The Anatomy of an Effective Ad: What Drives Engagement in Sponsored Social Media Content

## Project Poster

Click the poster to view the full PDF.

<a href="assets/poster.pdf">
  <img src="assets/670_poster_final.png" width="800">
</a>

## Overview

Influencer marketing has become a dominant strategy for digital advertising,
but as sponsored posts increasingly blend with organic content, audience
reactions are becoming more polarized. While brands aim to maximize marketing
efficiency, audiences often experience "ad fatigue," raising a key question:
why do some sponsored posts perform well while others fail to engage users?

This project investigates engagement dynamics in sponsored Instagram posts
through a bidirectional analytical framework that examines both content
characteristics and audience behavior. Using the Multimodal Post Attentive
Profiling (MPAP) dataset, the pipeline combines large-scale data processing,
natural language analysis, and machine learning to identify factors that
drive engagement in social media advertising.

From the content perspective, we analyze caption structure, sentiment,
hashtags, and interaction signals to understand which post features influence
engagement. From the audience perspective, we apply clustering techniques to
identify distinct audience response patterns and interpret how different
segments interact with sponsored content.

The results show that the presence of a sponsorship label does not
significantly reduce engagement, while interaction-oriented features such as
emojis and mentions improve reach. Additionally, audience analysis reveals
two distinct behavioral patterns: emotionally driven responders who produce
high engagement and pragmatically driven responders whose comments signal
purchase intent.

Together, these findings provide insights into how influencer advertising can
balance authenticity, audience engagement, and commercial intent.

## Key Findings

- Sponsorship labels do not significantly reduce engagement.
- Shorter captions are associated with higher engagement rates.
- Interaction features such as emojis and mentions positively influence reach.
- Audience responses split into two behavioral clusters:
  - **Emotional responders**: high engagement and expressive comments
  - **Pragmatic responders**: lower engagement but stronger purchase intent

## Data Access Notice

The Instagram dataset used in this project cannot be redistributed because of
Instagram’s privacy policy. The dataset was obtained directly from the
original paper’s authors.

For dataset details and access requests, please refer to the publication:

https://dl.acm.org/doi/fullHtml/10.1145/3366423.3380052

## Project Pipeline

- `project2.ipynb`  
  End-to-end data engineering pipeline that cleans raw Instagram data,
  translates captions and comments, runs RoBERTa sentiment analysis,
  enriches posts with follower counts, and exports the final dataset
  `clean_posts_ready.*`.

- `scrape_followers_single.py`  
  Selenium-based helper script that attaches to an existing Chrome session
  and scrapes follower counts for each creator. The results are saved as
  `followers_output.csv`.

- `project2_analytics.ipynb`  
  Exploratory analysis on `clean_posts_ready.csv`, including clustering,
  engagement comparisons between sponsored and non-sponsored posts,
  and feature correlation analysis.

- `project2_analytics2.ipynb`  
  Audience reaction analysis that extracts comment features, performs
  Gaussian Mixture Model clustering on active posts, and profiles
  engagement patterns across audience segments.

- `project2_analytics_model.ipynb`  
  Predictive modeling notebook that prepares numeric features, trains
  logistic regression and tree-based models for engagement-rate prediction,
  and evaluates model performance and feature importance.

## Recommended Execution Order

1. `project2.ipynb`  
   Generate cleaned and transformed datasets used in downstream analyses.

2. `scrape_followers_single.py`  
   Refresh `followers_output.csv` using Selenium when follower counts need
   to be updated.

3. `project2_analytics.ipynb`  
   Run general exploratory analyses on the prepared dataset.

4. `project2_analytics2.ipynb`  
   Perform audience segmentation and comment-level analysis.

5. `project2_analytics_model.ipynb`  
   Train predictive models and evaluate engagement-rate prediction results.

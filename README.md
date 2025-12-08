# SI670

## Data Access Notice
The Instagram dataset used in this project cannot be redistributed because of Instagram’s privacy policy; it was obtained directly from the original paper’s authors. For dataset details and access requests, please refer to the publication: https://dl.acm.org/doi/fullHtml/10.1145/3366423.3380052

## Notebook Execution Guide

### Roles

- `project2.ipynb`: End-to-end data engineering pipeline that saves `clean_posts.pkl/csv`, translates captions and comments, runs RoBERTa sentiment, enriches with follower counts, and exports `clean_posts_ready.*`.
- `scrape_followers_single.py`: Selenium helper that attaches to an existing Chrome session, scrapes follower counts for every `owner_username`, and writes `followers_output.csv` so engagement rates stay current before analytics.
- `project2_anlaytics.ipynb`: Broad exploratory analytics on `clean_posts_ready.csv`, including k-means clustering, ad vs. non-ad engagement comparisons, and feature correlation digs.
- `project2_analytics2.ipynb`: Audience-reaction module that parses cleaned comments, engineers verbosity/tone features, performs GMM clustering on active posts, and profiles each segment’s engagement/ad mix.
- `project2_analytics_model.ipynb`: Predictive modeling notebook that prepares numeric features, trains logistic/tree models for engagement-rate prediction, and reports performance plus feature influence.

### Recommended Execution Order

1. - `project2.ipynb` – Produce the cleaned/transformed datasets that power downstream work.
   - `scrape_followers_single.py` – Refresh `followers_output.csv` via Selenium before final merges/analytics whenever follower counts need an update.
3. `project2_anlaytics.ipynb` – Run the general exploratory analyses on the prepared data.
4. `project2_analytics2.ipynb` – Layer on audience/comment segmentation insights.
5. `project2_analytics_model.ipynb` – Finish with predictive modeling and interpretability.


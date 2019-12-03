# Get Stories
A simple Python demonstration of using [Streamlit](https://streamlit.io/) with the [Aylien News API](https://aylien.com/news-api/).

You can view a demo here;
https://intense-brushlands-31014.herokuapp.com/

You can modify the code to include extra sources, entities, and add support for [other parameters the Aylien News API takes](https://docs.aylien.com/newsapi/endpoints/#stories).

## Development
To run locally;
- `pip install -r requirements.txt`
- `streamlit run get_stories.py`

## Deployment
This app works well with Heroku.
- Install the Heroku CLI and set it up
- `heroku create`
- `git push heroku master`

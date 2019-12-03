import streamlit as st
import aylien_news_api
from aylien_news_api.rest import ApiException

default_source_domains = [
    'irishtimes.com',
    'nytimes.com',
    'bbc.com']
source_domains = default_source_domains + ['dailymail.co.uk', 
    'wsj.com',
    'thesun.co.uk',
    'independent.co.uk',
    'belfasttelegraph.co.uk',
    'cnn.com',
    'foxnews.com']

# Entities come from the DBPedia ontology http://mappings.dbpedia.org/server/ontology/classes/)
default_included_entity_types = ['Agent']
default_excluded_entity_types = ['FictionalCharacter', 'Deity']
entities = default_included_entity_types + default_excluded_entity_types

@st.cache
def get_stories(domain, entity_types, not_entity_types, sentiment_polarity, per_page):
    opts = {
        'language': ['en'], 
        'per_page': per_page, 
        'sentiment_title_polarity': sentiment_polarity, 
        'entities_title_type': entity_types,
        'not_entities_title_type': not_entity_types,
        'source_domain': [domain]}
    return api_instance.list_stories(**opts)

st.title('Get Stories')
st.markdown('A [simple demonstration](https://github.com/CaliberAI/streamlit-get-stories-aylien) of using [Streamlit](https://streamlit.io/) with the [Aylien News API](https://aylien.com/news-api/).')
aylien_api_key = st.text_input('Aylien API key', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
aylien_application_id = st.text_input('Aylien Application ID', 'xxxxxxxx')
included_source_domains = st.multiselect('Sources', source_domains, default_source_domains)
included_entities = st.multiselect('Included entities', entities, default_included_entity_types)
excluded_entities = st.multiselect('Excluded entities', entities, default_excluded_entity_types)
sentiment_polarity = st.radio('Sentiment polarity', ['negative', 'neutral', 'positive'])
per_page = st.number_input('Results per source', 1, 100, 10)
go = st.button('Get Stories')

if go:
    try:
        configuration = aylien_news_api.Configuration()
        configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = aylien_api_key
        configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = aylien_application_id
        api_instance = aylien_news_api.DefaultApi(aylien_news_api.ApiClient(configuration))
        stories = []
        for domain in included_source_domains:
            api_response = get_stories(domain, included_entities, excluded_entities, sentiment_polarity, per_page)
            for story in api_response.stories:
                stories += [[story.source.domain, story.title]]
        st.subheader('Stories')
        st.dataframe(stories)
    except ApiException as e:
        st.exception("Exception: %s\n" % e)

st.markdown('___')
st.markdown('by [CaliberAI](https://github.com/CaliberAI/)')
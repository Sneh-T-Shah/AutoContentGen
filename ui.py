import streamlit as st
from web_scrapp import get_article, get_urls
from content_create import ContentCreate

st.title("Welcome to the content generator app")
st.write("This app will generate content based on the given topic")

# Initialize session state variables
if 'responses' not in st.session_state:
    st.session_state.responses = None
if 'articles' not in st.session_state:
    st.session_state.articles = []
if 'citations' not in st.session_state:
    st.session_state.citations = []
if 'selected_articles' not in st.session_state:
    st.session_state.selected_articles = []
if 'selected_articles_citations' not in st.session_state:
    st.session_state.selected_articles_citations = []
if 'final_article' not in st.session_state:
    st.session_state.final_article = ""
if 'custom_prompt' not in st.session_state:
    st.session_state.custom_prompt = False

topic = st.text_input("Enter the topic you want to generate content on")
websites = st.slider("Select the number of articles to be generated", 1, 30, 1)
submit = st.button("Submit")

if submit and topic == "":
    st.write("Please enter a topic to generate content on")

if submit and topic != "":
    content = {"source": [], "content": []}
    i = 1
    st.write(f"Scraping articles for the topic... {topic}")
    while len(content["content"]) < websites:
        urls = get_urls(topic, i * 12)
        print(f"Scraping page {i}")
        print(f"Found {urls} urls")
        if urls:
            scrapped_article = 0
            for url in urls:
                try:
                    article = get_article(url)
                except:
                    print(f"Error scraping article from {url}")
                    continue
                if len(article.split(" ")) > 30:
                    scrapped_article += 1
                    content["source"].append(url)
                    content["content"].append(article)
            print(f"Scraped {scrapped_article} articles")
        i += 1
        if i > 10:
            break
    st.write("Successfully scraped the website for the articles")

    if not content["content"]:
        st.write("No articles found for the topic or unable to scrape articles")

    if content["content"]:
        content_create = ContentCreate(topic)
        st.write("Generating content for the articles....")
        content["content"] = content["content"][:websites]
        content["source"] = content["source"][:websites]
        responses = []
        for article, source in zip(content["content"], content["source"]):
            responses.append(content_create.generate_article(article, source))

        st.session_state.responses = responses
        st.session_state.citations = content["source"]
        st.session_state.responses = [f"### Article {i}:\n{response}" for i, response in enumerate(responses, start=1)]

if st.session_state.responses:
    st.write("Here is the generated content for the articles. Select the articles that you would like to incorporate in the final article\n\n")
    
    for idx, response in enumerate(st.session_state.responses):
        st.write(f"### Article {idx + 1}")
        if st.checkbox("Select this article", key=f"article_{idx}"):
            if idx not in st.session_state.selected_articles:
                st.session_state.selected_articles.append(idx)
        else:
            if idx in st.session_state.selected_articles:
                st.session_state.selected_articles.remove(idx)
        st.markdown(response)
    
    if st.button("Finalize Selection"):
        st.session_state.articles = [st.session_state.responses[idx] for idx in st.session_state.selected_articles]
        st.session_state.selected_articles_citations = [st.session_state.citations[idx] for idx in st.session_state.selected_articles]
        st.write("Selected articles for the final content:")
        for article in st.session_state.articles:
            st.markdown(article)
        
        st.session_state.custom_prompt = st.radio("Do you want to give a custom prompt for the final article?", ("Yes", "No"))
        if st.session_state.custom_prompt == "Yes":
            prompt = st.text_area("Enter the prompt for the final article", key='custom_prompt')
            st.session_state.prompt = prompt if prompt else ""
        if st.session_state.custom_prompt == "No":
            st.session_state.prompt = content_create.prompt

    if 'prompt' in st.session_state:
        if st.button("Generate Final Article", key="generate_final"):
            content_create = ContentCreate(topic)
            final_article = content_create.make_final_article(" ".join(st.session_state.articles), st.session_state.prompt)
            st.session_state.final_article = final_article
            st.write("Final article generated based on the selected articles")
            st.markdown(final_article)
            st.write("Citations for the selected articles:")
            for citation in st.session_state.selected_articles_citations:
                st.write(citation+"\n\n")
            
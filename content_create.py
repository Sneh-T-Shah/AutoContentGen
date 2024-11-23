import os
import google.generativeai as genai

class ContentCreate:
  def __init__(self, topic, api_key):
    self.topic = topic
    self.model = genai.GenerativeModel("gemini-1.5-flash")
    genai.configure(api_key=api_key)
    self.prompt = self.make_prompt()
    

  def make_prompt(self):
    prompt = self.model.generate_content(contents=f'Return me just A PROMPT TO GENERATE AN Single compiled ARTICLE BASED ON GIVEN SERIES OF ARTICLES ON THE TOPIC {self.topic}. Note:: Here articles are extracted through web scraping and does not have images or charts. Note do not give me articles just give me a prompt to generate an article based on the given series of articles.')
    return prompt.text

  def generate_article(self, article,source):
    article = self.model.generate_content(f"Here is a article about {self.topic} here is article about it: {article} from this extract the important information related to the topic also add citation to  the website {source}")
    return article.text

  def make_final_article(self, articles, prompt):
    final_article = self.model.generate_content(f"{prompt} Here are the articles: {' '.join(articles)}")  
    return final_article.text
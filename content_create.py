import os
import google.generativeai as genai

# Configure the API key outside the class (assuming it's set elsewhere)
os.environ['GEMINI_API_KEY'] = 'YOUR_API_KEY'
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

class ContentCreate:
  def __init__(self, topic):
    self.topic = topic
    self.model = genai.GenerativeModel("gemini-pro")
    self.prompt = self.make_prompt()
    

  def make_prompt(self):
    prompt = self.model.generate_content(contents=f'Return me just A PROMPT TO GENERATE AN ARTICLE BASED ON GIVEN SERIES OF ARTICLES ON THE TOPIC {self.topic}. Note:: Here articles are extracted through web scraping and does not have images or charts. Note do not give me articles just give me a prompt to generate an article based on the given series of articles.')
    return prompt.text

  def generate_article(self, article,source):
    article = self.model.generate_content(f"Here is a article about {self.topic} here is article about it: {article} from this extract the important information related to the topic also add citation to  the website {source}")
    return article.text

  def make_final_article(self, articles, prompt):
    final_article = self.model.generate_content(f"{prompt} Here are the articles: {' '.join(articles)}")  
    return final_article.text
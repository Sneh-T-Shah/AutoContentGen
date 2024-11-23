# AutoContentGen

## Description
AutoContentGen is an automatic content generator built with Python and Streamlit. It allows users to quickly generate summaries and new content based on a specified topic. Users can scrape a set number of Google search result pages, summarize the content using the Gemini language model, and generate custom articles with citations.

This tool is perfect for quickly getting up to speed on a topic, creating new content, or conducting research.

## Features
- **Automatic Web Scraping**: Specify a topic and the number of webpages to scrape.
- **Content Summarization**: Summarizes the content of the scraped webpages using the Gemini language model.
- **Custom Article Generation**: Create new articles based on custom prompts with citations to the original webpages.
- **User-Friendly Interface**: Simple and intuitive web interface built with Streamlit.

## Installation
Follow these steps to install and run AutoContentGen on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sneh-T-Shah/autocontentgen.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd autocontentgen
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run ui.py
   ```

## Usage
1. **Open the app:**
   Open your web browser and go to `http://localhost:8501`.

2. **Enter a topic:**
   Type a specific topic in the search bar and press "Enter" to apply.

3. **Specify the number of websites:**
   Use the slider to select the number of Google search result pages you want to scrape.
   
4. **Inset the Gemini api key**
   Inset the gemini api key which you can get from the google studio.

5. **Submit the topic:**
   Click the "Submit" button to start scraping and content generation.

6. **Get summaries:**
   The app will scrape the specified number of webpages, summarize their content, and display the summaries.

7. **Select preferred content:**
   Review the summaries and select the articles that align with your interests by checking the boxes.

8. **Generate a custom article:**
   Provide a custom prompt based on the selected content or use the default prompt generated by the app. Click the "Finalize Selection" button to confirm your choices.

9. **Generate the final article:**
   If you chose to provide a custom prompt, enter it in the text area. Click the "Generate Final Article" button to create the final article with citations.

## Code Explanation

### `web_scrapp.py`
This script handles the web scraping functionality. It uses the Goose3 library to extract the main text from the URLs obtained from Google search results.

### `content_create.py`
This script manages content generation using the Gemini API. It configures the API key, constructs the prompt, generates summarized articles, and creates a final article based on the selected summaries and a custom prompt.

### `ui.py`
This script sets up the Streamlit interface for user interaction. It captures user inputs, manages session states, displays the scraped and summarized content, and facilitates the final article generation process.

## Benefits
- **Ease of Setup**: The Gemini API is free for anyone to use, making it straightforward to set up and start using this project.
- **Time-Saving**: Quickly gather and summarize information on any topic, saving hours of manual research and writing.
- **Content Creation**: Generate high-quality content for blogs, research, and other writing needs effortlessly.
- **Research Tool**: Useful for students, researchers, and professionals who need to quickly synthesize information from multiple sources.

AutoContentGen empowers users to efficiently generate content and gain insights on various topics, making it a valuable tool for content creators, researchers, and anyone needing quick, reliable information synthesis.

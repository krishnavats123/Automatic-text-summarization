Automatic Text Summarization System
------------------------------------

Author: Krishna Vats  
Date: July 24, 2025  
Project Type: Web-based Extractive Text Summarizer  
Tech Stack: Flask, spaCy, Python

Overview:
---------
This project is a web-based tool designed to perform extractive summarization of large text documents. 
It is particularly useful for summarizing legal, academic, and news articles.

The system uses the TextRank algorithm and natural language processing techniques via spaCy to 
rank and select the most important sentences from the original content.

Key Features:
-------------
- Web interface for easy input of long text
- Extractive summarization using sentence ranking
- spaCy-powered sentence parsing and word frequency analysis
- Real-time summary generation
- Flask backend with basic error handling

Installation:
-------------
1. Clone the repository:
   git clone https://github.com/yourusername/flask-text-summarizer.git

2. Navigate to the project directory:
   cd flask-text-summarizer

3. (Optional) Create a virtual environment:
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Download spaCy language model:
   python -m spacy download en_core_web_sm

Running the App:
----------------
Run the Flask application:
   python app.py

Visit `http://127.0.0.1:5000/` in your browser to access the tool.

Project Structure:
------------------
- app.py              : Main Flask application
- summarizer.py       : TextRank-based summarization logic
- templates/index.html: Web form and result display (HTML)
- requirements.txt    : Python dependencies
- README.txt          : Project description and usage

Acknowledgments:
----------------
Developed by Krishna Vats in July 2025 as a personal NLP project.

License:
--------
This project is released under the MIT License. You are free to modify and use it with attribution.

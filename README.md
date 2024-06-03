
## Article Analyzer

### Description

**Article Analyzer** is a Python-based GUI application that allows users to input a URL of an article, and it fetches and analyzes the content of the article. The application extracts the article's title, authors, publication date, summary, and sentiment analysis, providing a comprehensive overview of the article's content. The GUI is built using `Tkinter` and styled with `ttkthemes` to provide a modern and user-friendly interface.

### Features

- **Fetch Article Details**: Extracts the title, authors, and publication date from the given URL.
- **Summarization**: Generates a concise summary of the article.
- **Sentiment Analysis**: Analyzes the sentiment of the article text and displays the polarity (positive, negative, or neutral).
- **Modern GUI**: Utilizes `Tkinter` and `ttkthemes` for a modern and sleek user interface.

### Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/Article-Analyzer.git
   cd Article-Analyzer
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required Python packages using `pip`.

   ```sh
   pip install -r requirements.txt
   ```

4. **Download NLTK Data**

   Ensure that you have the necessary NLTK data downloaded.

   ```python
   import nltk
   nltk.download('punkt')
   ```

### Usage

Run the `main.py` script to start the application.

```sh
python main.py
```

### Project Structure

```
Article-Analyzer/
│
├── main.py                 # Main application script
├── requirements.txt        # List of dependencies
├── README.md               # Project description and usage
└── .gitignore              # Git ignore file
```

### Code Explanation

Here is a detailed explanation of the main components of the project:

#### main.py

This is the main script that sets up and runs the Tkinter GUI.

```python
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import nltk
from textblob import TextBlob
from newspaper import Article

def summerize():
    url = urlT.get('1.0', "end").strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    p_date.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', ', '.join(article.authors))

    p_date.delete('1.0', 'end')
    p_date.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    p_date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

# Initialize nltk data
nltk.download('punkt')

root = ThemedTk(theme="breeze")
root.title('Article Analysis')
root.geometry('1200x700')
root.config(bg='#1e1e1e')

style = ttk.Style()
style.configure("TLabel", font=('Helvetica', 14, 'bold'), background='#1e1e1e', foreground='#ffffff')
style.configure("TText", font=('Helvetica', 12), background='#2e2e2e', foreground='#ffffff', padding=10)
style.configure("TButton", font=('Helvetica', 14, 'bold'), background='#1e1e1e', foreground='#ffffff')

# Title
tlabel = ttk.Label(root, text="Title")
tlabel.pack(pady=(10, 0))
title = tk.Text(root, height=1, width=140, font=('Helvetica', 12), bg='#2e2e2e', fg='#ffffff')
title.config(state='disabled')
title.pack(pady=(0, 10))

# Author
alabel = ttk.Label(root, text="Author")
alabel.pack(pady=(10, 0))
author = tk.Text(root, height=1, width=140, font=('Helvetica', 12), bg='#2e2e2e', fg='#ffffff')
author.config(state='disabled')
author.pack(pady=(0, 10))

# Publication Date
plabel = ttk.Label(root, text="Publication Date")
plabel.pack(pady=(10, 0))
p_date = tk.Text(root, height=1, width=140, font=('Helvetica', 12), bg='#2e2e2e', fg='#ffffff')
p_date.config(state='disabled')
p_date.pack(pady=(0, 10))

# Summary
slabel = ttk.Label(root, text="Summary")
slabel.pack(pady=(10, 0))
summary = tk.Text(root, height=10, width=140, font=('Helvetica', 12), bg='#2e2e2e', fg='#ffffff')
summary.config(state='disabled')
summary.pack(pady=(0, 10))

# Sentiment Analysis
selabel = ttk.Label(root, text="Sentiment Analysis")
selabel.pack(pady=(10, 0))
sentiment = tk.Text(root, height=1, width=140, font=('Helvetica', 12), bg='#2e2e2e', fg='#ffffff')
sentiment.config(state='disabled')
sentiment.pack(pady=(0, 10))

# URL Input
ulabel = ttk.Label(root, text="URL here")
ulabel.pack(pady=(10, 0))
urlT = tk.Text(root, height=1, width=140, font=('Helvetica', 12), bg='#2e2e2e', fg='#ffffff')
urlT.pack(pady=(0, 10))

# Summarize Button
button = ttk.Button(root, text='Summarize', command=summerize)
button.pack(pady=(10, 20))

root.mainloop()
```

### requirements.txt

This file lists the dependencies needed to run the project.

```
tkinter
ttkthemes
nltk
textblob
newspaper3k
```

### .gitignore

This file ensures that unnecessary files are not committed to the repository.

```
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
```

### Additional Notes

- Make sure to activate the virtual environment each time before running the project.
- Keep the `requirements.txt` file updated with any new dependencies.
- For contributions, please create a pull request and ensure your code follows the project's coding standards.

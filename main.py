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

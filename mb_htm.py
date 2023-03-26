import requests
from bs4 import BeautifulSoup

# Define the list of URLs to scrape
urls = ['https://motherbrain.ai/introducing-motherbrain-big-data-machine-learning-meets-private-equity-1635f417bac0',
        'https://motherbrain.ai/using-deep-learning-to-find-the-next-unicorn-a-practical-synthesis-272dc7e85cb5',
        'https://motherbrain.ai/predicting-revenue-for-scaleup-companies-5b07ec7a38cf',
        'https://motherbrain.ai/disrupting-private-capital-using-machine-learning-and-an-event-driven-architecture-a966c66ac93a',
        'https://motherbrain.ai/applying-transformers-to-score-potentially-successful-startups-7893284efb01',
        'https://motherbrain.ai/the-voyage-towards-gpt-enabled-m-a-3aa431a60792']

# Create a new HTML file
with open('articles.html', 'w', encoding='utf-8') as f:
    # Write the HTML boilerplate code
    f.write('''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Article Scraping Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
            }
            h1 {
                font-size: 36px;
                margin-bottom: 0.5em;
            }
            .article {
                margin-bottom: 3em;
            }
            .article h2 {
                font-size: 24px;
                margin-bottom: 0.5em;
            }
            .article p {
                font-size: 16px;
                margin-bottom: 1em;
            }
        </style>
    </head>
    <body>
    ''')

    # Loop through each URL in the list and scrape the article text
    for url in urls:
        # Make a request to the URL
        response = requests.get(url)

        # Parse the HTML response with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the article element and extract the title and text
        article = soup.find('article')
        title = article.find('h1').text
        text = ''
        for p in article.find_all('p'):
            text += p.text + '\n'

        # Write the article to the HTML file
        f.write(f'<div class="article">\n')
        f.write(f'<h2>{title}</h2>\n')
        f.write(f'<p>{text}</p>\n')
        f.write(f'</div>\n')

    # Write the HTML closing tags
    f.write('''
    </body>
    </html>
    ''')

# Import necessary libraries
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

# Initializing Flask application
app = Flask(__name__)

# Defining main route for the web application
@app.route('/', methods=['GET', 'POST'])
def home():
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the URL from the form input
        url = request.form.get('url')
        if url:
            try:
                # Sending GET request to the provided URL
                r = requests.get(url)
                # Parse the HTML content of the page
                soup = BeautifulSoup(r.content, 'html.parser')

                # Extract the page title
                title = soup.title.string
                # Extract first 3 paragraphs of text
                paragraphs = [p.get_text() for p in soup.find_all('p')[:3]]

                # Render the result template with extracted data
                return render_template('result.html', title=title, paragraphs=paragraphs)

            except requests.exceptions.RequestException as e:
                # Handle exceptions and show an error message
                error = f"An error occurred: {e}"
                return render_template('home.html', error=error)
    # Render the main page template
    return render_template('home.html')


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
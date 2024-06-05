# Web Scraping Using Flask

## Overview

This is a basic web application built with Flask framework that allows users to input a URL, scrape the web page's title and first 3 paragraphs of text, and display the results.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/`: Contains the HTML templates.
- `static/`: Contains static files like CSS.
- `requirements.txt`: Lists the project dependencies.
- `README.md`: Documentation for the project.

## Setup
1. Clone the repository.
2. Navigate to the project directory.
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    python app.py
    ```

5. Open your browser and go to `http://127.0.0.1:5000`.

## Explanation and Comments
1. **`app.py`**:
    - The Flask app is created and routes are defined.
    - On the `GET` request to the root URL, the `home.html` template is rendered.
    - On the `POST` request, the URL from the form is fetched, and the web page content is scraped using `requests` and `BeautifulSoup`.
    - The title and the first three paragraphs are extracted and passed to the `result.html` template for rendering.
    - Any errors during the request are caught and displayed on the `home.html` page.

2. **`home.html`**:
    - Contains a form for the user to input a URL.
    - Submits the form to the same route, handling errors if any.
    - Provides a button to clear the input field.

3. **`result.html`**:
    - Displays the scraped title and paragraphs.
    - Provides a button to go back to the home page..

4. **`style.css`**:
    - Adds basic styling to the pages for better readability.

## Running the Application
To run the Flask application, navigate to the project directory and execute:
```bash
python app.py

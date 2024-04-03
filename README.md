## LLM Explorer - Find the LLM You Need

### Description:
The LLM Explorer application helps users find the Legal Language Model (LLM) they need for specific legal tasks. It provides a user interface where users can search for LLMs based on their requirements and view the search results with pagination.




# LLM Explorer

LLM Explorer is a Streamlit application that helps users find the Legal Language Model (LLM) they need for specific legal tasks. It provides information and comparisons of different LLMs based on user requirements.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/KeenSightStreamLit/llm-explorer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd llm-explorer
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the Streamlit app, execute the following command:

```bash
streamlit run app.py
```

## Features

- Search for LLM by entering keywords in the search box.
- Paginate through search results to view more models.
- Each search result includes a link to the model for further exploration.






### Components:
1. **Search Input Box:**
   - A text input box where users can enter their search query to find LLMs.
   
2. **Search Results:**
   - Displays the search results based on the user's search query.
   - Each search result is a clickable link that redirects users to the corresponding LLM model page.
   - Supports pagination to navigate through multiple pages of search results.

3. **Pagination:**
   - Allows users to navigate through the search results using pagination controls.
   - Users can input the page number directly or use the "Back" and "Next" buttons to navigate between pages.

4. **Footer:**
   - Displays the data source attribution, linking to Hugging Face website.

### Functionality:
- Users can enter their search query in the search input box.
- The application filters the LLMs based on the search query and displays the search results.
- Search results are paginated, with each page displaying up to 10 search results.
- Users can navigate through the search results using pagination controls.
- Clicking on a search result link redirects users to the corresponding LLM model page.

### Usage:
1. Enter a search query in the search input box.
2. Browse through the search results.
3. Navigate between pages using pagination controls.
4. Click on a search result link to view more details about the LLM model.

### Data Source:
- The application fetches data from a JSON file containing information about various Legal Language Models.
- Data source attribution is provided in the footer, linking to the Hugging Face website.


import streamlit as st
import json

# Load JSON data
with open("list.json", "r") as f:
    data = json.load(f)

# Function to filter data based on search query
def filter_data(search_query):
    return [item for item in data if search_query.lower() in item["Model Name"].lower()]

# Streamlit app
def main():
    st.image("logo.png", width=200)
    st.title("LLM Explorer - Find the LLM You Need")

    # Search input box
    search_query = st.text_input("Search for LLM")

    if search_query is not None:
        # Filter data based on search query
        filtered_data = filter_data(search_query)

        # Pagination
        if filtered_data:
            num_results = len(filtered_data)
            num_pages = (num_results // 10) + 1 if num_results % 10 != 0 else num_results // 10
            current_page = st.number_input("Page", min_value=1, max_value=num_pages, value=1)
           

            start_index = (current_page - 1) * 10
            end_index = min(start_index + 10, num_results)

            st.subheader("Search Results")
            for item in filtered_data[start_index:end_index]:
                st.markdown(f"[{item['Model Name']}]({item['Link']})")
                

            st.write(f"Showing results {start_index + 1} to {end_index} out of {num_results}")

           
        else:
            st.write("No matching results found.")

    # Footer
    st.markdown("---")
    st.markdown("Data source: [Hugging Face](https://huggingface.co)")

if __name__ == "__main__":
    main()

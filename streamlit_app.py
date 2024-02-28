import streamlit as st
from google.generativeai import configure, GenerativeModel

# Configure the Generative AI
configure(api_key="AIzaSyDlBFVsmV8pao6Ax-bcR0dc5h4CusiNCsc")
model = GenerativeModel(model_name="gemini-pro")

def prompt(movie_title):
    prompt_parts = [
        f"You are an assistant that helps users find information about movies.\n\nMovie Title={movie_title}",
    ]
    return prompt_parts

def generate_info_about(movie_title, prompt=prompt, model=model):
    human_prompt = prompt(movie_title)
    response = model.generate_content(human_prompt)
    parts = response.candidates[0].content.parts
    text = "".join(part.text for part in parts)
    return text

def main():
    st.title("Movie Information Assistant")

    # Input box for movie title
    movie_title = st.text_input("Enter a movie title:", "")

    if st.button("Generate Information"):
        if movie_title:
            # Generate information
            info = generate_info_about(movie_title)
            # Display the information in a box
            st.info(info)
        else:
            st.error("Please enter a movie title.")

if __name__ == "__main__":
    main()

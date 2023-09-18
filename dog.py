import streamlit as st
import requests

# Fetch a random dog image from a specific breed
def fetch_random_dog_image(breed=None):
    if breed:
        url = f"https://dog.ceo/api/breed/{breed}/images/random"
    else:
        url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()
    return data["message"]

# Get a list of all available dog breeds
def get_dog_breeds_list():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    data = response.json()
    return list(data["message"].keys())

# Streamlit app
def main():
    st.title("Random Dog Image")

    # Create a radio button for breed selection
    breed_option = st.radio("Select an option:", ("Random Dog Image", "Select a Dog Breed"))

    if breed_option == "Select a Dog Breed":
        # Create a dropdown menu to select a dog breed
        dog_breeds = get_dog_breeds_list()
        selected_breed = st.selectbox("Select a Dog Breed", dog_breeds)

        # Create a button to fetch a random dog image for the selected breed
        if st.button("Fetch Random Dog Image"):
            st.text(f"Fetching a random {selected_breed} dog image...")
            image_url = fetch_random_dog_image(selected_breed)

            # Display the fetched dog image
            st.image(image_url, caption=f"Random {selected_breed} Dog Image", use_column_width=True)
    else:
        # Create a button to fetch a completely random dog image
        if st.button("Fetch Random Dog Image"):
            st.text("Fetching a completely random dog image...")
            image_url = fetch_random_dog_image()

            # Display the fetched dog image
            st.image(image_url, caption="Random Dog Image", use_column_width=True)

if __name__ == "__main__":
    main()

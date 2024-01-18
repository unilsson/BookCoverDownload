import requests
import os

def download_book_cover(isbn, save_path="."):
    # Google Books API URL
    api_url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"

    try:
        # Make the request to the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad responses

        # Parse the JSON response
        book_data = response.json()

        # Check if any items were found
        if "items" in book_data and len(book_data["items"]) > 0:
            volume_info = book_data["items"][0]["volumeInfo"]

            # Get the cover image URL
            image_links = volume_info.get("imageLinks", {})
            cover_url = image_links.get("thumbnail", "")

            if cover_url:
                # Download the cover image
                cover_response = requests.get(cover_url)
                cover_response.raise_for_status()

                content_type = cover_response.headers["Content-Type"]
                file_extension = content_type.split("/")[-1]

                save_filename = f"{isbn}_cover.{file_extension}"
                print(save_filename)
                save_path = os.path.join(save_path, save_filename)

                with open(save_path, "wb") as file:
                    file.write(cover_response.content)

                print(f"Book cover downloaded and saved: {save_path}")
            else:
                print("No cover image found for the book.")
        else:
            print("No book found with the given ISBN.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
# Hard-boiled wonderland and the end of the world by Haruki Murakami
isbn = "1448103681"
download_book_cover(isbn, save_path=".")

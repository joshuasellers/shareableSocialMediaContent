import instaloader

# Create an Instaloader instance
L = instaloader.Instaloader()

# Define the post URL
post_url = "https://www.instagram.com/p/DRtGmBrD1Az/" # Replace with the actual URL

try:
    # Extract the shortcode from the URL
    shortcode = post_url.split("/")[-2]

    # Retrieve the post metadata
    post = instaloader.Post.from_shortcode(L.context, shortcode)

    # Download the post (image/video and metadata)
    # The second argument specifies the target directory name
    L.download_post(post, "instagram_downloads")
    print(f"Post {shortcode} downloaded successfully into 'instagram_downloads' folder.")

except Exception as e:
    print(f"An error occurred: {e}")


import instaloader

# Initialize Instaloader
L = instaloader.Instaloader()

# OPTIONAL: Login if the profile is private or for consistent access (session cookies are stored)
# L.context.log_in("your_username", "your_password")

# Get the post object from its shortcode (the last part of the URL)
# Example shortcode "BFB6znLg5s1" from a full URL
post_shortcode = "YOUR_POST_SHORTCODE_HERE"
post = instaloader.Post.from_shortcode(L.context, post_shortcode)

# Check if the post is a video and download it
if post.is_video:
    print(f"Downloading video from: {post.video_url}")
    # This downloads the video file to the current directory
    L.download_post(post, target=post.owner_username)
else:
    print("The specified post is not a video.")
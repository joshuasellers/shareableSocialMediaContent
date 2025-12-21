import requests
import instaloader
import sys


def IDL(url,name) -> None:
    obj = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(obj.context, url.split('p/')[1].strip('/ '))
    photo_url = post.url
    video_url = post.video_url
    if video_url:
        response = requests.get(video_url)
        with open("./vids/"+"insta"+name+".mp4", "wb") as f:
            f.write(response.content)
    elif photo_url:
        response = requests.get(photo_url)
        with open("./vids/"+"insta" +name+".jpg", "wb") as f:
            f.write(response.content)


def main(args):
    for i in range(0, len(args)):
        IDL(args[i], "media" + i)


if __name__ == "__main__":
    main(sys.argv[1:])

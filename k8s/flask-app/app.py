from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/1.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/2.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/3.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/4.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/5.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/6.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/7.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/8.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/9.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/10.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/11.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

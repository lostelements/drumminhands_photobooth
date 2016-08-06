from flask import Flask, render_template
import os, random
app = Flask(__name__, static_url_path = "/wedding", static_folder = "wedding")

@app.route("/")
def hello():
    
    templateData = {
        'title' : 'HELLO!',
        'gif_url' : '/wedding/' + random.choice(os.listdir("/mnt/slides/wedding"))
        }
    return render_template('projector.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
    

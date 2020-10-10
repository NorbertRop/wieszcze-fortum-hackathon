from flask import Flask, render_template
app = Flask(__name__, static_url_path="/templates")
app._static_folder ='/front-flask\static'

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
   app.run()
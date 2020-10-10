from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return app.send_static_file('templates/index.html')

if __name__ == '__main__':
   app.run()
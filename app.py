
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>DevOps Mini Project</title></head>
    <body style="font-family:Arial;text-align:center;margin-top:100px">
        <h1>Automated CI/CD Pipeline</h1>
        <h2>Application Deployed Successfully!</h2>
        <p>Technologies: Jenkins, Docker, GitHub and Flask</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

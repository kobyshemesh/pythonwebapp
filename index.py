from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Kubernetes on vSphere! #tanzu #vmware @KobiShamama @OdedShopen!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)

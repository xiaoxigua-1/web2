from flask import Flask,request
app = Flask(__name__)
@app.route("/")
def pp():
    print("p")
    return "87"
def main():#????
    if __name__ == "__main__":
        print("開啟中")
        app.run()
main()
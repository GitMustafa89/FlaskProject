from flask import Flask, render_template, request

app = Flask(__name__)

#home page
@app.route("/")
def home():
    return render_template("home.html")

#About page
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")


# Getting User Input 
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    
    else:
        First_Num= float(request.form["First_Num"])
        Second_Num= float(request.form["Second_Num"])

        
        addition= First_Num+Second_Num 
        substraction= First_Num-Second_Num
        multiplication= First_Num*Second_Num
        division= First_Num/Second_Num
        
        return render_template("home.html", result=addition, result1=substraction, result2=multiplication, result3=division)

if __name__ == "__main__":
    app.run(debug=True)
    
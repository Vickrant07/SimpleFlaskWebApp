from flask import Flask, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"

#1.
@app.route("/spy", methods=["GET", "POST"])
def spy():
    if request.method == "GET":
        return render_template("spy_form.html")
    else:
        given_name = request.form["given_name"]
        family_name = request.form["family_name"]
        return render_template("spy_response.html", given_name=given_name, family_name=family_name)

#2.
@app.route("/morse", methods=["GET", "POST"])
def morse():
    if request.method == "GET":
        return render_template("morse_form.html")
    else:
        message = request.form["message"]
        cleaned_message = message.upper().replace(" ", "")
        if cleaned_message == "":
            return render_template("morse_form.html", error="Error: Please type in a message")
        morse = ""
        morse_dict = {
            "A": ".-",      "G":"--.",      "M":"--",      "S":"...",     "Y":"-.--",     "5":".....",
            "B": "-...",    "H":"....",     "N":"-.",      "T":"-",       "Z":"--..",     "6":"-....",
            "C": "-.-.",    "I":"..",       "O":"---",     "U":"..-",     "1":".----",    "7":"--...",
            "D": "-..",     "J":".---",     "P":".--.",    "V":"...-",    "2":"..---",    "8":"---..",
            "E": ".",       "K":"-.-",      "Q":"--.-",    "W":".--",     "3":"...--",    "9":"----.",
            "F": "..-.",    "L":".-..",     "R":".-.",     "X":"-..-",    "4":"....-",    "0":"-----", 
        }
        for char in cleaned_message:
            if char not in morse_dict:
                return render_template("morse_form.html", error="Error: Invalid character was/were entered")
            else:
                code = morse_dict[char]
                morse = morse + code + " "
        return render_template("morse_response.html", message=message, morse=morse)

#3.
@app.route("/lengths", methods=["GET", "POST"])
def lengths():
    if request.method == "GET":
        return render_template("lengths_form.html")
    else:
        inches = request.form["inches"]
        centimeters = request.form["centimeters"]
        if inches != "" and centimeters != "":
            return render_template("lengths_form.html", inches=inches, centimeters=centimeters, error="Error: OMG, please only enter any one of them! Not both!")
        elif inches != "" and centimeters == "":
            inches = float(inches)
            centimeters = inches * 2.54
            return render_template("lengths_form.html", inches=inches, centimeters=centimeters)
        elif inches == "" and centimeters != "":
            centimeters = float(centimeters)
            inches = centimeters / 2.54
            return render_template("lengths_form.html", inches=inches, centimeters=centimeters)
        else: #both fields are empty
            return render_template("lengths_form.html", inches=inches, centimeters=centimeters, error="Error: Would you please enter any one!")


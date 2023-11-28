from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["user_message"]
    bot_response = generate_response(user_message)
    return jsonify({"bot_response": bot_response})

def generate_response(user_message):
    # Simple logic for generating responses
    if "java" in user_message.lower():
        return "We offer Java programming courses. What specific information do you need?"
    elif "python" in user_message.lower():
        return "Our Python courses cover both beginner and advanced topics. What do you want to know?"
    elif "c++" in user_message.lower():
        return "Learn C++ with our comprehensive courses. What would you like to inquire about C++?"
    elif "web development" in user_message.lower():
        return "Explore our web development courses to master HTML, CSS, and JavaScript. What specifics are you interested in?"
    elif "ms office" in user_message.lower():
        return "We provide Microsoft Office courses covering Word, Excel, and PowerPoint. What do you need assistance with?"
    elif "amazon va" in user_message.lower():
        return "Our Amazon Virtual Assistant courses help you navigate tasks efficiently. What can I help you with?"
    elif "contact number" in user_message.lower():
        return "yes you can contact on +92 322 8499993 300 4870104?"
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase or ask a different question?"

if __name__ == "__main__":
    app.run(debug=True)

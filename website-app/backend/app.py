from flask import Flask, jsonify
import random

app = Flask(__name__)

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "There are 10 types of people: those who understand binary and those who don’t.",
    "I told my computer I needed a break, and it said no problem --> it froze.",
    "Why do Java developers wear glasses? Because they don’t see sharp.",
    "Debugging: being the detective in a crime movie where you are also the murderer.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
    "Why did the developer go broke? Because he used up all his cache.",
    "I would tell you a UDP joke, but you might not get it.",
    "Why was the computer cold? It left its Windows open.",
    "Why do Python programmers prefer snakes? Because they don’t like Java.",
    "What is a programmer’s favorite hangout place? Foo Bar.",
    "Why did the function return early? Because it had a date.",
    "Why did the developer get lost? Because he didn’t follow the path.",
    "Why do programmers hate nature? Too many bugs.",
    "Why did the computer show up at work late? It had a hard drive.",
    "Why do programmers always mix up Halloween and Christmas? Because 31 OCT = 25 DEC.",
    "Why was the developer unhappy at their job? They wanted arrays.",
    "Why did the code break up? Too many arguments.",
    "Why don’t programmers like to go outside? The real world has no debugger.",
    "Why was the variable sad? Because it couldn’t change."
]

@app.route("/message")
def message():
    return jsonify({"joke": random.choice(JOKES)})

app.run(host="0.0.0.0", port=5000)
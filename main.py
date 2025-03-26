from flask import Flask, jsonify
import os

app = Flask(__name__)

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


@app.route('/')
def index():
    contacts = []
    
    cris = Contact("Cristian Cardoso", "+525523457687")
    santi = Contact("Santiago Amezcua", "+525567879687")
    mario = Contact("Mario Centeno", "+5234543321")
    gerry = Contact("Gerardo Cornejo", "+52455565465")

    contacts.append(cris)
    contacts.append(santi)
    contacts.append(mario)
    contacts.append(gerry)
    
    return jsonify(contacts)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

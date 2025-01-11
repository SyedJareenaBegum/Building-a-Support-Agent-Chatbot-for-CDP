from flask import Flask, request, jsonify 
import requests 
from bs4 import BeautifulSoup 
app = Flask(__name__)
 # Example function to extract info from Segment documentation 
 def get_segment_info(question): 
    url = "https://segment.com/docs/" response = requests.get(url) 
 soup = BeautifulSoup(response.text, 'html.parser') 
 # Logic to find the answer in the documentation 
 return "Answer to: " + question
  @app.route('/api/chat', methods=['POST'])
   def chat(): 
    data = request.json 
    question = data.get('question') 
    if "segment" in question.lower():
         answer = get_segment_info(question)
          elif "mparticle" in question.lower(): 
            answer = "mParticle info" # Add function to get info
             elif "lytics" in question.lower(): 
                answer = "Lytics info" # Add function to get info 
                elif "zeotap" in question.lower(): 
                answer = "Zeotap info" # Add function to get info 
                else: 
                answer = "I can only answer questions about Segment, mParticle, Lytics, and Zeotap." 
                return jsonify({"answer": answer})
                 if __name__ == '__main__': 
                    app.run(debug=True)
import React,
 { useState } from 'react'; 
 import './App.css'; 
 function App() 
 { const [question, setQuestion] = useState('');
     const [answer, setAnswer] = useState('');
      const handleSubmit = async (e) => {
         e.preventDefault(); 
         const response = await fetch('/api/chat', { 
            method: 'POST', headers: { 
                'Content-Type': 'application/json',
             }, 
             body: JSON.stringify({ question }), 
            }); 
            const data = await response.json(); 
            setAnswer(data.answer); 
        }; 
        return ( 
        <div className="App"> 
        <header className="App-header"> 
            <h1>CDP Chatbot</h1>
             <form onSubmit={handleSubmit}>
                 <input 
                 type="text" value={question} 
                 onChange={(e) => setQuestion(e.target.value)} 
                 placeholder="Ask a question about Segment, mParticle, Lytics, or Zeotap" 
                 /> 
                 <button type="submit">Ask</button>
                  </form>
                   {answer && <p>{answer}</p>} 
                   </header>
                    </div> 
                    ); 
                } 
                export default App;
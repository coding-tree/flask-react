
import React, { useState } from "react";
import logo from './logo.svg';
import './App.css';

function App() {
  const [message, setMessage] = useState("START");

  setTimeout(() => {
    fetch("http://localhost:3000/hello")
      .then(res => {
        return res.text();
      })
      .then(response => {
        console.log(response);
        setMessage(response);
      });
  }, 3000);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React {message}
        </a>
      </header>
    </div>
  );
}

export default App;

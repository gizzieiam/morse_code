import React from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './login'

function App() {
  return (
    <div className="App">
      <Login 
        greeting='Welcome Back!'
        signup='Create an account!'
      />
    </div>
  );
}

export default App;

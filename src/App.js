import React, { Component } from 'react'
import logo from './logo.svg';
import './App.css';
import Greet from './components/Greet'
//import MyComponent from './components/Greet'
//import { Greet } from './components/Greet'
import Welcome from './components/Welcome'
import Hello from './components/Hello'
import Message from './components/Messsage'
import Counter from './components/Counter'
import FunctionClick from './components/FunctionClick'
import ClassClick from './components/ClassClick'

function App() {
  return (
    <div className="App">
    <ClassClick/>
    {/* <FunctionClick/> */}
    {/* <Counter/>
    <Message/>
      <MyComponent/>
      <Greet/>
      <Welcome/> 
      <Hello/>
      
      <Greet name="Bruce" heroName="Batman">
        <p> This is children props</p>
      </Greet>
      <Greet name="Clark" heroName="Superman">
      <button>action</button>
      </Greet>
      <Greet name="Diana" heroName="Wonder Woman"/>
    
      <Welcome name="Bruce" heroName="Batman"></Welcome>
      <Welcome name="Clark" heroName="Superman"></Welcome>
      <Welcome name="Diana" heroName="Wonder Woman"></Welcome> */}
    </div>
  );
}

export default App;

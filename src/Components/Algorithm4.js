import React, { Component, useState } from 'react'
import axios from 'axios'
import { useHistory } from 'react-router-dom';


function Algorithm4(props) {
    let History = useHistory()
    let [FileNum1, setFilename] = useState()
    const [answer, setanswer] = useState()

  React.useEffect(() => {
    console.log("Call 1")
        axios.get("http://localhost:5000/Algorithm", {
            params: {
                AlgoNum: "2",
                FileNum: FileNum1
            }
        }).then(res => { 
           setanswer(res.data.answer) 
         
        }).catch(err => {
            console.error(err);
        })
    }, [FileNum1]);

  return (
    <div  className = "container">
            <h1 className = "Header2">
           Longest Increasing Subsequence
            </h1>
            <div>
            <div>
            <h1 className = "Header3">
                Click on File to Run Project On
            </h1>
            </div>
            <button className = "Button11" onClick = {() => setFilename(0)}> 
            File 1
            </button>

            </div>
            <div>
             <button className = "Button11" onClick = {() => setFilename(1)}> 
            File 2
            </button>
            </div>
            <div>
             <button className = "Button11" onClick = {() => setFilename(2)}> 
            File 3
            </button>
            </div>
            <div>
            <button className = "Button11" onClick = {() => setFilename(3)}> 
            File 4
            </button>
            </div>
            <div>
             <button className = "Button11" onClick = {() => setFilename(4)}> 
            File 5
            </button>
            </div>
            <div>
             <button className = "Button11" onClick = {() => setFilename(5)}> 
            File 6
            </button>
            </div>
            <div>
            <button className = "Button11" onClick = {() => setFilename(6)}> 
            File 7
            </button>
            </div>
            <div>
           <button className = "Button11" onClick = {() => setFilename(7)}> 
            File 8
            </button>
            </div>
            <div>
            <button className = "Button11" onClick = {() => setFilename(8)}> 
            File 9
            </button>
            </div>
            <div>
             <button className = "ButtonEnd1" onClick = {() => setFilename(9)}> 
            File 10
            </button>
            </div>
            
           <div className = "container1">
            <h1 className = "Header4">Output:</h1>
              <div>
              <p className= "Header5">{answer}</p>
              </div>
            </div>
            </div>
  );
}

export default Algorithm4;

import React from 'react'
import { useHistory } from 'react-router-dom';

function HomeScreen(props) {
    let History = useHistory()
    console.log(props)
    return (
    <div className = "container">
            <div>
            <h1 className = "Header">
                Algorithm Project
            </h1>
            </div>
               
            <div>
            <h1 className = "Header1">
                Click on Project To Run
            </h1>
            </div>
            <div>
            <button className = "Button1" onClick = {() => {
                History.push("/Algorithm1")}}>
            Longest Common Subsequence Problem
            </button>
            </div>
            
            <div>
            <button className = "ButtonStart" onClick = {() => {
                History.push("/Algorithm2")
            }}> 
            Shortest Common Subsequence Problem
            </button>
            </div>
            <div>
            <button className = "ButtonStart" onClick = {() => {
                History.push("/Algorithm3")
            }}> 
            Levenshtein Distance (edit-distance) Problem
            </button>
            </div>
            <div>
            <button className = "ButtonStart" onClick = {() => {
                History.push("/Algorithm4")
            }}> 
            Longest Increasing Subsequence Problem
            </button>
            </div>
            <div>
            <button className = "ButtonStart" onClick = {() => {
                History.push("/Algorithm5")
            }}> 
            Matrix Chain Multiplication (Order) Problem
            </button>
            </div>
            <div>
            <button className = "ButtonStart" onClick = {() => {
                History.push("/Algorithm6")
            }}> 
            0-1-knapsack Problem
            </button>
            </div>
            <div>
            <button className = "ButtonStart" onClick = {() => {
                History.push("/Algorithm7")
            }}> 
            Partition Problem
            </button>
            </div>
            <div>
            <button className = "ButtonStart" onClick = {() => {
                History.push("/Algorithm8")
            }}> 
            Rod Cutting Problem
            </button>
            </div>
            <div>
            <button className = "ButtonStart" onClick = {() => {
                History.push("/Algorithm9")
            }}> 
            Coin-change-making Problem
            </button>
            </div>
            <div>
            <button className = "ButtonEnd" onClick = {() => {
                History.push("/Algorithm10")
            }}> 
            Word Break Problem 
            </button>
            </div>
 <div className = "container1">
            <h1 className = "Header4">Made By:</h1>
              <div>
              <p className= "Header5">Izaan Sohail 18K-0162 <br/> Maria AliAsghar 18K-0161> </p>
              </div>
            </div>

            </div>
    )
}

export default HomeScreen

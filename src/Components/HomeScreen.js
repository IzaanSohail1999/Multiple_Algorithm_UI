import React from 'react'
import './HomeScreen.css'
import { useHistory } from 'react-router-dom';

function HomeScreen(props) {
    let History = useHistory()
    console.log(props)
    return (
        <body className = "container">
    <div>
            <h1 className = "Header">
                Algorithm Project
            </h1>
            <div>
            
            <button className = "ButtonStart" onClick = {() => {
                History.push("/Algorithm1")}}>
            Longest Common Subsequence
            </button>
            </div>
            <div>
            <button className = "Button1" onClick = {() => {
                History.push("/Algorithm2")
            }}> 
            Shortest Common Subsequence
            </button>
            </div>
            <div>
            <button className = "Button1" onClick = {() => {
                History.push("/Algorithm3")
            }}> 
            Levenshtein Distance (edit-distance)
            </button>
            </div>
            <div>
            <button className = "Button1" onClick = {() => {
                History.push("/Algorithm4")
            }}> 
            Longest Increasing Subsequence
            </button>
            </div>
            <div>
            <button className = "Button1" onClick = {() => {
                History.push("/Algorithm5")
            }}> 
            Matrix Chain Multiplication (Order)
            </button>
            </div>
            <div>
            <button className = "Button1" onClick = {() => {
                History.push("/Algorithm6")
            }}> 
            0-1-knapsack-problem
            </button>
            </div>
            <div>
            <button className = "Button1" onClick = {() => {
                History.push("/Algorithm7")
            }}> 
            Partition-problem
            </button>
            </div>
            <div>
            <button className = "Button1" onClick = {() => {
                History.push("/Algorithm8")
            }}> 
            Rod Cutting Problem
            </button>
            </div>
            <div>
            <button className = "Button1" onClick = {() => {
                History.push("/Algorithm9")
            }}> 
            Coin-change-making-problem
            </button>
            </div>
            <div>
            <button className = "ButtonEnd" onClick = {() => {
                History.push("/Algorithm10")
            }}> 
            Word Break Problem 
            </button>
            </div>
            </div>
            </body>
    )
}

export default HomeScreen

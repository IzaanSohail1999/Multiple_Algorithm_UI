import React, { Component } from 'react'
import './App.css';
import { BrowserRouter,Switch, Route } from 'react-router-dom';
import HomeScreen from './Components/HomeScreen'
import Algorithm1 from './Components/Algorithm1'
import Algorithm2 from './Components/Algorithm2'
import Algorithm3 from './Components/Algorithm3'
import Algorithm4 from './Components/Algorithm4'
import Algorithm5 from './Components/Algorithm5'
import Algorithm6 from './Components/Algorithm6'
import Algorithm7 from './Components/Algorithm7'
import Algorithm8 from './Components/Algorithm8'
import Algorithm9 from './Components/Algorithm9'
import Algorithm10 from './Components/Algorithm10'



function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path = "/"  exact> <HomeScreen/> </Route>
        <Route path = "/Algorithm1"  exact> <Algorithm1/> </Route>
        <Route path = "/Algorithm2"  exact> <Algorithm2/> </Route>
        <Route path = "/Algorithm3"  exact> <Algorithm3/> </Route>
        <Route path = "/Algorithm4"  exact> <Algorithm4/> </Route>
        <Route path = "/Algorithm5"  exact> <Algorithm5/> </Route>
        <Route path = "/Algorithm6"  exact> <Algorithm6/> </Route>
        <Route path = "/Algorithm7"  exact> <Algorithm7/> </Route>
        <Route path = "/Algorithm8"  exact> <Algorithm8/> </Route>
        <Route path = "/Algorithm9"  exact> <Algorithm9/> </Route>
        <Route path = "/Algorithm10"  exact> <Algorithm10/> </Route>
      </Switch>
    </BrowserRouter>
    
  );
}

export default App;
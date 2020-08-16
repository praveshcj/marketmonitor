import React, {useEffect, useState, Component} from 'react';
import logo from './logo.svg';
import './App.css';
import {Button} from 'react-bootstrap';

class App extends Component {

  state = {
    currenttime: 0, 
  }
 

  get_all_data = async ()=>{
    await fetch('/get_ma').then(res => res.json()).then(data => {
      console.log(data);
    })
  }

  render () {
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
          Learn React
        </a>
        <p>The current time is {this.state.currenttime}.</p>
      </header>
      <Button onClick={this.get_all_data}>Get all Data</Button>
    </div>
  );
  }
}

export default App;

import React, { Component } from 'react';

import Header from './structure/Header';
import Footer from './structure/Footer';
import Camp from './mainscreen/Camp';
import Board from './mainscreen/Board'

import './App.css';

interface myProps {}
interface myState { height: number }

class App extends Component<myProps, myState> {

  constructor(props: myProps) {
    super(props)
    this.state = { height: window.innerHeight }
  }

  render() {
    return (
      <div className="App">
        <Header />
        <div>
          <div className="container-fluid">
            <div className="row" style={{ height: this.state.height - 110, marginTop: 30 }}>
              <div className="col-4 Info"> 
                <Board />
              </div>
              <div className="col-1"></div>
              <div className="col-7" id="Game">
                <Camp height={this.state.height - 110} />
              </div>
            </div>
          </div>
        </div>
        <Footer />
      </div >
    );
  }
}

export default App;

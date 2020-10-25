import React, { Component } from 'react'
import './App.css';
import Header from './structure/Header';
import Footer from './structure/Footer';
import Camp from './mainscreen/game/Camp';
import Board from './mainscreen/infos/Board'

class App extends Component {

  constructor(props) {
    super(props)
    this.height = window.innerHeight
  }

  render() {
    return (
      <div className="App">
        <Header />
        <div>
          <div className="container-fluid">
            <div className="row" style={{ height: this.height - 110, marginTop: 30 }}>
              <div className="col-4 Info">
                <Board />
              </div>
              <div className="col-1"></div>
              <div className="col-7" id="Game">
                <Camp height={this.height - 110} />
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

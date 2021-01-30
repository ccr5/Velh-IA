import React, { Component } from 'react'

import Header from './structure/Header'
import Footer from './structure/Footer'
import Camp from './mainscreen/Camp'
import Board from './mainscreen/Board'
import Welcome from './mainscreen/Welcome'
import MASBoard from './mainscreen/MASBoard'

import './App.css'

interface myState { height: number }

class App extends Component<Record<string, unknown>, myState> {
  constructor (props: Record<string, unknown>) {
    super(props)
    this.state = { height: window.innerHeight }
  }

  render (): JSX.Element {
    return (
      <div className="App">
        <Header />
        <div>
          <div className="container-fluid">
            <div className="row" style={{ marginTop: 30 }}>
              <div className="col-12">
                <Welcome />
              </div>
            </div>
            <div className="row" style={{ minHeight: this.state.height - 110 }}>
              <div className="col-4 Info">
                <Board />
              </div>
              <div className="col-1"></div>
              <div className="col-7" id="Game">
                <Camp height={this.state.height - 110} />
              </div>
            </div>
            <div className="row">
              <div className="col-12">
                <MASBoard />
              </div>
            </div>
          </div>
        </div>
        <Footer />
      </div >
    )
  }
}

export default App

import React from 'react';
import './App.css';
import Header from './structure/Header';
import Footer from './structure/Footer';
import Camp from './game/Camp';
import Board from './infos/Board'

function App() {
  const height = window.innerHeight
  return (
    <div className="App">
      <Header />
      <div className="container-fluid">
        <div className="row" style={{ height: height - 110, marginTop: 30 }}>
          <div className="col-4 Info">
            <Board />
          </div>
          <div className="col-8" id="Game">
            <Camp height={height - 130} />
          </div>
        </div>
      </div>
      <Footer />
    </div >
  );
}

export default App;

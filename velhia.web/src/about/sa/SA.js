import React from 'react'
import '../../App.css';
import './SA.css'
import Header from '../../structure/Header'
import Footer from '../../structure/Footer'


function SA() {
  return (
    <div className="App">
      <Header />
      <div className="container-fluid" style={{ minHeight: window.innerHeight - 110 }}>
        <div className="jumbotron field">
          <h1 className="display-4">How SA works?</h1>
          <div className="row">
            <div className="col-6">
              <p className="lead">
                When SA receive the game status and a position to play, it will check if
                there is some position to win or to protect itself. After that, it will calculate
                which position has more chance to win and no lose.
              </p>
            </div>
            <div className="col-6">
              <img src={process.env.PUBLIC_URL + "SA-workflow.png"} alt=""></img>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div >
  )
}

export default SA
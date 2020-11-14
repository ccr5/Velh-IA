import React from 'react'
import '../../App.css';
import './MAS.css'
import Header from '../../structure/Header'
import Footer from '../../structure/Footer'


function MAS() {
  return (
    <div className="App">
      <Header />
      <div className="container-fluid" style={{ minHeight: window.innerHeight - 110 }}>
        <div className="jumbotron field">
          <h1 className="display-2">How MAS works?</h1>
          <div className="row">
            <div className="col-12">
              <p className="lead">
                The MAS was programmed with a <strong>agent</strong> to represent all society  and tree
                establishment:
              </p>
            </div>
          </div>
          <br /><br />
          <div className="row">
            <div className="col-6">
              <p className="lead">
                <strong>1. Family establishment:</strong> The leader is the father, who are learning is
                the son and who died is the grandfather <br /><br />
                <strong>2. Religion establishment:</strong> The leader is the priest, who are learning is
                the follower and the group is the church <br /><br />
                <strong>3. Education establishment</strong> The leader is the teacher, who are learning is
                the student and the group is the school <br /><br />
              </p>
            </div>
            <div className="col-6">
              <img src={process.env.PUBLIC_URL + "MAS-infrastructure.png"} alt=""></img>
            </div>
          </div>
          <br /><br />
          <div className="row">
            <div className="col-12">
              <p className="lead">
                When MAS receive the game status, a vector with the positions already chosed
                and where it can play yet, the representative agent will pass the game status
                for each establishment leader and ask what is the best position to play.
              </p>
              <p className="lead">
                The Leader is the real player, in other words, who is responsible to answer
                the representative agent with a suggested position. it will check its memory and see if
                already receive a game like this one. if true, it will return the same position played before,
                but if it doesn't find, will return a ramdom position.
              </p>
              <p className="lead">
                When all leaders return a position, the representative agent will check if
                has a common position and return this one for Velh-IA but if all position is different
                it will choose randomly.
              </p>
              <br /> <hr />
              <p className="lead">
                The video below presents whole
                concept in a simple and objective way.
              </p>
                <iframe title="Pitch" width={window.innerWidth * 0.8} height={window.innerHeight * 0.8}
                  src="https://www.youtube.com/embed/twTLAVTcxgs" frameBorder="0"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowFullScreen>
                </iframe>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div >
  )
}

export default MAS

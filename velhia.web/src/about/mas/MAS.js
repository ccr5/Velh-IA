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
          <h1 className="display-4">How MAS works?</h1>
          <div className="row">
            <div className="col-6">
              <p className="lead">
                The MAS was programmed with a <strong>agent</strong> to represent all society  and tree
                establishment: <br /><br />
                <strong>2. Family establishment:</strong> The leader is the father, who are learning is
                the son and who died is the grandfather <br /><br />
                <strong>3. Religion establishment:</strong> The leader is the priest, who are learning is
                the follower and the group is the church <br /><br />
                <strong>4. Education establishment</strong> The leader is the teacher, who are learning is
                the student and the group is the school <br /><br />
              </p>
            </div>
            <div className="col-6">
              <img src={process.env.PUBLIC_URL + "MAS-infrastructure.png"} alt=""></img>
            </div>
          </div>
          <div className="row">
            <div className="col-6">
              <p className="lead">
                When MAS receive the game status and a position to play, the representative agent
                will pass the game status and ask for each establishment leader what is the best position
                to play. when all leaders return a position, it will check if has a common position to choose
                if not, it will choose randomly.
              </p>
            </div>
            <div className="col-6">
              <img src={process.env.PUBLIC_URL + "MAS-workflow.png"} alt=""></img>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div >
  )
}

export default MAS
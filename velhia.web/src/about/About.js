import React from 'react'
import '../App.css';
import './About.css'
import Header from '../structure/Header'
import Footer from '../structure/Footer'


function About() {
  return (
    <div className="App">
      <Header />
      <div className="container-fluid" style={{ minHeight: window.innerHeight - 110 }}>
        <div className="jumbotron field">
          <h1 className="display-2">What is Velh-IA?</h1>
          <p className="lead">
            Velh-IA is environment of a scientific research called <strong> Artificial
            Collective consciousness - Analysis of the Interactions between Artificial Intelligences</strong>
            . The objective is analyze the interactions, behaviors and results of a multi-agent system with no goal,
            under an uncontrolled and unknown environment, applying sociological concepts.
          </p>
          <h1 className="display-4">Introduction</h1>
          <p className="lead">
            Behind this website, two players are competing a Tic Tac Toe game: Statistical Algorithm and AI Network.
          </p>
          <div className="row" style={{ marginTop: "30px" }}>
            <div className="col-6" id="SA">
              <h3 className="display-5" style={{ textAlign: "center" }}> Statistical Algorithm (SA) </h3>
              <p className="lead">
                Algorithm programmed based on all the rules and objectives of the
                environment (tic-tac-toe) and plays using probability and statistics.
              </p>
            </div>
            <div className="col-6">
              <h3 className="display-5" style={{ textAlign: "center" }}> Multi-Agent System (MAS) </h3>
              <p className="lead">
                Network with AI organizations interacting and sharing informations, where a
                representative agent plays based on previous experiences of the agents in the network (stored memory)
              </p>
            </div>
          </div>
          <br /> <hr />
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
          <br /> <hr />
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
          <br /> <hr />
          <h1 className="display-4">Social concepts</h1>
          <p className="lead">
            The MAS was planned to use some social concepts like Social Fact and Functionalism theory and
            haven't a goal to achieve so...
          </p>
          <h3>
            How will the lack of purpose influence the evolution of SMA? <br />
            Would SMA organizations and agents behave as in sociological concepts?
          </h3>
          <br />
          <p className="lead">
            The video below presents the whole
            concept in a simple and objective way. We suggest that you watch
            before you move on to more specific approaches.
          </p>
          <center>
            <iframe title="Pitch" width={window.innerWidth * 0.8} height={window.innerHeight * 0.8}
              src="https://www.youtube.com/embed/tgbNymZ7vqY">
            </iframe>
          </center>
        </div>
      </div>
      <Footer />
    </div >
  )
}

export default About

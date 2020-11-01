import React from 'react'
import '../App.css';
import './About.css'
import Header from '../structure/Header'
import Footer from '../structure/Footer'
import { Link } from 'react-router-dom';


function About() {
  return (
    <div className="App">
      <Header />
      <div className="container-fluid" style={{ minHeight: window.innerHeight - 110 }}>
        <div className="jumbotron field">
          <h1 className="display-2">What is Velh-IA?</h1>
          <p className="lead">
            Velh-IA is a part of a scientific research called <strong> Artificial
            Collective consciousness - Analysis of the Interactions between Artificial Intelligences</strong>
            . The objective is analyze the interactions, behaviors and results of a multi-agent system with no goal,
            under an uncontrolled and unknown environment, applying sociological concepts.
          </p>
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
              <p className="lead">
                <center><Link to="/SA">Click here</Link> to see more</center>
              </p>
            </div>
            <div className="col-6">
              <h3 className="display-5" style={{ textAlign: "center" }}> Multi-Agent System (MAS) </h3>
              <p className="lead">
                Network with AI organizations interacting and sharing informations, where a
                representative agent plays based on previous experiences of the agents in the network (stored memory)
              </p>
              <p className="lead">
                <center><Link to="/MAS">Click here</Link> to see more</center>
              </p>
            </div>
          </div>
          <br /> <hr />
          <p className="lead">
            The video below presents whole
            concept in a simple and objective way. We suggest that you watch
            before you move on to more specific approaches.
          </p>
          <center>
            <iframe title="Pitch" width={window.innerWidth * 0.8} height={window.innerHeight * 0.8}
              src="https://www.youtube.com/embed/twTLAVTcxgs" frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen>
            </iframe>
          </center>
        </div>
      </div>
      <Footer />
    </div >
  )
}

export default About

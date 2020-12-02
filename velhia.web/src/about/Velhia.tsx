import React, { Component } from 'react'
import './Velhia.css'

class Velhia extends Component {
  render (): JSX.Element {
    return (
      <div className="">
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
        <div className="row" style={{ marginTop: '50px' }}>
          <div className="col-6">
            <h3 className="display-5" style={{ textAlign: 'center' }}> Statistical Algorithm (SA) </h3>
            <p className="lead">
                Algorithm programmed based on all the rules and objectives of the
                environment (tic-tac-toe) and plays using probability and statistics.
            </p>
          </div>
          <div className="col-6">
            <h3 className="display-5" style={{ textAlign: 'center' }}> Multi-Agent System (MAS) </h3>
            <p className="lead">
                Network with AI organizations interacting and sharing informations, where a
                representative agent plays based on previous experiences of the agents in the network (stored memory)
            </p>
          </div>
        </div>
      </div>
    )
  }
}

export default Velhia

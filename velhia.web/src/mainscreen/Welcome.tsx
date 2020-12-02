import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import './Welcome.css'

class Welcome extends Component {
  render (): JSX.Element {
    return (
      <div className="jumbotron welcome">
        <p className="display-1">Velh-IA</p>
        <p className="lead">
          Analyzing how interactions, behavior and results of a multi-agent system without
          objective, under an uncontrolled and unknown environment, applying concepts sociological.
        </p>
        <Link type="button" className="btn btn-light" to="/about">Read More</Link>
      </div>
    )
  }
}

export default Welcome

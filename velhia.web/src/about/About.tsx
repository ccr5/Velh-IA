import React from 'react'

import Velhia from './Velhia'
import Header from '../structure/Header'
import Footer from '../structure/Footer'

import '../App.css'
import './About.css'

function About (): JSX.Element {
  return (
    <div className="App">
      <Header />
      <div className="container-fluid" style={{ minHeight: window.innerHeight - 110 }}>
        <div className="jumbotron">
          <Velhia />
          <br /><hr /><br />
          <p className="lead">The video below presents whole
                              concept in a simple and objective way. We suggest that you watch
                              before you move on to more specific approaches.
          </p>
          <iframe title="Pitch" width={window.innerWidth * 0.8} height={window.innerHeight * 0.8}
            src="https://www.youtube.com/embed/twTLAVTcxgs" frameBorder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen>
          </iframe>
        </div>
      </div>
      <Footer />
    </div>
  )
}

export default About

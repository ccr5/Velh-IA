import React from 'react'
import '../App.css';
import './Collaborators.css'
import Header from '../structure/Header'
import Footer from '../structure/Footer'


function Collaborators() {
  return (
    <div className="App">
      <Header />
      <div className="container-fluid" style={{ minHeight: window.innerHeight - 110 }}>
        <p className="lead field  ">
          I'm very thankful to everybody who helped me in my jorney.
        </p>
        <br />
        <div className="row ">
          <div className="col-6">
            <div className="jumbotron youtube">
              Youtube
            </div>
          </div>
          <div className="col-6">
            <div className="jumbotron github">
              Github
            </div>
          </div>
        </div>
        <div className="row">
          <div className="col-12">
            <div className="jumbotron partnership">
              Partnerships
            </div>
          </div>
        </div>
        <div className="row">
          <div className="col-3">
            <div className="jumbotron facebook">
              Facebook
            </div>
          </div>
          <div className="col-1"></div>
          <div className="col-4">
            <div className="jumbotron instagram">
              Instagram
            </div>
          </div>
          <div className="col-1"></div>
          <div className="col-3">
            <div className="jumbotron linkedin">
              LinkedIn
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div >
  )
}

export default Collaborators

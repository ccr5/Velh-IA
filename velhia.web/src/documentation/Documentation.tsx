import React, { Component } from 'react'

import Header from '../structure/Header'
import Footer from '../structure/Footer'

import '../App.css'
import './Documentation.css'

class Documentation extends Component {
  render (): JSX.Element {
    return (
      <div className="App">
        <Header />
        <div className="container-fluid" style={{ minHeight: window.innerHeight - 110 }}>
          <div className="jumbotron">
            <div className="document">
              <h3 className="display-5">Pitch</h3>
              <br />
              <div className="row">
                <div className="col-4">
                  <ul className="lead">Google Presentation</ul>
                  <ul className="lead">Version 1.0</ul>
                  <ul className="lead">16/11/2020</ul>
                </div>
                <div className="col-8">
                  <h5>Description</h5>
                  <p className="lead">
                    This document presents in a more comprehensive way, but still succinctly,
                    the whole problem, functioning and objective. In it you will see all the planning,
                    its context and references used.
                  </p>
                </div>
              </div>
              <div className="button">
                <button type="button" className="btn btn-info">Click Here</button>
              </div>
            </div>
          </div>
          <div className="jumbotron">
            <div className="document">
              <h3 className="display-5">Article</h3>
              <br />
              <div className="row">
                <div className="col-4">
                  <ul className="lead">Google Docs</ul>
                  <ul className="lead">Version 1.0</ul>
                  <ul className="lead">16/11/2020</ul>
                </div>
                <div className="col-8">
                  <h5>Description</h5>
                  <p className="lead">
                    This document is the main documentation on all scientific research
                    and follows all standards, techniques and standard structures. In it you will see
                    all the research points, in addition to the expected results and the like.
                  </p>
                </div>
              </div>
              <div className="button">
                <button type="button" className="btn btn-info">Click Here</button>
              </div>
            </div>
          </div>
        </div>
        <Footer />
      </div>
    )
  }
}

export default Documentation

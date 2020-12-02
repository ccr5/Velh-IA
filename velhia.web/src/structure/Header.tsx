import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import './Header.css'

class Header extends Component {
  render (): JSX.Element {
    return (
      <nav className="navbar navbar-expand-lg bg-dark navbar-dark velhia-header">
        <a className="navbar-brand" href="/">Velh-IA</a>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item">
              <Link className="nav-link" to="/About">About</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/highlights">Analysis</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/documentation">Documentation</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/collaborators">Community</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/contact">Contact us</Link>
            </li>
          </ul>
        </div>
      </nav>
    )
  }
}

export default Header

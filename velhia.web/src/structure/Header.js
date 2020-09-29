import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import './Header.css'

class Header extends Component {
	render() {
		return (
			<nav className="navbar navbar-expand-lg navbar-dark blue velhia-header ">
				<a className="navbar-brand" href="/">Velh-IA</a>
				<button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
					<span className="navbar-toggler-icon"></span>
				</button>
				<div className="collapse navbar-collapse" id="navbarSupportedContent">
					<ul className="navbar-nav mr-auto">
						<li className="nav-item">
							<Link className="nav-link" to="/about">What is Velh-IA</Link>
						</li>
						<li className="nav-item">
							<Link className="nav-link" to="/highlights">Analysis</Link>
						</li>
						<li className="nav-item dropdown">
							<a className="nav-link dropdown-toggle" href="/" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
								Documentation
        			</a>
							<div className="dropdown-menu" aria-labelledby="navbarDropdown">
								<Link className="dropdown-item" to="/pitch">Pitch</Link>
								<Link className="dropdown-item" to="/article">Scientific Article</Link>
							</div>
						</li>
						<li className="nav-item dropdown">
							<a className="nav-link dropdown-toggle" href="/" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
								Community
        				</a>
							<div className="dropdown-menu" aria-labelledby="navbarDropdown">
								<Link className="dropdown-item" to="/collaborators">Collaborators</Link>
								<Link className="dropdown-item" to="/partnerships">Partnerships</Link>
							</div>
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

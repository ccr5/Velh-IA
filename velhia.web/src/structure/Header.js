import React, { Component } from 'react'
import './Header.css'

class Header extends Component {
	render() {
		return (
			<nav className="navbar navbar-dark blue velhia-header">
				<a className="navbar-brand" href="/">Velh-IA</a>
				<div className="collapse navbar-collapse" id="navbarSupportedContent">
					<ul className="navbar-nav mr-auto">
						<li className="nav-item active">
							<a className="nav-link" href="/">About </a>
						</li>
					</ul>
				</div>
			</nav>
		)
	}
}

export default Header

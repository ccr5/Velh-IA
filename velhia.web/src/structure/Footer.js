import React, { Component } from 'react'
import './Footer.css'

class Footer extends Component {
	render() {
		return (
			<footer className="velhia-footer">
				<a href="https://www.facebook.com/Pynatic">
					<img src={process.env.PUBLIC_URL + "facebook-logo.png"} height="30px" width="30px" alt=""></img>
				</a>
				<a href="https://www.youtube.com/channel/UCNBSO8r0BwMNQUaNy2UQN1g">
					<img src={process.env.PUBLIC_URL + "youtube-logo.png"} height="30px" width="30px" alt=""></img>
				</a>
				<a href="https://github.com/ccr5">
					<img src={process.env.PUBLIC_URL + "github-logo.png"} height="30px" width="30px" alt=""></img>
				</a>
				<a href="https://www.linkedin.com/in/mattnobre/">
					<img src={process.env.PUBLIC_URL + "linkedin-logo.png"} height="30px" width="30px" alt=""></img>
				</a>
							Copyright © - CCR5
			</footer >
		)
	}
}

export default Footer

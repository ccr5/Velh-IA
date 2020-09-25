import React from 'react'
import './Content.css'
import Camp from '../game/Camp'
import Board from '../infos/Board'

function Content() {
	return (
		<div className="container-fluid content">
			<div className="row">
				<div className="col-4">
					<Board />
				</div>
				<div className="col-8">
					<Camp />
				</div>
			</div>
		</div>
	)
}

export default Content

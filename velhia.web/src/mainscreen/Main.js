import React, { Component } from 'react'

import Camp from './game/Camp';
import Board from './infos/Board'

class Main extends Component {
  render() {
    return (
      <div>
        <div className="container-fluid">
          <div className="row" style={{ height: this.props.height - 110, marginTop: 30 }}>
            <div className="col-4 Info">
              <Board />
            </div>
            <div className="col-1"></div>
            <div className="col-7" id="Game">
              <Camp height={this.props.height - 110} />
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default Main

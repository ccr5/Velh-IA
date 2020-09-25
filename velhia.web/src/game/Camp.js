import React, { Component } from 'react'
import './Camp.css'

class Camp extends Component {

  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-4">
            <div className="square sup left" style={{ height: this.props.height / 4 }} id="C1L1"></div>
            <div className="square left" style={{ height: this.props.height / 4 }} id="C1L2"></div>
            <div className="square inf left" style={{ height: this.props.height / 4 }} id="C1L3"></div>
          </div>
          <div className="col-4">
            <div className="square sup" style={{ height: this.props.height / 4 }} id="C2L1"></div>
            <div className="square square" style={{ height: this.props.height / 4 }} id="C2L2"></div>
            <div className="square inf" style={{ height: this.props.height / 4 }} id="C2L3"></div>
          </div>
          <div className="col-4">
            <div className="square sup right" style={{ height: this.props.height / 4 }} id="C3L1"></div>
            <div className="square right" style={{ height: this.props.height / 4 }} id="C3L2"></div>
            <div className="square inf right" style={{ height: this.props.height / 4 }} id="C3L3"></div>
          </div>
        </div>
      </div>
    )
  }
}

export default Camp

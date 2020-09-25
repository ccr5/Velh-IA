import React from 'react'
import './Camp.css'

function Camp() {
  return (
    <div className="container">
      <div className="row Camp">
        <div className="col-4">
          <div className="square" id="C1L1">7</div>
          <div className="square" id="C1L2">4</div>
          <div className="square" id="C1L3">1</div>
        </div>
        <div className="col-4">
          <div className="square" id="C2L1">8</div>
          <div className="square" id="C2L2">5</div>
          <div className="square" id="C2L3">2</div>
        </div>
        <div className="col-4">
          <div className="square" id="C3L1">9</div>
          <div className="square" id="C3L2">6</div>
          <div className="square" id="C3L3">3</div>
        </div>
      </div>
    </div>
  )
}

export default Camp

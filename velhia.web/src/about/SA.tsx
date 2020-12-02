import React from 'react'
import '../App.css'
import './SA.css'

function SA (): JSX.Element {
  return (
    <>
      <h1 className="display-2">How SA works?</h1>
      <div className="row">
        <div className="col-12">
          <p className="lead">
                First, the SA will receive the game status from Velh-IA, a vector with the positions already chosed
                and where it can play yet. It'll check if there is some position to win and if it find something,
                will return this position to Velh-IA. The next step is check if there is some position where it
                must to play to don't lose. if true, it will return this position.  Now everything is checked,
                it can calculate what is the best position to win and not lose and return it for Velh-IA.
          </p>
        </div>
      </div>
    </>
  )
}

export default SA

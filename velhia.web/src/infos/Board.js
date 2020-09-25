import React, { Component } from 'react'
import './Board.css'

class Board extends Component {
  render() {
    return (
      <div className="container Board">
        <div className="jumbotron">
          <h5>General</h5>
          <table class="table">
            <thead>
              <tr>
                <th scope="col">Begin</th>
                <th scope="col">Nº Matchs</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{}</td>
                <td>{}</td>
              </tr>
            </tbody>
          </table>
          <br />
          <h5>Details</h5>
          <table class="table">
            <thead>
              <tr>
                <th scope="col">Player</th>
                <th scope="col">Wins</th>
                <th scope="col">Last</th>
                <th scope="col">%</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    )
  }
}

export default Board

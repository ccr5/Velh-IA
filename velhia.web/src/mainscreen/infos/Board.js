import React, { Component } from 'react'
import './Board.css'

class Board extends Component {
  render() {
    return (
      <div className="container board">
        <div className="jumbotron infos">
          <h5 className="title">Details</h5>
          <table class="table font">
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
                <td>Matheus</td>
                <td>1</td>
                <td>28/09/2020</td>
                <td>50%</td>
              </tr>
              <tr>
                <td>Lucas</td>
                <td>1</td>
                <td>28/09/2020</td>
                <td>50%</td>
              </tr>
            </tbody>
          </table>
          <br />
          <h5 className="title">General</h5>
          <table class="table font">
            <tbody>
              <tr>
                <td>Begin</td>
                <td>28/09/2020</td>
              </tr>
              <tr>
                <td>Nº Matchs</td>
                <td>2</td>
              </tr>
            </tbody>
          </table>
          <br />
        </div>
      </div>
    )
  }
}

export default Board

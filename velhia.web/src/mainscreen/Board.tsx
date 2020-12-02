import React, { Component } from 'react'
import Axios from 'axios'
import './Board.css'

interface myState {
  SA: {
    name: string,
    wins: number,
    last: string,
    percent: string
  },
  MAS: {
    name: string,
    wins: number,
    last: string,
    percent: string
  },
  General: {
    begin: string,
    matchs: number
  }
}

class Board extends Component<Record<string, unknown>, myState> {
  constructor (props: Record<string, unknown>) {
    super(props)
    this.state = {
      SA: {
        name: 'Statistical Algorithm',
        wins: 0,
        last: '24/10/2020',
        percent: '%'
      },
      MAS: {
        name: 'Multi-Agent System',
        wins: 0,
        last: '25/10/2020',
        percent: '%'
      },
      General: {
        begin: '28/09/2020',
        matchs: 0
      }
    }
  }

  componentDidMount ():void {
    setInterval(
      () => this.updateSAValues(),
      30000
    )
  }

  updateSAValues (): void {
    Axios.get('https://api.bitpreco.com/btc-brl/ticker')
      .then((response) => {
        this.setState({
          SA: {
            name: 'Statistical Algorithm',
            wins: response.data.avg,
            last: '24/10/2020',
            percent: '%'
          }
        })
      })
  }

  // componentWillUnmount(): void {
  //   clearInterval(this.boardAdd)
  // }

  render (): JSX.Element {
    return (
      <div className="container board">
        <div className="jumbotron infos">
          <h5 className="title">Details</h5>
          <table className="table font">
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
                <td>{this.state.SA.name}</td>
                <td>{this.state.SA.wins}</td>
                <td>{this.state.SA.last}</td>
                <td>{this.state.SA.percent}</td>
              </tr>
              <tr>
                <td>{this.state.MAS.name}</td>
                <td>{this.state.MAS.wins}</td>
                <td>{this.state.MAS.last}</td>
                <td>{this.state.MAS.percent}</td>
              </tr>
            </tbody>
          </table>
          <br />
          <h5 className="title">General</h5>
          <table className="table font">
            <tbody>
              <tr>
                <td>Begin</td>
                <td>{this.state.General.begin}</td>
              </tr>
              <tr>
                <td>Nº Matchs</td>
                <td>{this.state.General.matchs}</td>
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

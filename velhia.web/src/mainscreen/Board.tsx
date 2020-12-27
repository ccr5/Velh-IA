import React, { Component } from 'react'
import Axios from 'axios'
import './Board.css'

interface myState {
  SA: {
    name: string,
    wins: number,
    percent: string
  },
  MAS: {
    name: string,
    wins: number,
    percent: string
  },
  General: {
    begin: string,
    matchs: number,
    draws: number
  }
}

class Board extends Component<Record<string, unknown>, myState> {
  constructor (props: Record<string, unknown>) {
    super(props)
    this.state = {
      SA: {
        name: 'Statistical Algorithm',
        wins: 0,
        percent: '-'
      },
      MAS: {
        name: 'Multi-Agent System',
        wins: 0,
        percent: '-'
      },
      General: {
        begin: '',
        matchs: 0,
        draws: 0
      }
    }
  }

  componentDidMount ():void {
    this.updateSAValues()
    this.updateMASValues()
    this.updateGeneralValues()

    setInterval(
      () => {
        this.updateSAValues()
        this.updateMASValues()
        this.updateGeneralValues()
      },
      1000
    )
  }

  updateSAValues (): void {
    Axios.get('http://localhost:3000/api/v1/web/sa')
      .then((response) => {
        this.setState({
          SA: {
            name: 'Statistical Algorithm',
            wins: response.data.wins,
            percent: `${Math.round(response.data.percent * 100).toFixed(0)}%`
          }
        })
      })
  }

  updateMASValues (): void {
    Axios.get('http://localhost:3000/api/v1/web/mas')
      .then((response) => {
        this.setState({
          MAS: {
            name: 'Multi-Agent System',
            wins: response.data.wins,
            percent: `${Math.round(response.data.percent * 100).toFixed(0)}%`
          }
        })
      })
  }

  updateGeneralValues (): void {
    Axios.get('http://localhost:3000/api/v1/web/general')
      .then((response) => {
        this.setState({
          General: {
            begin: this.formatDate(new Date(response.data.begin)),
            matchs: response.data.nMatchs,
            draws: response.data.nDraws
          }
        })
      })
  }

  formatDate (date: Date): string {
    return `${date.getDate()}/${date.getMonth()}/${date.getFullYear()}`
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
                <th scope="col">%</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{this.state.SA.name}</td>
                <td>{this.state.SA.wins}</td>
                <td>{this.state.SA.percent}</td>
              </tr>
              <tr>
                <td>{this.state.MAS.name}</td>
                <td>{this.state.MAS.wins}</td>
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
              <tr>
                <td>Nº Draws</td>
                <td>{this.state.General.draws}</td>
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

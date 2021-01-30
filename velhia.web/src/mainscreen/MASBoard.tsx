import React, { Component } from 'react'
import Axios from 'axios'
import './MASBoard.css'

interface myState {
  family: {
    institution: string,
    generation: string,
    life: number,
    memories: number,
    matchAsLearner: number,
    matchAsLeader: number,
    victories: number,
    defeats: number,
    draws: number
  },
  education: {
    institution: string,
    generation: string,
    life: number,
    memories: number,
    matchAsLearner: number,
    matchAsLeader: number,
    victories: number,
    defeats: number,
    draws: number
  },
  religion: {
    institution: string,
    generation: string,
    life: number,
    memories: number,
    matchAsLearner: number,
    matchAsLeader: number,
    victories: number,
    defeats: number,
    draws: number
  }
}

export default class MASBoard extends Component<Record<string, unknown>, myState> {
  constructor (props: Record<string, unknown>) {
    super(props)
    this.state = {
      family: {
        institution: '',
        generation: '',
        life: 0,
        memories: 0,
        matchAsLearner: 0,
        matchAsLeader: 0,
        victories: 0,
        defeats: 0,
        draws: 0
      },
      education: {
        institution: '',
        generation: '',
        life: 0,
        memories: 0,
        matchAsLearner: 0,
        matchAsLeader: 0,
        victories: 0,
        defeats: 0,
        draws: 0
      },
      religion: {
        institution: '',
        generation: '',
        life: 0,
        memories: 0,
        matchAsLearner: 0,
        matchAsLeader: 0,
        victories: 0,
        defeats: 0,
        draws: 0
      }
    }
  }

  componentDidMount ():void {
    this.updateMASValues()

    setInterval(
      () => {
        this.updateMASValues()
      },
      1000
    )
  }

  updateMASValues (): void {
    Axios.get('http://localhost:3000/api/v1/web/mas-details')
      .then((response) => {
        this.setState({
          family: {
            institution: response.data.family.institution,
            generation: response.data.family.generation,
            life: +Math.round(response.data.family.life).toFixed(2),
            memories: response.data.family.memories,
            matchAsLearner: response.data.family.matchAsLearner,
            matchAsLeader: response.data.family.matchAsLeader,
            victories: response.data.family.victories,
            defeats: response.data.family.defeats,
            draws: response.data.family.draws
          },
          education: {
            institution: response.data.education.institution,
            generation: response.data.education.generation,
            life: +Math.round(response.data.education.life).toFixed(2),
            memories: response.data.education.memories,
            matchAsLearner: response.data.education.matchAsLearner,
            matchAsLeader: response.data.education.matchAsLeader,
            victories: response.data.education.victories,
            defeats: response.data.education.defeats,
            draws: response.data.education.draws
          },
          religion: {
            institution: response.data.religion.institution,
            generation: response.data.religion.generation,
            life: +Math.round(response.data.religion.life).toFixed(2),
            memories: response.data.religion.memories,
            matchAsLearner: response.data.religion.matchAsLearner,
            matchAsLeader: response.data.religion.matchAsLeader,
            victories: response.data.religion.victories,
            defeats: response.data.religion.defeats,
            draws: response.data.religion.draws
          }
        })
      })
  }

  // componentWillUnmount(): void {
  //   clearInterval(this.boardAdd)
  // }

  render (): JSX.Element {
    return (
      <div className="container-fluid board">
        <div className="jumbotron infosMAS">
          <h5 className="title">Multi Agent System</h5>
          <table className="table">
            <thead>
              <tr>
                <th scope="col">Institution</th>
                <th scope="col">Generation</th>
                <th scope="col">% Life </th>
                <th scope="col">Memories</th>
                <th scope="col">as Learner</th>
                <th scope="col">as Leader</th>
                <th scope="col">Victories</th>
                <th scope="col">defeats</th>
                <th scope="col">draws</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{this.state.family.institution}</td>
                <td>{this.state.family.generation}</td>
                <td>{this.state.family.life}</td>
                <td>{this.state.family.memories}</td>
                <td>{this.state.family.matchAsLearner}</td>
                <td>{this.state.family.matchAsLeader}</td>
                <td>{this.state.family.victories}</td>
                <td>{this.state.family.defeats}</td>
                <td>{this.state.family.draws}</td>
              </tr>
              <tr>
                <td>{this.state.education.institution}</td>
                <td>{this.state.education.generation}</td>
                <td>{this.state.education.life}</td>
                <td>{this.state.education.memories}</td>
                <td>{this.state.education.matchAsLearner}</td>
                <td>{this.state.education.matchAsLeader}</td>
                <td>{this.state.education.victories}</td>
                <td>{this.state.education.defeats}</td>
                <td>{this.state.education.draws}</td>
              </tr>
              <tr>
                <td>{this.state.religion.institution}</td>
                <td>{this.state.religion.generation}</td>
                <td>{this.state.religion.life}</td>
                <td>{this.state.religion.memories}</td>
                <td>{this.state.religion.matchAsLearner}</td>
                <td>{this.state.religion.matchAsLeader}</td>
                <td>{this.state.religion.victories}</td>
                <td>{this.state.religion.defeats}</td>
                <td>{this.state.religion.draws}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    )
  }
}

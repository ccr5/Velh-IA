import React, { Component } from 'react'
import Axios from 'axios'
import './Camp.css'

interface myProps {
  height: number
}

interface myState {
  C1: {
    L1: number,
    L2: number,
    L3: number
  },
  C2: {
    L1: number,
    L2: number,
    L3: number
  },
  C3: {
    L1: number,
    L2: number,
    L3: number
  }
}

function checkCamp(value: number, height: number) {
  if (value === 1) {
    return ( <img src={process.env.PUBLIC_URL + "X.jpg"} height={height} alt=""></img> )
  } else if (value === 0) {
    return ( <img src={process.env.PUBLIC_URL + "O.png"} height={height} alt=""></img> )
  }
}

class Camp extends Component<myProps, myState> {

  constructor(props: myProps) {
    super(props)
    this.state = {
      C1: {
        L1: 1,
        L2: -1,
        L3: -1
      },
      C2: {
        L1: -1,
        L2: 0,
        L3: -1
      },
      C3: {
        L1: -1,
        L2: -1,
        L3: -1
      }
    }
  }

  componentDidMount() {
    setInterval(
      () => this.updateSAValues(),
      30000
    )
  }

  updateSAValues() {
    Axios.get('https://api.bitpreco.com/btc-brl/ticker')
      .then((response) => {
        console.log(response.data.avg)
        this.setState({
          C1: {
            L1: 1,
            L2: -1,
            L3: -1
          },
          C2: {
            L1: -1,
            L2: 0,
            L3: -1
          },
          C3: {
            L1: -1,
            L2: -1,
            L3: -1
          }
        })
      })
  }

  // componentWillUnmount() {
  //   clearInterval(this.boardAdd)
  // }

  render() {
    return (
      <div className="container camp">
        <div className="row">
          <div className="col-4">
            <div className="square sup left" style={{ height: this.props.height / 4 }} id="C1L1">
              {checkCamp(this.state.C1.L1, this.props.height / 4)}
            </div>
            <div className="square left" style={{ height: this.props.height / 4 }} id="C1L2">
              {checkCamp(this.state.C1.L2, this.props.height / 4)}
            </div>
            <div className="square inf left" style={{ height: this.props.height / 4 }} id="C1L3">
              {checkCamp(this.state.C1.L3, this.props.height / 4)}
            </div>
          </div>
          <div className="col-4">
            <div className="square sup" style={{ height: this.props.height / 4 }} id="C2L1">
              {checkCamp(this.state.C2.L1, this.props.height / 4)}
            </div>
            <div className="square square" style={{ height: this.props.height / 4 }} id="C2L2">
              {checkCamp(this.state.C2.L2, this.props.height / 4)}
            </div>
            <div className="square inf" style={{ height: this.props.height / 4 }} id="C2L3">
              {checkCamp(this.state.C2.L3, this.props.height / 4)}
            </div>
          </div>
          <div className="col-4">
            <div className="square sup right" style={{ height: this.props.height / 4 }} id="C3L1">
              {checkCamp(this.state.C3.L1, this.props.height / 4)}
            </div>
            <div className="square right" style={{ height: this.props.height / 4 }} id="C3L2">
              {checkCamp(this.state.C3.L2, this.props.height / 4)}
            </div>
            <div className="square inf right" style={{ height: this.props.height / 4 }} id="C3L3">
              {checkCamp(this.state.C3.L3, this.props.height / 4)}
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default Camp

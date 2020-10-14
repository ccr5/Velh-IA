import React from 'react'
import '../App.css';
import './Collaborators.css'
import Header from '../structure/Header'
import Footer from '../structure/Footer'


function Collaborators() {
  return (
    <div className="App">
      <Header />
      <div className="container-fluid" style={{ minHeight: window.innerHeight - 80 }}>
        <div className="row">
          <div className="col-6">
            <div className="jumbotron transp">
              Colabo
            </div>
          </div>
          <div className="col-6">
            <div className="jumbotron transp">
              Colabo
            </div>
          </div>
        </div>

      </div>
      <Footer />
    </div >
  )
}

export default Collaborators

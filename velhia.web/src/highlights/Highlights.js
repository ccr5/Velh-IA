import React from 'react'
import '../App.css';
import './Highlights.css'
import Header from '../structure/Header'
import Footer from '../structure/Footer'


function Highlights() {
  return (
    <div className="App">
      <Header />
      <div className="container-fluid" style={{ minHeight: window.innerHeight - 80 }}>
        <center>
          <iframe title="Pitch" width={window.innerWidth * 0.8} height={window.innerHeight - 110}
            src="https://app.powerbi.com/view?r=eyJrIjoiMjIyODgxMGUtYTIwYi00YjkzLWIyNjMtN2EwZTBlNWJkZjk4IiwidCI6IjE4ZGZmZDg0LTg0Y2QtNDA3OC05YzJhLWI4NmQ2OGNhOThjYyJ9">
          </iframe>
        </center>
      </div>
      <Footer />
    </div >
  )
}

export default Highlights

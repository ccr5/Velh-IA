import React from 'react'
import '../App.css';
import './Highlights.css'
import Header from '../structure/Header'
import Footer from '../structure/Footer'
import Menu from './menu/Menu';



function Highlights() {
  return (
    <div className="App">
      <Header />
      <div className="container-fluid" style={{ minHeight: window.innerHeight - 80 }}>
        <div className="row">
          <div className="col-2">
            <Menu />
          </div>
          <div id="iframe" className="col-10">
            <iframe title="Pitch" width="100%" height={window.innerHeight - 110}
              src="https://app.powerbi.com/view?r=eyJrIjoiMjIyODgxMGUtYTIwYi00YjkzLWIyNjMtN2EwZTBlNWJkZjk4IiwidCI6IjE4ZGZmZDg0LTg0Y2QtNDA3OC05YzJhLWI4NmQ2OGNhOThjYyJ9">
            </iframe>
          </div>
        </div>
      </div>
      <Footer />
    </div >
  )
}

export default Highlights

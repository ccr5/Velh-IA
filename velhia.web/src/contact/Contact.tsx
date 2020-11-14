import React from 'react'
import '../App.css';
import './Contact.css'
import Header from '../structure/Header'
import Footer from '../structure/Footer'


function Contact() {
  return (
    <div className="App">
      <Header />
      <div className="container-fluid" style={{ minHeight: window.innerHeight - 80 }}>
        <div className="jumbotron transp">
          <h1 className="display-4">Contact</h1>
          <div className="row">
            <div className="jumbotron field col-6">
              <div className="row">
                <div className="col-md-9 mb-md-0 mb-5">
                  <form id="contact-form" name="contact-form" action="mail.php" method="POST">
                    <div className="row">
                      <div className="col-md-6">
                        <div className="md-form mb-0">
                          <input type="text" id="name" name="name" className="form-control"></input>
                          <label htmlFor ="name" className="">Your name</label>
                        </div>
                      </div>
                      <div className="col-md-6">
                        <div className="md-form mb-0">
                          <input type="text" id="email" name="email" className="form-control"></input>
                          <label htmlFor="email" className="">Your email</label>
                        </div>
                      </div>
                    </div>
                    <div className="row">
                      <div className="col-md-12">
                        <div className="md-form mb-0">
                          <input type="text" id="subject" name="subject" className="form-control"></input>
                          <label htmlFor="subject" className="">Subject</label>
                        </div>
                      </div>
                    </div>
                    <div className="row">
                      <div className="col-md-12">
                        <div className="md-form">
                          <textarea id="message" name="message" rows={2} className="form-control md-textarea"></textarea>
                          <label htmlFor="message">Your message</label>
                        </div>
                      </div>
                    </div>
                  </form>
                  <div className="text-center text-md-left">
                    <a className="btn btn-primary" href="/#">Send</a>
                  </div>
                  <div className="status"></div>
                </div>
              </div>
            </div>
            <div className="jumbotron infos col-6">
              <p className="lead">
                Fell free to call me. I'm waiting you
              </p>
              <h5>Matheus Nobre Gomes</h5>
              <br />
              <div className="row">
                <div className="col-6">
                  <p className="lead">E-mail:</p>
                </div>
                <div className="col-6">
                  <p className="lead">matt-gomes@live.com</p>
                </div>
              </div>
              <div className="row">
                <div className="col-6">
                  <p className="lead">Location:</p>
                </div>
                <div className="col-6">
                  <p className="lead">Sao Paulo, Brazil</p>
                </div>
              </div>
              <div className="row">
                <div className="col-6">
                  <p className="lead">WhatsApp</p>
                </div>
                <div className="col-6">
                  <p className="lead">+55 11 99566-0126</p>
                </div>
              </div>
              <br />
              <hr />
              <br /><br />
                <a href="https://www.facebook.com/Pynatic">
                  <img src={process.env.PUBLIC_URL + "facebook-logo.png"} height="30px" width="30px" alt=""></img>
                </a>
                <a href="https://www.youtube.com/channel/UCNBSO8r0BwMNQUaNy2UQN1g">
                  <img src={process.env.PUBLIC_URL + "youtube-logo.png"} height="30px" width="30px" alt=""></img>
                </a>
                <a href="https://github.com/ccr5">
                  <img src={process.env.PUBLIC_URL + "github-logo.png"} height="30px" width="30px" alt=""></img>
                </a>
                <a href="https://www.linkedin.com/in/mattnobre/">
                  <img src={process.env.PUBLIC_URL + "linkedin-logo.png"} height="30px" width="30px" alt=""></img>
                </a>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div >
  )
}

export default Contact
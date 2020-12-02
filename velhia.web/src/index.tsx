import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Route, Switch } from 'react-router-dom'

import About from './about/About'
import Highlights from './highlights/Highlights'
import Documentation from './documentation/Documentation'
import Contact from './contact/Contact'
import Collaborators from './collaborators/Collaborators'

import './index.css'
import App from './App'

ReactDOM.render(
  <BrowserRouter>
    <Switch>
      <Route path="/" exact={true} component={App} />
      <Route path="/about" component={About} />
      <Route path="/highlights" component={Highlights} />
      <Route path="/documentation" component={Documentation} />
      <Route path='/pitch' render={() => (window.location.href = 'https://drive.google.com/file/d/1UKPZ7I5N6bp6ra51rSCFFoxtNL2clJYr/view?usp=sharing')} />
      <Route path='/article' render={() => (window.location.href = 'https://drive.google.com/file/d/1GUsFL3vxVUZH8SzdMD6WA2x4VfcXHlio/view?usp=sharing')} />
      <Route path='/code' render={() => (window.location.href = 'https://github.com/ccr5/Velh-IA')} />
      <Route path="/collaborators" component={Collaborators} />
      <Route path="/contact" component={Contact} />
      {/* <Route path="*">Erro</Route> */}
    </Switch>
  </BrowserRouter>,
  document.getElementById('root')
)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals()

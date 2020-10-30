import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import './index.css';
import App from './App';

import About from './about/About';
import Highlights from './highlights/Highlights';
import Contact from './contact/Contact';
import Collaborators from './collaborators/Collaborators';
import SA from './about/sa/SA';
import MAS from './about/mas/MAS';

import * as serviceWorker from './serviceWorker';

ReactDOM.render(
  <BrowserRouter>
    <Switch>
      <Route path="/" exact={true} component={App} />
      <Route path="/about" component={About} />
      <Route path="/SA" component={SA} />
      <Route path="/MAS" component={MAS} />
      <Route path="/highlights" component={Highlights} />
      <Route path='/pitch' render={() => (
        window.location.href = 'https://drive.google.com/file/d/1UKPZ7I5N6bp6ra51rSCFFoxtNL2clJYr/view?usp=sharing'
      )} />
      <Route path='/article' render={() => (
        window.location.href = 'https://drive.google.com/file/d/1GUsFL3vxVUZH8SzdMD6WA2x4VfcXHlio/view?usp=sharing'
      )} />
      <Route path='/code' render={() => (
        window.location.href = 'https://github.com/ccr5/Velh-IA'
      )} />
      <Route path="/collaborators" component={Collaborators} />
      <Route path="/contact" component={Contact} />
      {/* <Route path="*">Erro</Route> */}
    </Switch>
  </BrowserRouter>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
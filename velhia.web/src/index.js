import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import './index.css';
import App from './App';
import About from './about/About';
import * as serviceWorker from './serviceWorker';



ReactDOM.render(
  <BrowserRouter>
    <Switch>
      <Route path="/" exact={true} component={App} />
      <Route path="/about" component={About} />
      {/* <Route path="/highlights"></Route>
        <Route path="/pitch"></Route>
        <Route path="/article"></Route>
        <Route path="/collaborators"></Route>
        <Route path="/partnerships"></Route>
        <Route path="*">Erro</Route> */}
    </Switch>
  </BrowserRouter>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

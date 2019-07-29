import React from 'react';
import ReactDOM from 'react-dom';
import { Route, Link, BrowserRouter as Router } from 'react-router-dom';

import * as serviceWorker from './serviceWorker';
import App from './App';

import Login from './components/login'
import Register from './components/register'

import Profile from './components/profile'
import Tickets from './components/tickets'

const routing = (
    <Router>
      <div>
        <Route path="/login" component={Login}/>
        <Route path="/register" component={Register}/>
        <Route path="/profile" component={Profile}/>
        <Route path="/tickets" component={Tickets}/>
      </div>
    </Router>
  )

ReactDOM.render(routing, document.getElementById('root'));

serviceWorker.unregister();

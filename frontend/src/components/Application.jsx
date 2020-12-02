import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom';
import Home from './HomePage/Home';
import WorkSpace from './WorkSpacePage/WorkSpace';
import Login from './LoginPage/Login';

export default function Application() {
  const API_URL = 'https://localhost/api/';
  return (
    <Router>
      <Switch>
        <Route path="/" exact>
          <Home url={API_URL} />
        </Route>
        <Route path="/content/" exact>
          <WorkSpace url={API_URL} />
        </Route>
        <Route path="/login/" exact>
          <Login url={API_URL} />
        </Route>
      </Switch>
    </Router>
  );
}

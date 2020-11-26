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
  return (
    <Router>
      <Switch>
        <Route path="/" exact>
          <Home />
        </Route>
        <Route path="/content/" exact>
          <WorkSpace />
        </Route>
        <Route path="/login/" exact>
          <Login />
        </Route>
      </Switch>
    </Router>
  );
}

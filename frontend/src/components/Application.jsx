import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom';
import Home from './HomePage/Home';
import WorkSpace from './WorkSpacePage/WorkSpace';
import StartPage from './LoginPage/StartPage';
import PrivateRoute from './Auth/PrivateRoute';
import NotFound from './NotFound';
import ProvideAuth from './Auth/ProvideAuth';

export default function Application() {
  const API_URL = 'https://localhost/api/';
  return (
    <ProvideAuth>
      <Router>
        <Switch>
          <PrivateRoute path="/home/" exact>
            <Home url={API_URL} />
          </PrivateRoute>
          <PrivateRoute path="/content/" exact>
            <WorkSpace url={API_URL} />
          </PrivateRoute>
          <Route path="/login/" exact>
            <StartPage url={API_URL} />
          </Route>
          <Route path="*">
            <NotFound />
          </Route>
        </Switch>
      </Router>
    </ProvideAuth>
  );
}

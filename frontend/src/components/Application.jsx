import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from 'react-router-dom';
import { Home } from './Home'
import { PersonalPage } from './PersonalPage';


export function Application() {
    return (
        <Router>
            <Switch>
                <Route path='/' exact>
                    <Home/>
                </Route>
                <Route path='/content/' exact>
                    <PersonalPage/>
                </Route>
            </Switch>
        </Router>
    );
}

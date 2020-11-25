import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from 'react-router-dom';
import { Home } from './HomePage/Home'
import { WorkSpacePage } from './WorkSpace/WorkSpacePage';


export function Application() {
    return (
        <Router>
            <Switch>
                <Route path='/' exact>
                    <Home/>
                </Route>
                <Route path='/content/' exact>
                    <WorkSpacePage/>
                </Route>
            </Switch>
        </Router>
    );
}

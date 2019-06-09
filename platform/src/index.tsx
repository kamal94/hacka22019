import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import { Button, Card, Navbar, Row, Col, NavItem  } from 'react-materialize';
import {BrowserRouter, Link} from 'react-router-dom';

ReactDOM.render(
    <BrowserRouter>
        <div className="container">
            <Navbar alignLinks="left">
                <NavItem >
                <Link to="/">Home</Link>
                </NavItem>
            </Navbar>
            <App />
        </div>
    </BrowserRouter>,
     document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

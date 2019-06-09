import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import { Navbar, Row  } from 'react-materialize';
import {BrowserRouter, Link} from 'react-router-dom';

ReactDOM.render(
    <BrowserRouter>
        <div className="container">
            <Navbar alignLinks="left">
                <Link to="/">Home</Link>
                <Link to="/" className="brand-logo right"><img src="/EnergySaver3.png" width="100px" height="70px"/></Link>
            </Navbar>
            <Row height="20px"></Row>
            <App />
        </div>
    </BrowserRouter>,
     document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

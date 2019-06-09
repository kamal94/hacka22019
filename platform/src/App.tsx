import React from 'react';
import './App.css';
import './.d.ts';
import {Homepage} from './homepage';
import {Complex} from './complex';
import {Unit} from './unit';
import { Route, Switch } from 'react-router-dom'

const App: React.FC = () => {
  return (
    <Switch>
      <Route exact path="/" component={Homepage} />
      <Route path="/complex/:id" component={Complex} />
      <Route path="/unit/:id" component={Unit} />
    </Switch>
  );
}

export default App;

import React from 'react';
import './App.css';
import './.d.ts';
import { complexes,  units} from './dummy';
import {Homepage} from './homepage';
import {Complex} from './complex';
import { Route, Switch } from 'react-router-dom'

const App: React.FC = () => {
  return (
    <Switch>
      <Route exact path="/" component={Homepage} />
      <Route path="/complex/:id" component={Complex} />
    </Switch>
  );
}

export default App;

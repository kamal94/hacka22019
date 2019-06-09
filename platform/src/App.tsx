import React from 'react';
import logo from './logo.svg';
import './App.css';
import './.d.ts';
import { Button, Card, Navbar, Row, Col, NavItem  } from 'react-materialize';
import { complexes,  units} from './dummy';
const App: React.FC = () => {
  const complex_divs = complexes.map((complex) => {
      return (<Col s={4}>
        <Card>
          <a href={'/complex/'+ complex.id }>
            <div className="card-content">
              <div className="card-title"> {complex.address} </div>
              <div className="card-content"> {complex.num_units} apartments</div>
            </div>
          </a>
        </Card>
      </Col>)
    }
  )
  return (
    <div className="container">
      <Navbar alignLinks="left">
        <NavItem >
        Getting started
        </NavItem>
      </Navbar>
      <Row>
        {complex_divs}
      </Row>
    </div>
  );
}

export default App;

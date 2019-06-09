import React from 'react';
import './App.css';
import './.d.ts';
import { Button, Card, Navbar, Row, Col, NavItem } from 'react-materialize';
import { complexes, units } from './dummy';
import { fetchComplexes } from './api';


export class Homepage extends React.Component<{},{complexes:any, isLoaded: boolean}> {
  
  constructor(props) {
    super(props);
    this.state = {
      complexes: [],
      isLoaded: false
    };
  }

  componentDidMount() {
    return fetchComplexes()
    .then((response) => {
      console.log("complexes:");
      console.log(response);
      this.setState({complexes: response.data, isLoaded: true})
    })
  }
  
  render() {


    if (this.state.isLoaded) {
      const complex_divs = this.state.complexes.map((complex) => {
        return (
          <Col s={4}>
            <Card>
              <a href={'/complex/' + complex.id}>
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
        <Row>
          {complex_divs}
        </Row>
      )
    } else {
      return <Row>Loading</Row>
    }
  }
}
import React from 'react';
import './App.css';
import { Card, CardTitle, Row, Col} from 'react-materialize';
import { fetchComplexes } from './api';


export class Homepage extends React.Component<{}, { complexes: any, isLoaded: boolean }> {

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
        this.setState({ complexes: response.data, isLoaded: true })
      })
  }

  render() {


    if (this.state.isLoaded) {
      const complex_divs = this.state.complexes.map((complex) => {
        return (
          <Col s={12} m={6} l={3}>
            <a href={'/complex/' + complex.id}>
              <Card className="hoizontal"
                header={<CardTitle image={'/' + complex.image}></CardTitle>}>
                <div className="card-content">
                  <div className="card-title"> {complex.address} </div>
                  <div className="card-content"> {complex.num_units} apartments</div>
                </div>
              </Card>
            </a>
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
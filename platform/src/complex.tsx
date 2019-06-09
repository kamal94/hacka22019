import React from 'react';
import './App.css';
import './.d.ts';
import { Button, Card, Navbar, Row, Col, Table, } from 'react-materialize';
import { complexes, units, monthly } from './dummy';
import { RouteComponentProps } from 'react-router-dom';
import { fetchComplex, fetchComplexUnits } from './api';
import { UnitMonthlyRow } from './unit-monthly-row';
import * as moment from 'moment';

import DatePicker from "react-datepicker";
 
import "react-datepicker/dist/react-datepicker.css";

export class Complex extends React.Component<{ matches }, any> {
    constructor(props) {
        super(props);
        this.state = {
            complex: null,
            complex_id: props.match.params.id,
            units: [],
            start_date: "",
            end_date:""
        }
        this.handleStartDateChange = this.handleStartDateChange.bind(this);
        this.handleEndDateChange = this.handleEndDateChange.bind(this);
    }

    handleStartDateChange(date) {
        console.log("start date:", date);
        this.setState({
            start_date: date
        })
    }

    handleEndDateChange(date) {
        console.log("end date:", date);

        this.setState({
            end_date: date
        })
    }

    componentDidMount() {
        fetchComplex(this.state.complex_id)
            .then(res =>
                this.setState({
                    complex: res.data
                })
            )
        fetchComplexUnits(this.state.complex_id)
            .then(res =>
                this.setState({
                    units: res.data
                })
            )
    }

    isLoaded() {
        return (this.state.complex != null && units != [])
    }
    render() {
        if (this.isLoaded()) {
            const unit_rows = this.state.units.map(unit =>
                <UnitMonthlyRow 
                unit_id={unit.id} 
                start_date={this.state.start_date} 
                end_date={this.state.end_date} 
                reading_type="" 
                />
            );
            return (
                <div>
                    <Row>
                        <h2>{this.state.complex.address}</h2>
                    </Row>
                    <Row>
                        <Col s={3}> 
                            <div>Start Date</div> <div> 
                                <DatePicker
                                    selected={this.state.start_date}
                                    onChange={this.handleStartDateChange}/>
                            </div>
                        </Col>

                        <Col s={3}> 
                            <div>End Date</div> <div> 
                                <DatePicker
                                    selected={this.state.end_date}
                                    onChange={this.handleEndDateChange}/>
                            </div>
                        </Col>
                    </Row>
                    <Row>
                        <Table className="highlight centered responsive-table">
                            <thead>
                                <tr>
                                    <th data-field="id">
                                        Address
                                    </th>
                                    <th data-field="name">
                                        Bed #
                                    </th>
                                    <th data-field="price">
                                        Allowance
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                {unit_rows}
                            </tbody>
                        </Table>
                    </Row>
                </div>
                        )
        } else {
            return <div>Loading</div>
                        }
                    }
} 
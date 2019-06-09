import React from 'react';
import './App.css';
import { Row, Col, Table, } from 'react-materialize';
import { fetchComplex, fetchComplexUnits } from './api';
import { UnitMonthlyRow } from './unit-monthly-row';
import moment from 'moment';

import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

export class Complex extends React.Component<{ matches }, any> {
    constructor(props) {
        super(props);
        this.state = {
            complex: null,
            complex_id: props.match.params.id,
            units: [],
            start_date: moment().subtract(12, 'months'),
            end_date: moment()
        }
        this.handleStartDateChange = this.handleStartDateChange.bind(this);
        this.handleEndDateChange = this.handleEndDateChange.bind(this);
    }

    handleStartDateChange(date) {
        this.setState({
            start_date: date
        })
    }

    handleEndDateChange(date) {
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

    createDateRange() {
        let counter = moment(this.state.start_date).startOf('month');
        let dates = [JSON.parse(JSON.stringify(counter))];
        console.log("counter");
        while (counter.isBefore(this.state.end_date)) {
            console.log(counter);
            dates.push(moment(JSON.parse(JSON.stringify(counter))));
            counter.add(1, 'month');
        }
        console.log(dates);
        return dates;
    }

    isLoaded() {
        return (this.state.complex !== null && this.state.units !== [])
    }
    render() {
        if (this.isLoaded()) {
            const unit_rows = this.state.units.map(unit =>
                <UnitMonthlyRow 
                unit_id={unit.id} 
                start_date={moment(this.state.start_date).format("YYYY-MM-DD")} 
                end_date={moment(this.state.end_date).format("YYYY-MM-DD")} 
                reading_type="" 
                />
            );
            const dates = this.createDateRange();
            const date_columns = dates.map(date =>
                <th> { moment(date).format("MMM YYYY") } </th>
            );

            return (
                <div>
                    <Row>
                        <Col s={4}>
                            <img width="400px" height="200px" src={"/"+this.state.complex.image}/>
                        </Col>
                        <Col s={4}>
                            <h2>{this.state.complex.address}</h2>
                        </Col>
                    </Row>
                    <Row>
                        <Col s={3}> 
                            <div>Start Date</div> <div> 
                                <DatePicker
                                    selected={new Date(moment(this.state.start_date).format("YYYY-MM-DD"))}
                                    onChange={this.handleStartDateChange}/>
                            </div>
                        </Col>

                        <Col s={3}> 
                            <div>End Date</div> <div> 
                                <DatePicker
                                    selected={new Date(moment(this.state.end_date).format("YYYY-MM-DD"))}
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
                                    {date_columns}
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
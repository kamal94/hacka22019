import React from 'react';
import './App.css';
import { Row, Col} from 'react-materialize';
import { fetchUnit } from './api';
import moment from 'moment';
import UnitChart from './unit-chart';

import "react-datepicker/dist/react-datepicker.css";

export class Unit extends React.Component<{ matches }, any> {
    constructor(props) {
        super(props);
        this.state = {
            unit_id: props.match.params.id,
            readings: []
        }
    }

    handleStartDateChange(date) {
        console.log("start date:", date);
        console.log("start date:", moment(date));
        this.setState({
            start_date: date
        })
    }

    handleEndDateChange(date) {
        console.log("end date:", date);
        console.log("end date:", moment(date));
        this.setState({
            end_date: date
        })
    }

    componentDidMount() {
        fetchUnit(this.state.unit_id)
            .then(res =>
                this.setState({
                    unit: res.data
                })
            )
    }

    isLoaded() {
        return (this.state.unit !== null && this.state.readings !== [])
    }
    render() {
        if (this.isLoaded()) {
            return (
                <div>
                    <Row>
                        <Col s={12}><h2>{this.state.unit.address}</h2></Col>
                    </Row>
                    <Row>
                        <Col l={12}>
                            <UnitChart unit_id={this.state.unit_id} allowance={this.state.unit.allowance} />
                        </Col>
                    </Row>
                </div>
            )
        } else {
            return <div>Loading</div>
        }
    }
} 
import * as React from 'react';
import { Button, Card, Navbar, Row, Col, Table, } from 'react-materialize';
import { fetchMonthlyReadings, fetchReadings, fetchUnit } from './api';

export interface IUnitMonthlyRowProps {
    unit_id,
    start_date: string,
    end_date: string,
    reading_type: 'GAS' | 'ELECTRICITY' | ''
}

export class UnitMonthlyRow extends React.Component<IUnitMonthlyRowProps, any> {

    constructor(props: IUnitMonthlyRowProps) {
        super(props);
        this.state = {
            unit_id: props.unit_id,
            unit: null,
            reading_type: props.reading_type,
            start_date: props.start_date,
            end_date: props.end_date,
            readings: []
        }
    }

    componentDidMount() {
        fetchMonthlyReadings(this.state.unit_id, this.state.start_date, this.state.end_date, this.state.reading_type)
            .then(res => this.setState({ readings: res.data }))
        fetchUnit(this.state.unit_id).then(res => this.setState({ unit: res.data }))
    }

    isLoaded() {
        return (this.state.unit != null && this.state.reading != [])
    }

    public render() {
        if (this.isLoaded()) {
            // const data_columns = this.state.reading.sort()
            const columns = Object.entries(this.state.readings).map((date_usage, index) => {   
                    return <td> { date_usage[1] } </td>
                }
            );
            return (
                <tr>
                    <td>
                        {this.state.unit.address}
                    </td>
                    <td>
                        {this.state.unit.bed_number}
                    </td>
                    <td>
                        {this.state.unit.allowance}
                    </td>
                    {columns}
                </tr>
            )
        }
        else {
            return (
                <div>

                </div>
            );
        }
    }
}

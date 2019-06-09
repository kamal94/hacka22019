import React, { PureComponent } from 'react';
import {
    AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ReferenceLine, ResponsiveContainer
} from 'recharts';
import { fetchDailyElectricityReadings, fetchDailyGasReadings, fetchDailyTotalReadings} from './api';
import moment from 'moment';
export default class UnitChart extends PureComponent<any, any> {
    constructor(props) {
        super(props);
        this.state = {
            start_date: moment().subtract(30, 'days'),
            end_date: moment(),
            unit_id: props.unit_id,
            gas_readings: [],
            electricity_readings: [],
            total_readings: [],
            allowance: props.allowance
        }
    }

    componentDidMount() {
        fetchDailyTotalReadings(
            this.state.unit_id,
            moment(this.state.start_date).format("YYYY-MM-DD"),
            moment(this.state.end_date).format("YYYY-MM-DD")
        )
            .then(res => this.setState({ total_readings: res.data }))

        fetchDailyGasReadings(
            this.state.unit_id,
            moment(this.state.start_date).format("YYYY-MM-DD"),
            moment(this.state.end_date).format("YYYY-MM-DD")
        )
            .then(res => this.setState({ gas_readings: res.data }))

        fetchDailyElectricityReadings(
            this.state.unit_id,
            moment(this.state.start_date).format("YYYY-MM-DD"),
            moment(this.state.end_date).format("YYYY-MM-DD")
        )
            .then(res => this.setState({ electricity_readings: res.data }))
    }

    isLoaded() {
        return (this.state.gas_readings !== [] && this.state.electricity_readings !== [] && this.state.total_readings !== [])
    }

    createDates() {
        let start = moment(this.state.start_date);
        const end_condition = moment(this.state.end_date);
        var dates: moment.Moment[] = [];

        while (start.isBefore(end_condition)) {
            dates.push(moment(start.format("YYYY MM DD")));
            start = start.add(1, 'days');
        }
        return dates;
    }

    render() {
        if (this.isLoaded()) {
            const dates = this.createDates();
            console.log(this.state);
            let graph_data = dates.map(date => {return {date: date.format("YYYY-MM-DD")}})
            this.state.gas_readings.forEach(element => {
                console.log("looking for ", element.date, "in ", graph_data);
                let index = graph_data.findIndex((date) => date.date === element.date);
                if (!(graph_data[index] === undefined)) {
                    graph_data[index]['Gas'] = element.charge
                }
                console.log("the date:");
                console.log(index);
            });
            this.state.electricity_readings.forEach(element => {
                let index = graph_data.findIndex((date) => date.date === element.date);
                if (!(graph_data[index] === undefined)) {
                    graph_data[index]['Electricity'] = element.charge
                }
            });

            graph_data = graph_data.filter( datapoint => 
                (
                    datapoint.hasOwnProperty('Gas') ||
                    datapoint.hasOwnProperty('Electricity')
                )
            );
            
            console.log("graph data:")
            console.log(graph_data)
            // this.setState({graph_data: updated_graph_data});
            return (
                <ResponsiveContainer width="100%" height={600}>
                    <AreaChart
                        data={graph_data}
                        margin={{
                            top: 10, right: 30, left: 0, bottom: 0,
                        }}
                    >
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="date" />
                        <YAxis label={{ value: 'Dollars $', angle: -90, position: 'insideLeft' }}/>
                        <Tooltip />
                        <Area type="monotone" dataKey="Gas" stackId="1" stroke="#8884d8" fill="#8884d8" />
                        <Area type="monotone" dataKey="Electricity" stackId="1" stroke="#82ca9d" fill="#82ca9d" />
                        <ReferenceLine y={this.state.allowance/30} label={"Average Total Allowance "+this.state.allowance/30}  stroke="red" />
                        <Legend/>
                    </AreaChart>
                </ResponsiveContainer>
            );
        } else {
            return <div>Loading</div>
        }
    }
}

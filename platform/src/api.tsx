import axios from 'axios';
const IP = 'http://127.0.0.1:8000';

export const fetchComplexes = () => {
    return axios.get(
        IP+'/v1/complex',
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                'Authorization': 'Basic ' + btoa('kamal:123456'),
            }
        }
    )
}

export const fetchComplex = (complex_id) => axios.get(
    IP+'/v1/complex/'+complex_id,
    {
        method: 'GET',
        headers: {
            "Content-Type": "application/json",
            'Authorization': 'Basic ' + btoa('kamal:123456'),
        }
    }
)


export const fetchComplexUnits = (complex_id) => {
    return axios.get(
        IP+'/v1/complex/'+complex_id+'/units',
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                'Authorization': 'Basic ' + btoa('kamal:123456'),
            }
        }
    )
}

export const fetchUnit = (unit_id) => {
    return axios.get(
        IP+'/v1/unit/'+unit_id,
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                'Authorization': 'Basic ' + btoa('kamal:123456'),
            }
        }
    )
}


export const fetchReadings = (unit_id, start_date, end_date, reading_type) => {
    return axios.get(
        IP+'/v1/unit/'+unit_id+'/readings?start_date='+start_date+'&end_date='+end_date+'&reading_type='+reading_type,
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                'Authorization': 'Basic ' + btoa('kamal:123456'),
            }
        }
    )
}

export const fetchDailyGasReadings = (unit_id, start_date, end_date) => {
    return axios.get(
        IP+'/v1/unit/'+unit_id+'/readings/gas?start_date='+start_date+'&end_date='+end_date,
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                'Authorization': 'Basic ' + btoa('kamal:123456'),
            }
        }
    )
}


export const fetchDailyElectricityReadings = (unit_id, start_date, end_date) => {
    return axios.get(
        IP+'/v1/unit/'+unit_id+'/readings/electricity?start_date='+start_date+'&end_date='+end_date,
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                'Authorization': 'Basic ' + btoa('kamal:123456'),
            }
        }
    )
}


export const fetchDailyTotalReadings = (unit_id, start_date, end_date) => {
    return axios.get(
        IP+'/v1/unit/'+unit_id+'/readings/total?start_date='+start_date+'&end_date='+end_date,
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                'Authorization': 'Basic ' + btoa('kamal:123456'),
            }
        }
    )
}


export const fetchMonthlyReadings = (unit_id, start_date, end_date) => {
    return axios.get(
        IP+'/v1/unit/'+unit_id+'/readings/total/monthly?start_date='+start_date+'&end_date='+end_date,
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                'Authorization': 'Basic ' + btoa('kamal:123456'),
            }
        }
    )
}
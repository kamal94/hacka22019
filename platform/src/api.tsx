import axios from 'axios';
const IP = 'http://127.0.0.1:8000';

export const fetchComplexes = async () => {
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

export const fetchComplex = async (complex_id) => {
    return axios.get(
        IP+'/v1/complex/'+complex_id,
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                'Authorization': 'Basic ' + btoa('kamal:123456'),
            }
        }
    )
}


export const fetchComplexUnits = async (complex_id) => {
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

export const fetchUnit = async (unit_id) => {
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


export const fetchReadings = async (unit_id, start_date, end_date, reading_type) => {
    return axios.get(
        IP+'/v1/unit/'+unit_id+'/readings?'+'start_date='+start_date+'&end_date='+end_date+'&reading_type='+reading_type,
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                'Authorization': 'Basic ' + btoa('kamal:123456'),
            }
        }
    )
}


export const fetchMonthlyReadings = async (unit_id, start_date, end_date, reading_type) => {
    return axios.get(
        IP+'/v1/unit/'+unit_id+'/readings/monthly?'+'start_date='+start_date+'&end_date='+end_date+'&reading_type='+reading_type,
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                'Authorization': 'Basic ' + btoa('kamal:123456'),
            }
        }
    )
}
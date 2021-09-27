import axios from 'axios';

const baseUrl = "http://localhost:5001"

export const get = (middleUrl, payload) => {
    return axios.get(baseUrl + middleUrl, payload)
};

export const post = (middleUrl, payload) => {
    return axios.post(baseUrl + middleUrl, payload.body, {
        headers: payload.headers
    })
};

export const postNoHeader = (middleUrl, payload) => {
    return axios.post(baseUrl + middleUrl, payload.body)
};
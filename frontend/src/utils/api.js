import axios from 'axios';

const baseUrl = process.env.REACT_APP_API_URL
console.log(baseUrl)
console.log("aaaaa")
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

export const _delete = (middleUrl, payload) => {
    return axios.delete(baseUrl + middleUrl, payload)
};
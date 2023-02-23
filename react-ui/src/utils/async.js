import React from 'react';
import axios from 'axios';
import configData from '../config';

const ENDPOINT_URL = configData.API_SERVER + 'openai';

const useAsyncEndpoint = (fn) => {
    const [res, setRes] = React.useState({ data: null, complete: false, pending: false, error: false });
    const [req, setReq] = React.useState();

    React.useEffect(() => {
        if (!req) return;
        setRes({ data: null, pending: true, error: false, complete: false });
        axios(req)
            .then((res) => setRes({ data: res.data, pending: false, error: false, complete: true }))
            .catch(() => setRes({ data: null, pending: false, error: true, complete: true }));
    }, [req]);

    return [res, (...args) => setReq(fn(...args))];
};

export const postGenerateTextEndpoint = (endpoint) => {
    return useAsyncEndpoint((data) => ({ url: ENDPOINT_URL + '/' +endpoint, method: 'POST', data }));
};

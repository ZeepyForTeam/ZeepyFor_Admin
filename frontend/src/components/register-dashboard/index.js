import styled from 'styled-components';
import React from 'react'
import Header from '../header'

const DashboardBody = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
`

const RegisterBody = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 80vh;
    transition: all 0.1s ease;
`;

const RegisterDashboard = () => {

    return (
        <DashboardBody>
            <Header name="관리자 계정 생성"></Header>
            <RegisterBody>
            </RegisterBody>
        </DashboardBody>
    );
}

export default RegisterDashboard;
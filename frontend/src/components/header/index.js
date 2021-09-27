import styled from 'styled-components';
import React from 'react'

const HeaderBody = styled.div`
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 64px;
    transition: all 0.1s ease;
`;

const HeaderCol = styled.div`
    display: flex;
    font-family: Noto Sans KR;
    align-items: center;
    margin-left: 10px;
    margin-right: 10px;
    font-size: 20px;
    font-weight: bold;
    color: #6289ED;
`;

const Header = ({ name }) => {
    return (
        <HeaderBody style={{ backgroundColor: '#FDF4DF' }}>
            <HeaderCol>{name}</HeaderCol>
        </HeaderBody>
    );
}

export default Header;
import styled from 'styled-components';
import React from 'react'

// Emphasis Text Pink
const Etp = styled.div` 
    display: inline-block;
    font-family: Noto Sans KR;
    font-size: 14px;
    font-weight: bold;
    color: #ff607f;
`

// Emphasis Text Red
const Etr = styled.div` 
    display: inline-block;
    font-family: Noto Sans KR;
    font-size: 14px;
    font-weight: bold;
    color: red;
`

// Emphasis Text Red
const EtrBig = styled.div` 
    display: inline-block;
    font-family: Noto Sans KR;
    font-size: 20px;
    font-weight: bold;
    color: red;
`

const OptionDescription = styled.div`
    font-family: Noto Sans KR;
    margin-left: 14px;
    font-size: 14px;
    color: #282c34;
`

const DateJobDescription = () => {
    return (
        <OptionDescription>
            작동 날짜를 지정합니다. 선택항목은 다음과 같이 분류됩니다.<br />
            <ul>
                <li><Etp>작업할 년도</Etp></li>
                <li><Etp>작업할 월자</Etp></li>
                <li><Etp>작업할 일자</Etp></li>
                <li><Etp>작업할 시간</Etp></li>
                <li><Etp>작업할 분</Etp></li>
            </ul>
            작업의 경우 등록한 년도, 월, 일, 시간, 분에 선택하신 작업 내용을 <Etp>자동으로</Etp> 인지하여 처리합니다.<br />
            작업은 단발성으로 이루어지기 때문에 명확한 날짜를 입력하셔야 합니다.
        </OptionDescription>
    );
}

export default DateJobDescription;
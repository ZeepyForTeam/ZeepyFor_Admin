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

const DateJobValueDescription = () => {
    return (
        <OptionDescription>
            작업 내용을 지정합니다. 선택항목은 다음과 같이 분류됩니다.<br />
            <ul>
                <li><Etp>작업 시작 년도</Etp></li>
                <li><Etp>작업 시작 월자</Etp></li>
                <li><Etp>작업 종료 년도</Etp></li>
                <li><Etp>작업 종료 월자</Etp></li>
            </ul>
            작업 내용에 따라 지정해야할 정보가 다릅니다<br />
            <Etp>부동산 데이터 추출</Etp><br />
            데이터를 추출 시작할 년도, 월자 를 추출 종료할 년도, 월자를 지정합니다.<br />
            조건의 경우 시작할 날짜 부터 시작해서 추출 종료할 날짜를 포함하는 것이 아닌 그 전 년도 월자에서 작업이 종료됩니다<br />
            <Etp>그외 작업들</Etp><br />
            데이터 작업을 시작할 년도, 월자 만을 기입합니다.<br />
            만약 지피 단발 서버 부동산 정보 삽입의 경우 2021년 6월로 입력하면, 건물 거래 정보에서 2021년 6월에 거래된 항목만 작업이 이루어집니다.
        </OptionDescription>
    );
}

export default DateJobValueDescription;
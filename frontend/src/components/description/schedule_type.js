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

const OptionDescription = styled.div`
    font-family: Noto Sans KR;
    margin-left: 14px;
    font-size: 14px;
    color: #282c34;
`

const ScheduleTypeDescription = () => {
    return (
        <OptionDescription>
            스케줄 방식을 지정합니다. 스케줄 방식은 다음과 같이 분류됩니다.<br />
            <ul>
                <li><Etp>반복성 작업</Etp></li>
                <li><Etp>일회성 작업</Etp></li>
            </ul>
            <Etp>반복성 작업</Etp>의 경우 매월 지정 날짜 시간 분 에 맞춰서 예약한 작업을 <Etp>반복 수행</Etp>합니다.<br />
            <Etp>일회성 작업</Etp>의 경우 지정한 년도 월 날짜 시간 분 에 맞춰서 예약한 작업을 <Etp>일회 수행</Etp>합니다.
        </OptionDescription>
    );
}

export default ScheduleTypeDescription;
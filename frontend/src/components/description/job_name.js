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

const JobNameDescription = () => {
    return (
        <OptionDescription>
            작업의 이름을 작성합니다. 주의사항은 아래와 같습니다.<br />
            <ul>
                <li><Etp>이모지 사용 금지</Etp></li>
                <li><Etp>"/" 사용 금지(스래시 사용 금지)</Etp></li>
            </ul>
            작업 이름을 작성하면 스케줄 로그, 대기 저장소에서 여러분이 등록한 작업을 쉽게 확인할 수 있습니다
        </OptionDescription>
    );
}

export default JobNameDescription;
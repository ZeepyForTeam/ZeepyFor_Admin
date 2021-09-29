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

const JobTypeDescription = () => {
    return (
        <OptionDescription>
            작업 내용을 지정합니다. 작업 내용은 다음과 같이 분류됩니다.<br />
            <ul>
                <li><Etp>부동산 데이터 추출</Etp></li>
                <li><Etp>카카오 주소 API 호출</Etp></li>
                <li><Etp>지피 대용량 서버 부동산 정보 삽입</Etp></li>
                <li><Etp>지피 단발 서버 부동산 정보 삽입</Etp></li>
            </ul>
            <Etp>부동산 데이터 추출</Etp>의 경우 <Etp>공공 API</Etp> 를 이용해 해당 월에 거래된 부동산 정보를 불러옵니다.<br />
            <Etp>카카오 주소 API 호출</Etp>의 경우 DB에 존재하는 부동산 정보 중에 지정한 날짜에 거래된 데이터 중 위치 정보가 없는 경우 <Etp>카카오 API</Etp> 를 통해 위치 정보를 갱신합니다.<br />
            <Etp>지피 대용량 서버 부동산 정보 삽입</Etp>의 경우 <Etp>배치 인서트</Etp> 를 통한 대용량 건물 정보를 지피 매인 서버에 업로드 합니다.<br />
            <Etp>지피 단발 서버 부동산 정보 삽입</Etp>의 경우 <Etp>단일 인서트</Etp> 를 통한 대용량 건물 정보를 지피 매인 서버에 업로드 합니다.<br /><br />
            <EtrBig>주의 !!!</EtrBig><br />
            <Etr>"지피 대용량 서버 부동산 정보 삽입" 은 서버 정식 배포 완료되었다는 신호 전까지 사용하시면 안됩니다!!</Etr><br />
            <Etr>"지피 단발 서버 부동산 정보 삽입" 은 시간이 굉장히 오래 걸리는 작업입니다!! 작업 예약하시기 전에 충분한 휴식을 즐기시면서 하세요!!</Etr>
        </OptionDescription>
    );
}

export default JobTypeDescription;
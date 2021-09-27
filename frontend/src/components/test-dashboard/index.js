import styled from 'styled-components';
import React from 'react'
import Header from '../header'

const DashboardBody = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
`

const TestBody = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 80vh;
`;

const SorryText = styled.div`
    font-size: 40px;
    font-weight: 800;
    fint-family: Noto-Sans KR
`

const TestDashboard = () => {

    return (
        <DashboardBody>
            <Header name="실험용 기능"></Header>
            <TestBody>
                <SorryText>
                    서비스 준비중
                </SorryText>
                <SorryText>
                    예상 서비스
                </SorryText>
                <SorryText>
                    건물 정보 스케줄링, 리뷰 데이터 대량 삽입, 건물 데이터 추가 삽입 등등
                </SorryText>
                <SorryText>
                    기능 추가 요구사항 Minky에게 연락주세요
                </SorryText>
                <SorryText>
                    zx6486@gmail.com
                </SorryText>
            </TestBody>
        </DashboardBody>
    );
}

export default TestDashboard;
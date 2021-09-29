import Drawer from '@mui/material/Drawer';
import Toolbar from '@mui/material/Toolbar';
import Divider from '@mui/material/Divider';
import SpeedIcon from '@mui/icons-material/Speed';
import ApartmentIcon from '@mui/icons-material/Apartment';
import SupervisorAccountIcon from '@mui/icons-material/SupervisorAccount';
import ExitToAppIcon from '@mui/icons-material/ExitToApp';
import AccessAlarmsIcon from '@mui/icons-material/AccessAlarms';
import DescriptionIcon from '@mui/icons-material/Description';
import HourglassEmptyIcon from '@mui/icons-material/HourglassEmpty';
import { useHistory } from "react-router-dom";
import { deleteCookie } from '../../utils/cookie';
import styled from 'styled-components';
import React from 'react'

const ZeepyTopIcon = styled.img`
    width: 30px;
    height: 30px;
    border-radius: 5px;
    margin-right: 15px;
`

const DrawerList = styled.div`
    display: flex;
    flex-direction: column;
    height: 80vh;
`;

const DrawerItem = styled.div`
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 5px;
    padding-right: 5px;
    display: flex;
    flex-direction: row;
    cursor: pointer;
    color: #282c34;
    &:hover {
        border-radius: 10px;
        background-color: #d6d6d6;
        color: #6289ED !important;
    }
    transition: all ease 0.3s;
`;

const DrawerIcon = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 20px;
`;

const DrawerText = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Noto Sans KR;
    font-size: 16px; 
    font-weight: 600;
`;

const DrawerBar = () => {
    const drawerWidth = 260;

    const history = useHistory();
    const handleRoute = (path) => {
        history.push(path);
    }

    const logout = () => {
        deleteCookie("token", "")
        history.push("login");
    }

    return (
        <Drawer
            sx={{
                width: drawerWidth,
                flexShrink: 0,
                '& .MuiDrawer-paper': {
                    width: drawerWidth,
                    boxSizing: 'border-box',
                },
            }}
            variant="permanent"
            anchor="left"
        >
            <Toolbar style={{ backgroundColor: '#FDF4DF' }}>
                <div style={{
                    display: 'flex', alignItens: 'center', justifyContent: 'center',
                    fontFamily: 'Noto Sans KR', fontSize: '20px', fontWeight: 'bold', color: '#6289ED'
                }}>
                    <ZeepyTopIcon src="/zeepy.png"></ZeepyTopIcon>
                    ZEEPY ADMIN
                </div>
            </Toolbar>
            <Divider />
            <DrawerList>
                <DrawerItem button onClick={() => { handleRoute("/test") }}>
                    <DrawerIcon>
                        <SpeedIcon />
                    </DrawerIcon>
                    <DrawerText>
                        실험용 기능
                    </DrawerText>
                </DrawerItem>
                <Divider />
                <DrawerItem button onClick={() => { handleRoute("/schedule") }}>
                    <DrawerIcon>
                        <DescriptionIcon />
                    </DrawerIcon>
                    <DrawerText>
                        스케줄 로그 저장소
                    </DrawerText>
                </DrawerItem>
                <Divider />
                <DrawerItem button onClick={() => { handleRoute("/schedule/wait") }}>
                    <DrawerIcon>
                        <HourglassEmptyIcon />
                    </DrawerIcon>
                    <DrawerText>
                        스케줄링 대기 저장소
                    </DrawerText>
                </DrawerItem>
                <Divider />
                <DrawerItem button onClick={() => { handleRoute("/schedule/register") }}>
                    <DrawerIcon>
                        <AccessAlarmsIcon />
                    </DrawerIcon>
                    <DrawerText>
                        스케줄 등록
                    </DrawerText>
                </DrawerItem>
                <Divider />
                <DrawerItem button onClick={() => { handleRoute("/storage") }}>
                    <DrawerIcon>
                        <ApartmentIcon />
                    </DrawerIcon>
                    <DrawerText>
                        건물 데이터 저장소
                    </DrawerText>
                </DrawerItem>
                <Divider />
                <DrawerItem button onClick={() => { handleRoute("/register") }}>
                    <DrawerIcon>
                        <SupervisorAccountIcon />
                    </DrawerIcon>
                    <DrawerText>
                        관리자 계정 생성
                    </DrawerText>
                </DrawerItem>
                <Divider />
                <DrawerItem button onClick={logout}>
                    <DrawerIcon>
                        <ExitToAppIcon />
                    </DrawerIcon>
                    <DrawerText>
                        로그아웃
                    </DrawerText>
                </DrawerItem>
                <Divider />
            </DrawerList>
        </Drawer>
    );
}

export default DrawerBar;

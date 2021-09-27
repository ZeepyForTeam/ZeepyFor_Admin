import styled from 'styled-components';
import React from 'react'
import Card from '@mui/material/Card';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import AccountCircle from '@mui/icons-material/AccountCircle';
import VpnKeyIcon from '@mui/icons-material/VpnKey';
import Button from '@mui/material/Button';
import LoginIcon from '@mui/icons-material/Login';
import { postNoHeader } from '../../utils/api';
import { setCookie } from '../../utils/cookie';
import { redirect } from '../../utils/redirect';

const DashboardBody = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100vh;
`

const LoginBody = styled.div`
    display: flex;
    padding-top: 20px;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-bottom: 150px;
`;

const ZeepyIcon = styled.img`
    width: 150px;
    height: 150px;
    border-radius: 10px;
`

const LoginTitle = styled.div`
    font-family: Roboto;
    font-size: 30px;
    font-weight: bold;
    color: #6289ED;
    padding-bottom: 30px;
`

const LoginDashboard = ({ setErrorAlert, setAlertMessage, }) => {
    const [email, setEmail] = React.useState(null)
    const [password, setPassword] = React.useState(null)

    const login = () => {
        postNoHeader("/api/auth", { body: { email: email, password: password } })
            .then(response => {
                let token = response.data.access_token
                setCookie("token", token, 3)
                redirect("/storage");
            })
            .catch(error => {
                setAlertMessage("로그인 실패 - 이메일, 비밀번호를 확인하세요")
                setErrorAlert(true)
                setTimeout(() => setErrorAlert(false), 2000);
            })
    }

    return (
        <DashboardBody>
            <ZeepyIcon src="/zeepy.png"></ZeepyIcon>
            <LoginBody>
                <LoginTitle>ZeepyFor_Admin</LoginTitle>
                <Card sx={{ width: 400, minHeight: 200, paddingTop: '10px' }}>
                    <Box sx={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'center', marginBottom: '10px' }}>
                        <AccountCircle sx={{ color: '#6289ED', mr: 1, my: 0.5 }} />
                        <TextField
                            sx={{ fontFamily: 'Noto Sans KR', fontWeight: 'bold' }}
                            id="input-with-sx"
                            label="Email"
                            variant="standard"
                            onChange={(event) => { setEmail(event.target.value) }}
                        />
                    </Box>
                    <Box sx={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'center', marginBottom: '25px' }}>
                        <VpnKeyIcon sx={{ color: '#6289ED', mr: 1, my: 0.5 }} />
                        <TextField
                            sx={{ fontFamily: 'Noto Sans KR', fontWeight: 'bold' }}
                            id="input-with-sx"
                            label="PW"
                            variant="standard"
                            onChange={(event) => { setPassword(event.target.value) }}
                        />
                    </Box>
                    <Box sx={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'center' }}>
                        <Button
                            sx={{ fontFamily: 'Noto Sans KR', fontWeight: 'bold', backgroundColor: '#FDF4DF', color: '#6289ED' }}
                            startIcon={<LoginIcon />}
                            variant="contained"
                            onClick={login}
                        >
                            Login
                        </Button>
                    </Box>
                </Card>
            </LoginBody>
        </DashboardBody>
    );
}

export default LoginDashboard;
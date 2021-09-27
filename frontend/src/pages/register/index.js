import DrawerBar from '../../components/drawer-bar'
import Box from '@mui/material/Box';
import RegisterDashboard from '../../components/register-dashboard';
import { redirect } from '../../utils/redirect';
import { validate } from '../../utils/cookie';
import React from 'react'

const Register = () => {

    React.useEffect(() => {
        if (!validate("token")) redirect("/login");
    }, [])

    return (
        <Box sx={{ display: 'flex' }}>
            <DrawerBar></DrawerBar>
            <RegisterDashboard></RegisterDashboard>
        </Box>
    );
}

export default Register;

import DrawerBar from '../../components/drawer-bar'
import Box from '@mui/material/Box';
import TestDashboard from '../../components/test-dashboard';
import { redirect } from '../../utils/redirect';
import { validate } from '../../utils/cookie';
import React from 'react'

const Test = () => {

    React.useEffect(() => {
        if (!validate("token")) redirect("/login");
    }, [])

    return (
        <Box sx={{ display: 'flex' }}>
            <DrawerBar></DrawerBar>
            <TestDashboard></TestDashboard>
        </Box>
    );
}

export default Test;

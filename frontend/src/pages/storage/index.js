import DrawerBar from '../../components/drawer-bar'
import BuildingDashboard from '../../components/building-dashboard';
import Box from '@mui/material/Box';
import { redirect } from '../../utils/redirect';
import { validate } from '../../utils/cookie';
import React from 'react'

const Storage = () => {

    React.useEffect(() => {
        if (!validate("token")) redirect("/login");
    }, [])

    return (
        <Box sx={{ display: 'flex' }}>
            <DrawerBar></DrawerBar>
            <BuildingDashboard></BuildingDashboard>
        </Box>
    );
}

export default Storage;

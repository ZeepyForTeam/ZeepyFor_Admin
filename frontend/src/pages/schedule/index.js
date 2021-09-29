import DrawerBar from '../../components/drawer-bar'
import Box from '@mui/material/Box';
import ScheduleDashboard from '../../components/schedule-dashboard';
import { redirect } from '../../utils/redirect';
import { validate } from '../../utils/cookie';
import React from 'react'

const Schedule = ({ setErrorAlert, setSuccessAlert, setAlertMessage, }) => {

    React.useEffect(() => {
        if (!validate("token")) redirect("/login");
    }, [])

    return (
        <Box sx={{ display: 'flex' }}>
            <DrawerBar></DrawerBar>
            <ScheduleDashboard
                setErrorAlert={setErrorAlert}
                setSuccessAlert={setSuccessAlert}
                setAlertMessage={setAlertMessage}
            ></ScheduleDashboard>
        </Box>
    );
}

export default Schedule;

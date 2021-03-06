import DrawerBar from '../../components/drawer-bar'
import Box from '@mui/material/Box';
import ScheduleWaitDashboard from '../../components/schedule-wait-dashboard';
import { redirect } from '../../utils/redirect';
import { validate } from '../../utils/cookie';
import React from 'react'

const ScheduleWait = ({ setErrorAlert, setSuccessAlert, setAlertMessage, }) => {

    React.useEffect(() => {
        if (!validate("token")) redirect("/login");
    }, [])

    return (
        <Box sx={{ display: 'flex' }}>
            <DrawerBar></DrawerBar>
            <ScheduleWaitDashboard
                setErrorAlert={setErrorAlert}
                setSuccessAlert={setSuccessAlert}
                setAlertMessage={setAlertMessage}
            ></ScheduleWaitDashboard>
        </Box>
    );
}

export default ScheduleWait;

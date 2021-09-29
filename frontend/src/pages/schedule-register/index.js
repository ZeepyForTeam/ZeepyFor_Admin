import DrawerBar from '../../components/drawer-bar'
import Box from '@mui/material/Box';
import ScheduleRegisterDashboard from '../../components/schedule-register-dashboard';
import { redirect } from '../../utils/redirect';
import { validate } from '../../utils/cookie';
import React from 'react'

const ScheduleRegister = ({ setErrorAlert, setSuccessAlert, setAlertMessage, }) => {

    React.useEffect(() => {
        if (!validate("token")) redirect("/login");
    }, [])

    return (
        <Box sx={{ display: 'flex' }}>
            <DrawerBar></DrawerBar>
            <ScheduleRegisterDashboard
                setErrorAlert={setErrorAlert}
                setSuccessAlert={setSuccessAlert}
                setAlertMessage={setAlertMessage}
            ></ScheduleRegisterDashboard>
        </Box>
    );
}

export default ScheduleRegister;

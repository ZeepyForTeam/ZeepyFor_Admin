import './App.css';
import { BrowserRouter, Switch, Route, Redirect } from "react-router-dom";
import Alert from '@mui/material/Alert';
import Collapse from '@mui/material/Collapse';
import Box from '@mui/material/Box';
import Login from './pages/login'
import Register from './pages/register'
import Storage from './pages/storage'
import Test from './pages/test'
import Schedule from './pages/schedule'
import ScheduleRegister from './pages/schedule-register'
import ScheduleWait from './pages/schedule-wait'
import React from 'react'

const App = () => {
    const [errorAlert, setErrorAlert] = React.useState(false)
    const [successAlert, setSuccessAlert] = React.useState(false)
    const [warningAlert, setWarningAlert] = React.useState(false)
    const [alertMessage, setAlertMessage] = React.useState("")
    return (
        <BrowserRouter>
            <Box sx={{ top: 0, left: 0, width: '100vw', position: 'absolute', zIndex: 100000 }}>
                <Collapse in={errorAlert}>
                    <Alert variant="filled" severity="error">
                        {alertMessage}
                    </Alert>
                </Collapse>
            </Box>
            <Box sx={{ top: 0, left: 0, width: '100vw', position: 'absolute', zIndex: 100000 }}>
                <Collapse in={warningAlert}>
                    <Alert variant="filled" severity="warning">
                        {alertMessage}
                    </Alert>
                </Collapse>
            </Box>
            <Box sx={{ top: 0, left: 0, width: '100vw', position: 'absolute', zIndex: 100000 }}>
                <Collapse in={successAlert}>
                    <Alert variant="filled" severity="success">
                        {alertMessage}
                    </Alert>
                </Collapse>
            </Box>
            <Switch>
                <Route exact path="/storage">
                    <Storage
                        setErrorAlert={setErrorAlert}
                        setSuccessAlert={setSuccessAlert}
                        setAlertMessage={setAlertMessage}
                    />
                </Route>
                <Route exact path="/test">
                    <Test />
                </Route>
                <Route exact path="/schedule">
                    <Schedule
                        setErrorAlert={setErrorAlert}
                        setSuccessAlert={setSuccessAlert}
                        setAlertMessage={setAlertMessage}
                    />
                </Route>
                <Route exact path="/schedule/register">
                    <ScheduleRegister
                        setErrorAlert={setErrorAlert}
                        setSuccessAlert={setSuccessAlert}
                        setAlertMessage={setAlertMessage}
                    />
                </Route>
                <Route exact path="/schedule/wait">
                    <ScheduleWait
                        setErrorAlert={setErrorAlert}
                        setSuccessAlert={setSuccessAlert}
                        setAlertMessage={setAlertMessage}
                    />
                </Route>
                <Route exact path="/register">
                    <Register />
                </Route>
                <Route exact path="/login">
                    <Login
                        setErrorAlert={setErrorAlert} setAlertMessage={setAlertMessage}
                    />
                </Route>
                <Redirect path="*" to="/storage" />
            </Switch>
        </BrowserRouter >
    );
}

export default App;

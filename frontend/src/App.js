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
import React from 'react'

const App = () => {
    const [errorAlert, setErrorAlert] = React.useState(false)
    const [successAlert, setSuccessAlert] = React.useState(false)
    const [warningAlert, setWarningAlert] = React.useState(false)
    const [alertMessage, setAlertMessage] = React.useState("")
    return (
        <BrowserRouter>
            <Box sx={{ top: 0, left: 0, width: '100vw', position: 'absolute', }}>
                <Collapse in={errorAlert}>
                    <Alert variant="filled" severity="error">
                        {alertMessage}
                    </Alert>
                </Collapse>
            </Box>
            <Box sx={{ top: 0, left: 0, width: '100vw', position: 'absolute', }}>
                <Collapse in={warningAlert}>
                    <Alert variant="filled" severity="warning">
                        {alertMessage}
                    </Alert>
                </Collapse>
            </Box>
            <Box sx={{ top: 0, left: 0, width: '100vw', position: 'absolute', }}>
                <Collapse in={successAlert}>
                    <Alert variant="filled" severity="success">
                        {alertMessage}
                    </Alert>
                </Collapse>
            </Box>
            <Switch>
                <Route exact path="/storage">
                    <Storage />
                </Route>
                <Route path="/test">
                    <Test />
                </Route>
                <Route path="/schedule">
                    <Schedule />
                </Route>
                <Route path="/schedule/register">
                    <ScheduleRegister />
                </Route>
                <Route path="/register">
                    <Register />
                </Route>
                <Route path="/login">
                    <Login setErrorAlert={setErrorAlert} setAlertMessage={setAlertMessage} />
                </Route>
                <Redirect path="*" to="/storage" />
            </Switch>
        </BrowserRouter >
    );
}

export default App;

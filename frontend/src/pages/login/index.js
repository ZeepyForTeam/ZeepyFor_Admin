import LoginDashboard from '../../components/login-dashboard';
const Login = ({ setErrorAlert, setAlertMessage, }) => {
    return (
        <LoginDashboard setErrorAlert={setErrorAlert} setAlertMessage={setAlertMessage}></LoginDashboard>
    )
}

export default Login;

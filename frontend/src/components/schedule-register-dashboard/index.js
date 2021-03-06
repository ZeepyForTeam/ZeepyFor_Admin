import styled from 'styled-components';
import React from 'react'
import { getCookie, deleteCookie } from '../../utils/cookie';
import { redirect } from '../../utils/redirect';
import {
    runTypeList, jobTypeList, returnYearList, returnUpperYearList, returnMonthList, returnDayList, returnHourList, returnMinuteList
} from '../../data/select_schedule';
import { post } from '../../utils/api';
import JobTypeDescription from "../description/job_type"
import ScheduleTypeDescription from "../description/schedule_type"
import CronJobDescription from "../description/cron_job"
import DateJobDescription from "../description/date_job"
import DateJobValueDescription from "../description/date_job_value"
import JobNameDescription from "../description/job_name"
import Header from '../header'
import Selecter from '../selecter'
import Divider from '@mui/material/Divider';
import HelpOutlineIcon from '@mui/icons-material/HelpOutline';
import TextField from '@mui/material/TextField';
import AccountCircle from '@mui/icons-material/AccountCircle';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';
import moment from 'moment'

const DashboardBody = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
`

const SelectBody = styled.div`
    display: flex;
    flex-direction: column;
    margin-bottom: 150px;
`;

const SelectContainer = styled.div`
    display: flex;
    flex-direction: row;
`

const OptionHeader = styled.div`
    display: flex;
    flex-direction: row;
    padding-top: 10px;
    padding-bottom: 10px;
    align-items: center;
`

const OptionTitle = styled.div`
    font-family: Noto Sans KR;
    margin-left: 10px;
    font-size: 20px;
    font-weight: bold;
    color: #6289ED;
`

const ScheduleRegisterDashboard = ({ setErrorAlert, setSuccessAlert, setAlertMessage, }) => {
    const dayList = returnDayList()
    const hourList = returnHourList()
    const minuteList = returnMinuteList()
    const yearList = returnYearList()
    const monthList = returnMonthList()
    const upperYearList = returnUpperYearList()

    // ?????? ?????? ????????????
    const [nickname, setNickname] = React.useState('');
    // ?????? ?????? ????????????
    const [runType, setRunType] = React.useState('');
    const [jobType, setJobType] = React.useState('');
    // ?????? ????????????
    const [startYear, setStartYear] = React.useState('');
    const [startMonth, setStartMonth] = React.useState('');
    const [endYear, setEndYear] = React.useState('');
    const [endMonth, setEndMonth] = React.useState('');
    // ?????? ?????? ????????????
    const [year, setYear] = React.useState('');
    const [month, setMonth] = React.useState('');
    const [day, setDay] = React.useState('');
    const [hour, setHour] = React.useState('');
    const [minute, setMinute] = React.useState('');
    // ?????? ??????
    const [isHide0, setIsHide0] = React.useState(true);
    const [isHide1, setIsHide1] = React.useState(true);
    const [isHide2, setIsHide2] = React.useState(true);
    const [isHide3, setIsHide3] = React.useState(true);
    const [isHide4, setIsHide4] = React.useState(true);
    const [isHide5, setIsHide5] = React.useState(true);

    const registJob = () => {
        if (nickname === '') {
            setAlertMessage("?????? ????????? ???????????????")
            setErrorAlert(true)
            setTimeout(() => setErrorAlert(false), 2000);
            return
        }

        if (runType === '') {
            setAlertMessage("?????? ????????? ???????????????")
            setErrorAlert(true)
            setTimeout(() => setErrorAlert(false), 2000);
            return
        }

        if (jobType === '') {
            setAlertMessage("?????? ????????? ???????????????")
            setErrorAlert(true)
            setTimeout(() => setErrorAlert(false), 2000);
            return
        }

        if (runType === "cron") {
            if (day === "" || hour === "" || minute === "") {
                setAlertMessage("?????? ????????? ???????????????")
                setErrorAlert(true)
                setTimeout(() => setErrorAlert(false), 2000);
                return
            }
            callCronJobAPI()
        } else if (runType === "date") {
            if (year === "" || month === "" || day === "" || hour === "" || minute === "") {
                setAlertMessage("?????? ????????? ???????????????")
                setErrorAlert(true)
                setTimeout(() => setErrorAlert(false), 2000);
                return
            }

            if (jobType === "MOLIT") {
                if (startYear === "" || startMonth === "" || endYear === "" || endMonth === "") {
                    setAlertMessage("?????? ????????? ???????????????")
                    setErrorAlert(true)
                    setTimeout(() => setErrorAlert(false), 2000);
                    return
                }
            } else {
                if (startYear === "" || startMonth === "") {
                    setAlertMessage("?????? ????????? ???????????????")
                    setErrorAlert(true)
                    setTimeout(() => setErrorAlert(false), 2000);
                    return
                }
            }
            callDateJobAPI()

        } else {
            setAlertMessage("????????? ?????? ?????? - ??????????????? ???????????????")
            setErrorAlert(true)
            setTimeout(() => setErrorAlert(false), 2000);
            return
        }
    }

    const callDateJobAPI = () => {
        let date = new Date(year, month - 1, day, hour, minute, 0)
        let date_string = moment(date).format("YYYY-MM-DD HH:mm:ss")

        post("/api/jobs/date", {
            body: {
                nickname: nickname,
                run_date: date_string,
                run_type: jobType,
                arg_start_year: startYear,
                arg_start_month: startMonth,
                arg_end_year: endYear,
                arg_end_month: endMonth,
            }
        }).then(response => {
            setAlertMessage("???????????? ??????")
            setSuccessAlert(true)
            setTimeout(() => setSuccessAlert(false), 2000);
        }).catch(error => {
            if (error.response.status === 422 || error.response.status === 401) {
                deleteCookie("token", "")
                redirect("/login");
            } else {
                setAlertMessage("???????????? ?????? - ??????????????? ???????????????")
                setErrorAlert(true)
                setTimeout(() => setErrorAlert(false), 2000);
            }
        })
    }

    const callCronJobAPI = () => {
        post("/api/jobs/cron", {
            body: {
                nickname: nickname,
                run_type: jobType,
                cron_day: day,
                cron_hour: hour,
                cron_minute: minute,
            },
            headers: {
                Authorization: "Bearer " + getCookie("token")
            }

        }).then(response => {
            setAlertMessage("???????????? ??????")
            setSuccessAlert(true)
            setTimeout(() => setSuccessAlert(false), 2000);
        }).catch(error => {
            if (error.response.status === 422 || error.response.status === 401) {
                deleteCookie("token", "")
                redirect("/login");
            } else {
                setAlertMessage("???????????? ?????? - ??????????????? ???????????????")
                setErrorAlert(true)
                setTimeout(() => setErrorAlert(false), 2000);
            }
        })
    }

    return (
        <DashboardBody>
            <Header name="????????? ?????? (????????? ????????? F5??? ????????????)"></Header>
            <SelectBody>
                <OptionHeader>
                    <OptionTitle>????????? ?????? ?????? ??????</OptionTitle>
                    <HelpOutlineIcon
                        style={{ marginLeft: "10px", color: "#6289ED", cursor: "pointer" }}
                        onClick={() => { setIsHide0(!isHide0) }}
                    >
                    </HelpOutlineIcon>
                </OptionHeader>
                {!isHide0 && <JobNameDescription></JobNameDescription>}
                <Box
                    sx={
                        {
                            display: 'flex',
                            alignItems: 'flex-end',
                            justifyContent: 'left',
                            marginLeft: '10px',
                            paddingBottom: '10px',
                        }
                    }
                >
                    <AccountCircle sx={{ color: '#6289ED', mr: 1, my: 0.5 }} />
                    <TextField
                        sx={{ fontFamily: 'Noto Sans KR', fontWeight: 'bold' }}
                        id="input-with-sx"
                        label="?????? ??????"
                        variant="standard"
                        onChange={(event) => { setNickname(event.target.value) }}
                    />
                </Box>
                <OptionHeader>
                    <OptionTitle>????????? ?????? ?????? ??????</OptionTitle>
                    <HelpOutlineIcon
                        style={{ marginLeft: "10px", color: "#6289ED", cursor: "pointer" }}
                        onClick={() => { setIsHide1(!isHide1) }}
                    >
                    </HelpOutlineIcon>
                </OptionHeader>
                {!isHide1 && <ScheduleTypeDescription></ScheduleTypeDescription>}
                <Selecter
                    label="?????? ??????"
                    value={runType}
                    valueList={runTypeList}
                    setValue={setRunType}
                    minWidth={200}
                ></Selecter>
                <Divider></Divider>
                <OptionHeader>
                    <OptionTitle>?????? ?????? ??????</OptionTitle>
                    <HelpOutlineIcon
                        style={{ marginLeft: "10px", color: "#6289ED", cursor: "pointer" }}
                        onClick={() => { setIsHide2(!isHide2) }}
                    >
                    </HelpOutlineIcon>
                </OptionHeader>
                {!isHide2 && <JobTypeDescription></JobTypeDescription>}
                <Selecter
                    label="?????? ??????"
                    value={jobType}
                    valueList={jobTypeList}
                    setValue={setJobType}
                    minWidth={300}
                ></Selecter>
                {runType === "date" &&
                    <div>
                        <Divider></Divider>
                        <OptionHeader>
                            <OptionTitle>????????? ????????? ?????? ?????? ??????</OptionTitle>
                            <HelpOutlineIcon
                                style={{ marginLeft: "10px", color: "#6289ED", cursor: "pointer" }}
                                onClick={() => { setIsHide3(!isHide3) }}
                            >
                            </HelpOutlineIcon>
                        </OptionHeader>
                        {!isHide3 && <DateJobValueDescription></DateJobValueDescription>}
                        <SelectContainer>
                            {yearList &&
                                <Selecter
                                    label="?????? ??????"
                                    value={startYear}
                                    valueList={yearList}
                                    setValue={setStartYear}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {monthList &&
                                <Selecter
                                    label="?????? ???"
                                    value={startMonth}
                                    valueList={monthList}
                                    setValue={setStartMonth}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {yearList &&
                                <Selecter
                                    label="?????? ??????"
                                    value={endYear}
                                    valueList={yearList}
                                    setValue={setEndYear}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {monthList &&
                                <Selecter
                                    label="?????? ???"
                                    value={endMonth}
                                    valueList={monthList}
                                    setValue={setEndMonth}
                                    minWidth={200}
                                ></Selecter>
                            }
                        </SelectContainer>
                        <Divider></Divider>
                        <OptionHeader>
                            <OptionTitle>????????? ????????? ?????? ?????? ??????</OptionTitle>
                            <HelpOutlineIcon
                                style={{ marginLeft: "10px", color: "#6289ED", cursor: "pointer" }}
                                onClick={() => { setIsHide4(!isHide4) }}
                            >
                            </HelpOutlineIcon>
                        </OptionHeader>
                        {!isHide4 && <DateJobDescription></DateJobDescription>}
                        <SelectContainer>
                            {upperYearList &&
                                <Selecter
                                    label="?????? ??????"
                                    value={year}
                                    valueList={upperYearList}
                                    setValue={setYear}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {monthList &&
                                <Selecter
                                    label="?????? ???"
                                    value={month}
                                    valueList={monthList}
                                    setValue={setMonth}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {dayList &&
                                <Selecter
                                    label="?????? ???"
                                    value={day}
                                    valueList={dayList}
                                    setValue={setDay}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {hourList &&
                                <Selecter
                                    label="?????? ??????"
                                    value={hour}
                                    valueList={hourList}
                                    setValue={setHour}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {minuteList &&
                                <Selecter
                                    label="?????? ???"
                                    value={minute}
                                    valueList={minuteList}
                                    setValue={setMinute}
                                    minWidth={200}
                                ></Selecter>
                            }
                        </SelectContainer>
                    </div>
                }
                {runType === "cron" &&
                    <div>
                        <Divider></Divider>
                        <OptionHeader>
                            <OptionTitle>????????? ????????? ?????? ?????? ??????</OptionTitle>
                            <HelpOutlineIcon
                                style={{ marginLeft: "10px", color: "#6289ED", cursor: "pointer" }}
                                onClick={() => { setIsHide5(!isHide5) }}
                            >
                            </HelpOutlineIcon>
                        </OptionHeader>
                        {!isHide5 && <CronJobDescription></CronJobDescription>}
                        <SelectContainer>
                            {dayList &&
                                <Selecter
                                    label="?????? ???"
                                    value={day}
                                    valueList={dayList}
                                    setValue={setDay}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {hourList &&
                                <Selecter
                                    label="?????? ??????"
                                    value={hour}
                                    valueList={hourList}
                                    setValue={setHour}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {minuteList &&
                                <Selecter
                                    label="?????? ???"
                                    value={minute}
                                    valueList={minuteList}
                                    setValue={setMinute}
                                    minWidth={200}
                                ></Selecter>
                            }
                        </SelectContainer>
                    </div>
                }
                <Box
                    sx={
                        {
                            display: 'flex',
                            alignItems: 'flex-end',
                            justifyContent: 'left',
                            marginLeft: '10px',
                            marginTop: '30px',
                        }
                    }
                >
                    <Button
                        sx={
                            {
                                fontFamily: 'Noto Sans KR',
                                fontWeight: 'bold',
                                backgroundColor: '#FDF4DF !important',
                                color: '#6289ED !important',
                                minWidth: "200px",
                                minHeight: "50px",
                            }
                        }
                        startIcon={<CheckCircleOutlineIcon />}
                        variant="contained"
                        onClick={registJob}
                    >
                        ?????? ????????????
                    </Button>
                </Box>
            </SelectBody>
        </DashboardBody>
    );
}

export default ScheduleRegisterDashboard;
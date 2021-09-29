import styled from 'styled-components';
import React from 'react'
import { postNoHeader } from '../../utils/api';
import { setCookie, getCookie, deleteCookie } from '../../utils/cookie';
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

const LoginDashboard = ({ setErrorAlert, setSuccessAlert, setAlertMessage, }) => {
    const dayList = returnDayList()
    const hourList = returnHourList()
    const minuteList = returnMinuteList()
    const yearList = returnYearList()
    const monthList = returnMonthList()
    const upperYearList = returnUpperYearList()

    // 작업 이름 파라미터
    const [nickname, setNickname] = React.useState('');
    // 구동 방식 파라미터
    const [runType, setRunType] = React.useState('');
    const [jobType, setJobType] = React.useState('');
    // 작업 파라미터
    const [startYear, setStartYear] = React.useState('');
    const [startMonth, setStartMonth] = React.useState('');
    const [endYear, setEndYear] = React.useState('');
    const [endMonth, setEndMonth] = React.useState('');
    // 작업 날짜 파라미터
    const [year, setYear] = React.useState('');
    const [month, setMonth] = React.useState('');
    const [day, setDay] = React.useState('');
    const [hour, setHour] = React.useState('');
    const [minute, setMinute] = React.useState('');
    // 설명 변수
    const [isHide0, setIsHide0] = React.useState(true);
    const [isHide1, setIsHide1] = React.useState(true);
    const [isHide2, setIsHide2] = React.useState(true);
    const [isHide3, setIsHide3] = React.useState(true);
    const [isHide4, setIsHide4] = React.useState(true);
    const [isHide5, setIsHide5] = React.useState(true);

    const registJob = () => {
        if (nickname === '') {
            setAlertMessage("예약 이름을 등록하세요")
            setErrorAlert(true)
            setTimeout(() => setErrorAlert(false), 2000);
            return
        }

        if (runType === '') {
            setAlertMessage("작동 방식을 선택하세요")
            setErrorAlert(true)
            setTimeout(() => setErrorAlert(false), 2000);
            return
        }

        if (jobType === '') {
            setAlertMessage("작업 내용을 선택하세요")
            setErrorAlert(true)
            setTimeout(() => setErrorAlert(false), 2000);
            return
        }

        if (runType === "cron") {
            if (day === "" || hour === "" || minute === "") {
                setAlertMessage("작동 날짜를 선택하세요")
                setErrorAlert(true)
                setTimeout(() => setErrorAlert(false), 2000);
                return
            }
            callCronJobAPI()
        } else if (runType === "date") {
            if (year === "" || month === "" || day === "" || hour === "" || minute === "") {
                setAlertMessage("작동 날짜를 선택하세요")
                setErrorAlert(true)
                setTimeout(() => setErrorAlert(false), 2000);
                return
            }

            if (jobType === "MOLIT") {
                if (startYear === "" || startMonth === "" || endYear === "" || endMonth === "") {
                    setAlertMessage("작업 내용을 선택하세요")
                    setErrorAlert(true)
                    setTimeout(() => setErrorAlert(false), 2000);
                    return
                }
            } else {
                if (startYear === "" || startMonth === "") {
                    setAlertMessage("작업 내용을 선택하세요")
                    setErrorAlert(true)
                    setTimeout(() => setErrorAlert(false), 2000);
                    return
                }
            }
            callDateJobAPI()

        } else {
            setAlertMessage("의도치 못한 버그 - 개발자에게 문의하세요")
            setErrorAlert(true)
            setTimeout(() => setErrorAlert(false), 2000);
            return
        }
    }

    const callDateJobAPI = () => {
        let date = new Date(year, month - 1, day, hour, minute, 0)
        let date_string = moment(date).format("YYYY-MM-DD HH:mm:ss")

        postNoHeader("/api/jobs/date", {
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
            setAlertMessage("작업등록 성공")
            setSuccessAlert(true)
            setTimeout(() => setSuccessAlert(false), 2000);
        }).catch(error => {
            setAlertMessage("작업등록 실패 - 개발자에게 문의하세요")
            setErrorAlert(true)
            setTimeout(() => setErrorAlert(false), 2000);
        })
    }

    const callCronJobAPI = () => {
        postNoHeader("/api/jobs/cron", {
            body: {
                nickname: nickname,
                run_type: jobType,
                cron_day: day,
                cron_hour: hour,
                cron_minute: minute,
            }
        }).then(response => {
            setAlertMessage("작업등록 성공")
            setSuccessAlert(true)
            setTimeout(() => setSuccessAlert(false), 2000);
        }).catch(error => {
            setAlertMessage("작업등록 실패 - 개발자에게 문의하세요")
            setErrorAlert(true)
            setTimeout(() => setErrorAlert(false), 2000);
        })
    }

    return (
        <DashboardBody>
            <Header name="스케줄 등록 (설렉터 깨지면 F5를 누르세요)"></Header>
            <SelectBody>
                <OptionHeader>
                    <OptionTitle>스케줄 작업 이름 작성</OptionTitle>
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
                        label="작업 이름"
                        variant="standard"
                        onChange={(event) => { setNickname(event.target.value) }}
                    />
                </Box>
                <OptionHeader>
                    <OptionTitle>스케줄 작동 방식 선택</OptionTitle>
                    <HelpOutlineIcon
                        style={{ marginLeft: "10px", color: "#6289ED", cursor: "pointer" }}
                        onClick={() => { setIsHide1(!isHide1) }}
                    >
                    </HelpOutlineIcon>
                </OptionHeader>
                {!isHide1 && <ScheduleTypeDescription></ScheduleTypeDescription>}
                <Selecter
                    label="작동 방식"
                    value={runType}
                    valueList={runTypeList}
                    setValue={setRunType}
                    minWidth={200}
                ></Selecter>
                <Divider></Divider>
                <OptionHeader>
                    <OptionTitle>작업 내용 선택</OptionTitle>
                    <HelpOutlineIcon
                        style={{ marginLeft: "10px", color: "#6289ED", cursor: "pointer" }}
                        onClick={() => { setIsHide2(!isHide2) }}
                    >
                    </HelpOutlineIcon>
                </OptionHeader>
                {!isHide2 && <JobTypeDescription></JobTypeDescription>}
                <Selecter
                    label="작업 내용"
                    value={jobType}
                    valueList={jobTypeList}
                    setValue={setJobType}
                    minWidth={300}
                ></Selecter>
                {runType === "date" &&
                    <div>
                        <Divider></Divider>
                        <OptionHeader>
                            <OptionTitle>일회성 스케줄 작업 내용 선택</OptionTitle>
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
                                    label="시작 년도"
                                    value={startYear}
                                    valueList={yearList}
                                    setValue={setStartYear}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {monthList &&
                                <Selecter
                                    label="시작 월"
                                    value={startMonth}
                                    valueList={monthList}
                                    setValue={setStartMonth}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {yearList &&
                                <Selecter
                                    label="종료 년도"
                                    value={endYear}
                                    valueList={yearList}
                                    setValue={setEndYear}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {monthList &&
                                <Selecter
                                    label="종료 월"
                                    value={endMonth}
                                    valueList={monthList}
                                    setValue={setEndMonth}
                                    minWidth={200}
                                ></Selecter>
                            }
                        </SelectContainer>
                        <Divider></Divider>
                        <OptionHeader>
                            <OptionTitle>일회성 스케줄 작동 날짜 선택</OptionTitle>
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
                                    label="작업 년도"
                                    value={year}
                                    valueList={upperYearList}
                                    setValue={setYear}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {monthList &&
                                <Selecter
                                    label="작업 월"
                                    value={month}
                                    valueList={monthList}
                                    setValue={setMonth}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {dayList &&
                                <Selecter
                                    label="작업 일"
                                    value={day}
                                    valueList={dayList}
                                    setValue={setDay}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {hourList &&
                                <Selecter
                                    label="작업 시간"
                                    value={hour}
                                    valueList={hourList}
                                    setValue={setHour}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {minuteList &&
                                <Selecter
                                    label="작업 분"
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
                            <OptionTitle>반복성 스케줄 작동 날짜 선택</OptionTitle>
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
                                    label="작업 일"
                                    value={day}
                                    valueList={dayList}
                                    setValue={setDay}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {hourList &&
                                <Selecter
                                    label="작업 시간"
                                    value={hour}
                                    valueList={hourList}
                                    setValue={setHour}
                                    minWidth={200}
                                ></Selecter>
                            }
                            {minuteList &&
                                <Selecter
                                    label="작업 분"
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
                        작업 등록하기
                    </Button>
                </Box>
            </SelectBody>
        </DashboardBody>
    );
}

export default LoginDashboard;
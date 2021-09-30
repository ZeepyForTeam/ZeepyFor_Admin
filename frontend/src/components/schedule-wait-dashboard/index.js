import styled from 'styled-components';
import React from 'react'
import { get, _delete } from '../../utils/api';
import { redirect } from '../../utils/redirect';
import { getCookie, deleteCookie } from '../../utils/cookie';
import { DataGrid, GridToolbar } from '@mui/x-data-grid';
import Box from '@mui/material/Box';
import CircularProgress from '@mui/material/CircularProgress';
import Header from '../header'
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import DeleteOutlineIcon from '@mui/icons-material/DeleteOutline';
import moment from 'moment'

const DashboardBody = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
`

const ConfigBody = styled.div`
    display: flex;
    flex-direction: row;
    align-items: center;
    width: 100%;
    z-index: 1000;
    margin-top: 10px;
    margin-bottom: 10px;
    justify-content: space-between;
`

const PageBody = styled.div`
    font-family: Noto Sans KR;
    font-weight: bold;
    font-size: 16px;
    margin-left: 5px;
    margin-right: 5px;
    color: #6289ED;
`

const PageContoller = styled.div`
    display: flex;
    justify-content: right;
    flex-direction: row;
    align-items: center;
`

const ScheduleBody = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 80vh;
    transition: all 0.1s ease;
`;

const ScheduleWaitDashboard = ({ setErrorAlert, setSuccessAlert, setAlertMessage, }) => {
    const [page, setPage] = React.useState(1)
    const [totalElement, setTotalElement] = React.useState(null)
    const [totalPage, setTotalPage] = React.useState(null)
    const [jobList, setJobList] = React.useState(null)
    const [selectJob, setSelectJob] = React.useState(null)
    const [currentBuildingList, setCurrentBuildingList] = React.useState(null)

    const getJobList = () => {
        get(`/api/jobs`, { headers: { Authorization: "Bearer " + getCookie("token") } })
            .then(response => {
                let jobs = []
                for (let job of response.data) {
                    job.next_run_time = moment.unix(job.next_run_time).format('YYYY-MM-DD HH:mm:ss')
                    job.job_first_add_time = moment(job.job_first_add_time).format('YYYY-MM-DD HH:mm:ss')
                    jobs.push(job)
                }
                setJobList(jobs)
                setCurrentBuildingList(jobs)
                // setTotalPage(response.data.totalPage)
                // setTotalElement(response.data.total)
            }).catch(error => {
                if (error.response.status === 422 || error.response.status === 401) {
                    deleteCookie("token", "")
                    redirect("/login");
                } else {
                    setAlertMessage("의도치 못한 버그 - 개발자에게 문의하세요")
                    setErrorAlert(true)
                    setTimeout(() => setErrorAlert(false), 2000);
                }
            })

    }

    const deleteJob = () => {
        if (selectJob === null) {
            setAlertMessage("삭제할 스케줄을 선택해주세요")
            setErrorAlert(true)
            setTimeout(() => setErrorAlert(false), 2000);
            return
        }
        _delete(`/api/jobs?_id=${selectJob.id}`, { headers: { Authorization: "Bearer " + getCookie("token") } })
            .then(response => {
                let jobs = []
                for (let job of jobList) {
                    if (job._id === selectJob.id) continue
                    jobs.push(job)
                }
                setJobList(jobs)
                setCurrentBuildingList(jobs)
                setSelectJob(null)
                setAlertMessage("작업삭제 성공")
                setSuccessAlert(true)
                setTimeout(() => setSuccessAlert(false), 2000);
            }).catch(error => {
                if (error.response.status === 422 || error.response.status === 401) {
                    deleteCookie("token", "")
                    redirect("/login");
                } else {
                    setAlertMessage("작업삭제 실패 - 개발자에게 문의하세요")
                    setErrorAlert(true)
                    setTimeout(() => setErrorAlert(false), 2000);
                }
            })
    }

    const columns = [
        { field: '_id', headerName: 'ID', width: 70, hide: true },
        { field: 'nickname', headerName: '별칭', width: 200 },
        { field: 'job_first_add_time', headerName: '스케줄 삽입 시간', width: 200 },
        { field: 'run_type', headerName: '실행 작업', width: 200 },
        { field: 'job_type', headerName: '작업 방식', width: 200 },
        { field: 'next_run_time', headerName: '실행 예측 시간', width: 200 },
    ];

    React.useEffect(() => {
        getJobList()
    }, [])

    React.useEffect(() => {
        setJobList(null)
        setCurrentBuildingList(null)
        getJobList()
    }, [page])

    const clickToNextPage = () => {
        setPage(page + 1)
    }

    const clickToBeforePage = () => {
        setPage(page - 1)
    }

    const onKeyPressToChangePage = (event) => {
        if (event.key !== 'Enter') return
        let eventPage = event.target.value
        if (eventPage === "") return
        eventPage = Number(eventPage)
        if (eventPage < 1) return
        if (eventPage > totalPage) return
        setPage(eventPage)
    }

    return (
        <DashboardBody>
            <Header name="스케줄 대기 저장소"></Header>
            {/* <ConfigBody>
                {totalElement && totalPage && <PageBody>
                    전체: {totalElement} | 전체 페이지 {totalPage} | 현재 페이지 {page}
                </PageBody>}
                <PageContoller>
                    {page > 1 && <Box sx={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'center' }}>
                        <Button
                            sx={{ height: '50px', fontFamily: 'Noto Sans KR', fontWeight: 'bold', color: '#6289ED !important' }}
                            startIcon={<ChevronLeftIcon />}
                            onClick={clickToBeforePage}
                        >
                        </Button>
                    </Box>}
                    <TextField
                        sx={{ width: '100px' }}
                        id="outlined-number"
                        label="page"
                        type="number"
                        InputLabelProps={{
                            shrink: true,
                        }}
                        onKeyPress={onKeyPressToChangePage}
                    />
                    {page < totalPage && <Box sx={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'center' }}>
                        <Button
                            sx={{ height: '50px', fontFamily: 'Noto Sans KR', fontWeight: 'bold', color: '#6289ED !important' }}
                            startIcon={<ChevronRightIcon />}
                            onClick={clickToNextPage}
                        >
                        </Button>
                    </Box>}
                </PageContoller>
            </ConfigBody> */}
            <ScheduleBody>
                <Box
                    sx={{
                        top: 0,
                        left: 0,
                        bottom: 0,
                        right: 0,
                        position: 'absolute',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                    }}
                >
                    {!jobList && <CircularProgress size={100} thickness={8} color="primary" />}
                </Box>
                {jobList && <DataGrid
                    getRowId={(row) => row._id}
                    rows={jobList}
                    columns={columns}
                    pageSize={50}
                    rowsPerPageOptions={[100]}
                    components={{
                        Toolbar: GridToolbar,
                    }}
                    onCellClick={(params, event) => {
                        setSelectJob(params)
                    }}
                />}
            </ScheduleBody>
            <Box
                sx={
                    {
                        display: 'flex',
                        alignItems: 'flex-end',
                        justifyContent: 'right',
                        marginRight: '20px',
                        paddingTop: '30px',
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
                    startIcon={<DeleteOutlineIcon />}
                    variant="contained"
                    onClick={deleteJob}
                >
                    선택한 작업 삭제하기
                </Button>
            </Box>
        </DashboardBody>
    );
}

export default ScheduleWaitDashboard;
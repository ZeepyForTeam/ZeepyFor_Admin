import styled from 'styled-components';
import React from 'react'
import { get } from '../../utils/api';
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

const BuildingBody = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 80vh;
    transition: all 0.1s ease;
`;

const BuildingDashboard = ({ setErrorAlert, setSuccessAlert, setAlertMessage, }) => {
    const [page, setPage] = React.useState(1)
    const [totalElement, setTotalElement] = React.useState(null)
    const [totalPage, setTotalPage] = React.useState(null)
    const [buildingList, setBuildingList] = React.useState(null)
    const [currentBuildingList, setCurrentBuildingList] = React.useState(null)

    const getBuildingList = () => {
        get(`/api/buildings?page=${page}`, { headers: { Authorization: "Bearer " + getCookie("token") } })
            .then(response => {
                let buildings = []
                for (let building of response.data.body) {
                    building.id = building._id
                    if (building.build_year === null) building.build_year = 0
                    if (building.sigungu === null) building.sigungu = ""
                    if (building.latitude === null) building.latitude = 0.0
                    if (building.longitude === null) building.longitude = 0.0
                    buildings.push(building)
                }
                setBuildingList(buildings)
                setCurrentBuildingList(buildings)
                setTotalPage(response.data.totalPage)
                setTotalElement(response.data.total)
            }).catch(error => {
                if (error.response.status === 422 || error.response.status === 401) {
                    deleteCookie("token", "")
                    redirect("/login");
                } else {
                    setAlertMessage("????????? ?????? ?????? - ??????????????? ???????????????")
                    setErrorAlert(true)
                    setTimeout(() => setErrorAlert(false), 2000);
                }
            })

    }

    const columns = [
        { field: '_id', headerName: 'ID', width: 70, hide: true },
        { field: 'build_year', headerName: '?????? ??????', width: 130, editable: true },
        { field: 'deal_year', headerName: '?????? ??????', width: 130, editable: true },
        { field: 'deal_month', headerName: '?????? ???', width: 130, editable: true },
        { field: 'deal_day', headerName: '?????? ???', width: 130, editable: true },
        { field: 'deposit', headerName: '?????????', width: 130, editable: true },
        { field: 'monthly_rent', headerName: '??????', width: 130, editable: true },
        { field: 'using_area', headerName: '??????', width: 130, editable: true },
        { field: 'full_address', headerName: '?????????', width: 130, editable: true },
        { field: 'short_address', headerName: '?????????', width: 130, editable: true },
        { field: 'full_number_address', headerName: '????????????(L)', width: 130, editable: true },
        { field: 'short_number_address', headerName: '????????????(S)', width: 130, editable: true },
        { field: 'dong', headerName: '???', width: 130, editable: true },
        { field: 'jibun', headerName: '??????', width: 130, editable: true },
        { field: 'apartment', headerName: '?????????', width: 130, editable: true },
        { field: 'floor', headerName: '???', width: 90, editable: true },
        { field: 'latitude', headerName: '??????', width: 130, editable: true },
        { field: 'longitude', headerName: '??????', width: 130, editable: true },
        { field: 'type', headerName: '??????', width: 130, editable: true },
        { field: 'area_code', headerName: '??????', width: 110, editable: true },
    ];

    React.useEffect(() => {
        getBuildingList()
    }, [])

    React.useEffect(() => {
        setBuildingList(null)
        setCurrentBuildingList(null)
        getBuildingList()
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
            <Header name="?????? ????????? ?????????"></Header>
            <ConfigBody>
                {totalElement && totalPage && <PageBody>
                    ??????: {totalElement} | ?????? ????????? {totalPage} | ?????? ????????? {page}
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
            </ConfigBody>
            <BuildingBody>
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
                    {!buildingList && <CircularProgress size={100} thickness={8} color="primary" />}
                </Box>
                {currentBuildingList && <DataGrid
                    rows={currentBuildingList}
                    columns={columns}
                    pageSize={50}
                    rowsPerPageOptions={[100]}
                    checkboxSelection
                    components={{
                        Toolbar: GridToolbar,
                    }}
                />}
            </BuildingBody>
        </DashboardBody>
    );
}

export default BuildingDashboard;
export const runTypeList = [
    {
        value: "cron",
        name: "반복성 작업"
    },
    {
        value: "date",
        name: "일회성 작업"
    },
]

export const jobTypeList = [
    {
        value: "MOLIT",
        name: "부동산 데이터 추출"
    },
    {
        value: "KAKAO",
        name: "카카오 주소 API 호출"
    },
    {
        value: "ZEEPY_BATCH_BUILDING",
        name: "지피 대용량 서버 부동산 정보 삽입"
    },
    {
        value: "ZEEPY_BUILDING",
        name: "지피 단발 서버 부동산 정보 삽입"
    },
]

export const returnUpperYearList = () => {
    let currentYear = new Date().getFullYear();
    let start = currentYear
    let end = currentYear + 15
    let result = []
    for (let year = start; year < end; year++) {
        result.push(
            {
                value: year,
                name: `${year}년`,
            }
        )
    }
    return result
}

export const returnYearList = () => {
    let currentYear = new Date().getFullYear();
    let start = currentYear - 15
    let end = currentYear + 15
    let result = []
    for (let year = start; year < end; year++) {
        result.push(
            {
                value: year,
                name: `${year}년`,
            }
        )
    }
    return result
}

export const returnMonthList = () => {
    let result = []
    for (let month = 1; month < 13; month++) {
        result.push(
            {
                value: month,
                name: `${month}월`,
            }
        )
    }
    return result
}

export const returnDayList = () => {
    let result = []
    for (let day = 1; day < 31; day++) {
        result.push(
            {
                value: day,
                name: `${day}일`,
            }
        )
    }
    return result
}

export const returnHourList = () => {
    let result = []
    for (let hour = 0; hour < 24; hour++) {
        result.push(
            {
                value: hour,
                name: `${hour}시`,
            }
        )
    }
    return result
}

export const returnMinuteList = () => {
    let result = []
    for (let minute = 0; minute < 60; minute++) {
        result.push(
            {
                value: minute,
                name: `${minute}분`,
            }
        )
    }
    return result
}
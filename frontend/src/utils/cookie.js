export const getCookie = (name) => {
    var value = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return value ? value[2] : null;
};

export const setCookie = (name, value, day) => {
    var expire = new Date();
    expire.setDate(expire.getDate() + day);
    let cookies = name + '=' + value + '; path=/ ';
    cookies += ';expires=' + expire.toUTCString() + ';';
    document.cookie = cookies;
}

export const deleteCookie = (name, value) => {
    var expire = new Date();
    expire.setDate(expire.getDate() - 1);
    let cookies = name + '=' + value + '; path=/ ';
    cookies += ';expires=' + expire.toUTCString() + ';';
    document.cookie = cookies;
}

export const validate = (name) => {
    var value = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    if (value === null) return false
    else return true
};
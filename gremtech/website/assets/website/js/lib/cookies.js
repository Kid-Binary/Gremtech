"use strict";

class Cookies{

    constructor(){

    }

    set(cookie){
        if(!cookie.name && !cookie.value) return;

        let name = cookie.name +"="+ escape(cookie.value) +";";
        let maxAge = "max-age="+ this._getMaxAge(cookie.expires) +";";
        let path = "path="+ (cookie.path ? cookie.path : "/") + ";";
        let domain = "domain="+ (cookie.domain ? cookie.domain : "") + ";";
        let secure = cookie.secure ? "secure;" : "";

        document.cookie = name + maxAge + path + domain + secure;
    }

    get(name){
        if(!document.cookie.length) return;
        let regExp = new RegExp("(?:^"+ name +"|\\;\\s*"+ name +")=(.*?)(?:\\;|$)", "gi");
        let match = regExp.exec(document.cookie);

        return match ? match[1] : null;
    }

    remove(name){
        if(!this.get(name)) return;
        document.cookie = name +"=;expires="+ this._getMaxAge(-1) +";";
    }

    _getMaxAge(expireDate){;
        expireDate = expireDate || 1;
        let date = new Date();

        date.setTime(date.getTime() + (parseInt(expireDate) * 24 * 60 * 60 * 1000));

        return date.toUTCString();
    }

}

export default new Cookies();

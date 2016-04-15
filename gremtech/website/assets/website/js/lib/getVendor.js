"use strict";

function getVendor(property){
    let style = document.createElement("div").style;
    let prefixes = ["ms", "O", "Moz", "Webkit"];

    if(style[property] === "") return property;
    property = property.charAt(0).toUpperCase() + property.slice(1);

    for(let prefix of prefixes){
        if(style[prefix + property] === "") return (prefix + property);
    }
}

export default getVendor;
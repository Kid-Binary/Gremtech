"use strict";

import "jquery";
import isMobile from "./lib/isMobile";
import Loader from "./lib/loader";
import setProgressPercents from "./lib/setProgressPercents";
import Scrollify from "./lib/scrollify";
import ScrollAppearance from "./lib/scrollAppearance";

new Loader();

$(() => {

    new Scrollify();
    new ScrollAppearance();
    
    setProgressPercents();
});
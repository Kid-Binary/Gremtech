"use strict";

import "jquery";
import "jquery-validation";
import "jquery-mask-plugin";

import Loader from "./lib/loader";
import InvestmentController from "./controllers/investmentController";

new Loader();

$(() => {

    new InvestmentController();
    $("form").validate({ignore: ""});
});
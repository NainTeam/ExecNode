var sys = require('sys')
var exec = require('child_process').exec;
/*
 * GET home page.
 */
import express = require('express');

export function index(req: express.Request, res: express.Response) {    
    exec("whoami", (error, stdout, stderr) => res.send('Loggued as:'+ stdout));
};

export function execute(req: express.Request, res: express.Response) {
    console.log(req.body);
    exec(req.body.exec, (error, stdout, stderr) => res.send('Command:\n\t' + stdout));
};
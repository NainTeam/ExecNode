var sys = require('sys');
var exec = require('child_process').exec;
function index(req, res) {
    exec("whoami", function (error, stdout, stderr) { return res.send('Loggued as:' + stdout); });
}
exports.index = index;
;
function execute(req, res) {
    console.log(req.body);
    exec(req.body.exec, function (error, stdout, stderr) { return res.send('Command:\n\t' + stdout); });
}
exports.execute = execute;
;
//# sourceMappingURL=exec.js.map
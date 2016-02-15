

var path = require("path");

module.exports = function(opts) {
    
    return function(input) {
        var messages = input.messages;
        var num = 0;
        if (!messages || !messages.length) return undefined;

        var output = "\n";

        messages.forEach(function(w) {
            num ++;
            output += messageToString(w) + "\n";
        });

        return output + "\n" + "---------- total " + num + " errors ----------" + "\n";

        function messageToString(message) {
            var str = "";
            var match;
            if (message.node && message.node.source && message.node.source.start) {
                str += message.line + ":" +
                       message.column + "  ";
            }
            else if( (match = /( line) (\d+)/g.exec(message.text)) && match.length > 1 ) {

                str += "" + match[2] + ":1  ";
            }

            str += message.text;
            return str;
        }
    };
};

const packageJson = require('./../package.json');

module.exports = function (ai) {

    ai.addModule({
        id: packageJson.name,
        commands: []
            .concat(require('./wake-up')(ai))
    });
};

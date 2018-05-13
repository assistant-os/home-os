const ns = require('natural-script');
const later = require('later');
const randomstring = require("randomstring");

const snoozeTimeout = 30 * 1000;

function WakeUpDate (ai) {

    this.ai = ai;
    this.id = 'wake-up';


    this.timeouts = {};

    this.valid = function (user, message, words) {
        return ns.parse(message, 'wake me up {{date:date}}');
    };

    this.do = function (user, message, words, result) {
        // console.log(result.occurrence.laterjs);
        // var occurrences = later.schedule(result.occurrence.laterjs).next(3);
        // console.log(occurrences);

        // console.log('ok');
        let date = result.date.start.date();
        // console.log(date);

        let now = new Date();
        // console.log(now);

        let diff = date - now;

        let delay = ai.os.helpers.humanReadable.delay(diff);

        this.ai.say(user, 'Ok I will wake you up in '+delay+'!');

        let id = randomstring.generate();

        let timeout = setTimeout(() => {
            this.ai.say(user, 'Wake up!');

            let snoozeInterval = setInterval( () => {
                this.ai.say(user, 'Wake up!');
            }, snoozeTimeout);
        }, diff);


        
    };
}

function WakeUp (ai, os) {

    this.ai = ai;
    this.os = os;
    this.id = 'wake-up';

    this.valid = function (user, message, words) {
        return ns.parse(message, 'wake me up {{occurrence:occurrence}}');
    };

    this.do = function (user, message, words, result) {
        // console.log(result.occurrence.laterjs);
        // var occurrences = later.schedule(result.occurrence.laterjs).next(3);
        // console.log(occurrences);
        // this.ai.say(user, 'ok let\'s go '+occurrences.join(', '));
        this.ai.say(user, 'Ok I will wake you up!');

        later.setInterval(() =>  {
            this.ai.say(user, 'Wake up!');
        }, result.occurrence.laterjs);

    };
}

module.exports = function (ai, os) {
    return [
        new WakeUpDate(ai, os),
        new WakeUp(ai, os)
    ];
};

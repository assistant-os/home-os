const dataset = require("../datasets/kinetics-700-2020/train.json");

const activites = Object.values(dataset).map(
  (video) => video.annotations.label
);

let uniqueActivities = [...new Set(activites)];

Object.values(uniqueActivities).forEach((activity) => {
  console.log(activity);
});

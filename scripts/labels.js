const fs = require('fs')
const dataset = require('../models/kinetics700_2020/train.json')

const labels = Array.from(
  new Set(Object.values(dataset).map(v => v.annotations.label))
)

fs.writeFile('classes.txt', labels.join('\n'), () => {
  console.log('done')
})

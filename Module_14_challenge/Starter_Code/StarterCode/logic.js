// setup the URL to read in the JSON data 
let baseURL =  'https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json';

// read in the sampls.json file 
d3.json(baseURL).then(function(data) {
    console.log(data);
  });
  

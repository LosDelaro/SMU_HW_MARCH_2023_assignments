// setup the URL to read in the JSON data 
let link =  'https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json';

// perform a get request 
d3.json(link).then(function (data){
    console.log(data);
    makeDropdown(data);
    makeMetadata(data, data.names[0]);
    makeBarChart(data, data.names[0]);
});

function optionChanged(val) {
    d3.json(link).then(function (data) {
      console.log(data);
  makeMetadata(data, val);
      makeBarChart(data, val);
    });
  }
  function makeDropdown(data) {
    for (let i = 0; i < data.names.length; i++){
      let name = data.names[i];
      d3.select("#selDataset").append("option").text(name);
    }
  }
  function makeMetadata(data, val) {
    console.log(val);
  // nuke parent
    d3.select("#sample-metadata").html("");
  let meta = data.metadata.filter(x => x.id == val)[0];
    let keys = Object.keys(meta);
    for (let i = 0; i < keys.length; i++){
      let key = keys[i];
      d3.select("#sample-metadata").append("p").text(`${key}: ${meta[key]}`);
    }
  }
  function makeBarChart(data, val) {
    let sample = data.samples.filter(x => x.id == val)[0];
  // Slice the first 10 objects for plotting
    let sample_values = sample.sample_values.slice(0, 10);
    let otu_labels = sample.otu_labels.slice(0, 10);
    let otu_ids = sample.otu_ids.slice(0, 10);
  // Reverse the array to accommodate Plotly's defaults
    sample_values.reverse();
    otu_labels.reverse();
    otu_ids.reverse();
    
  // Trace for the Greek Data
    let trace1 = {
      x: sample_values,
      y: otu_ids.map(x => `OTU: ${x}`),
      hovertext: otu_labels,
      type: 'bar',
      orientation: "h",
      marker: {color: 'blue'}
    };
  // Data array
    let plotly_data = [trace1];
  // Apply a title to the layout
    let layout = {
      "title": `Bacteria for ID: ${val}`,
      "xaxis": {'title': "Number of Bacteria Found"}
    }
  // Render the plot to the div tag with id "plot"
    Plotly.newPlot("bar", plotly_data, layout);
  }
  
  

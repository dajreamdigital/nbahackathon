

// building the skills radar chart using chartjs
var skillsData = {
	labels : ["January","February","March","April","May","June"],
	datasets : [
		{
			fillColor : "rgba(172,194,132,0.4)",
			strokeColor : "#ACC26D",
			pointColor : "#fff",
			pointStrokeColor : "#9DB86D",
			data : [203,156,99,251,305,247]
		},
    {
			fillColor : "rgba(132,194,255,0.4)",
			strokeColor : "#ACC26D",
			pointColor : "#fff",
			pointStrokeColor : "#9DB86D",
			data : [100,10,20,123,200,300]
		},
	]
};

var context = document.getElementById('skills').getContext('2d');
var skillsChart = new Chart(context).Radar(skillsData);

var skillsChart = new Chart(context, {
    type: 'radar',
    data: skillsData,
    // options: options
});

// building the twitter bar chart using chartjs
var tweetData = {
	labels : ["Team Avg. Twitter Activity","Player Twitter Activity"],
	datasets : [
		{
      fillColor : "rgba(73,188,170,0.4)",
			strokeColor : "rgba(72,174,209,0.4)",
			data : [456, 123]
		},
	]
};


var ctx = document.getElementById('tweets').getContext('2d');
var skillsChart = new Chart(ctx).Bar(tweetData);



// building the skills radar chart using chartjs

console.log(data);

var skillsData = {
	labels : ["Holding Ball","Passes Made","Distance Run","Ball Touches","Turnovers"],
	datasets : [
		{
			fillColor : "rgba(172,194,132,0.4)",
			strokeColor : "#ACC26D",
			pointColor : "#fff",
			pointStrokeColor : "#9DB86D",
			data : [data.player.ballhold,data.player.pass,data.player.run,data.player.touch,data.player.turnover]
		},
    {
			fillColor : "rgba(132,194,255,0.4)",
			strokeColor : "#ACC26D",
			pointColor : "#fff",
			pointStrokeColor : "#9DB86D",
			data : [data.average.ballhold,data.average.pass,data.average.run,data.average.touch,data.average.turnover]
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
			data : [10, data.count]
		},
	]
};


var ctx = document.getElementById('tweets').getContext('2d');
var skillsChart = new Chart(ctx).Bar(tweetData);

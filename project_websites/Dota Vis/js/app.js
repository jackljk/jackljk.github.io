// function finalproject() {
//   var hero_stats = "hero_stats.json";
//   var proPlayers = "proPlayers.json";
//   scatterplot(hero_stats);
//   barChart(hero_stats);
//   lollipopChart(hero_stats);
//   geomap(proPlayers);
//   nodelink(hero_stats);
// }

function scatter() {
  var hero_stats = "data/hero_stats.json";
  scatterplot(hero_stats);
}

function bar() {
  var hero_stats = "data/hero_stats.json";
  barChart(hero_stats);
}

function lolli() {
  var hero_stats = "data/hero_stats.json";
  lollipopChart(hero_stats);
}

function geo() {
  var proPlayers = "data/proPlayers.json";
  geomap(proPlayers);
}

function nodelinkgraph() {
  var hero_stats = "data/hero_stats.json";
  nodelink(hero_stats);
}

var scatterplot = function (hero_stats) {
  d3.json(hero_stats).then(function (data) {
    // For each hero, add up the total number of picks and wins
    for (var i = 0; i < data.length; i++) {
      data[i]["total_pick"] =
        +data[i]["1_pick"] +
        +data[i]["2_pick"] +
        +data[i]["3_pick"] +
        +data[i]["4_pick"] +
        +data[i]["5_pick"] +
        +data[i]["6_pick"] +
        +data[i]["7_pick"] +
        +data[i]["8_pick"];
      data[i]["total_win"] =
        +data[i]["1_win"] +
        +data[i]["2_win"] +
        +data[i]["3_win"] +
        +data[i]["4_win"] +
        +data[i]["5_win"] +
        +data[i]["6_win"] +
        +data[i]["7_win"] +
        +data[i]["8_win"];
    }

    // Get win percentage by dividing total_win by total_pick
    for (var i = 0; i < data.length; i++) {
      data[i]["win_percentage"] = data[i]["total_win"] / data[i]["total_pick"];
    }
    // ------------------ Scatterplot ------------------
    var HEIGHT = 800;
    var WIDTH = 1000;
    var PADDING = 100;

    var svg = d3
      .select("#scatterplot")
      .append("svg")
      .attr("width", WIDTH)
      .attr("height", HEIGHT);

    // ------------------ Scales ------------------
    var xScale = d3
      .scaleLinear()
      .domain([0, d3.max(data, (d) => d.total_pick)])
      .range([PADDING, WIDTH - PADDING]);

    var yScale = d3
      .scaleLinear()
      .domain([0, d3.max(data, (d) => d.total_win)])
      .range([HEIGHT - PADDING, PADDING]);

    // ------------------ Axes ------------------
    var xAxis = svg
      .append("g")
      .attr("transform", "translate(0," + (HEIGHT - PADDING) + ")");

    var yAxis = svg
      .append("g")
      .attr("transform", "translate(" + PADDING + ",0)");

    // ------------------ Title and Axis Titles ------------------
    svg
      .append("text")
      .attr("x", WIDTH / 2)
      .attr("y", PADDING / 2)
      .attr("text-anchor", "middle")
      .attr("font-size", "20px")
      .text("Total Picks vs Total Wins");

    svg
      .append("text")
      .attr("x", WIDTH / 2)
      .attr("y", HEIGHT - PADDING / 2)
      .attr("text-anchor", "middle")
      .attr("font-size", "16px")
      .text("Total Picks");

    svg
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("x", -HEIGHT / 2)
      .attr("y", PADDING / 2)
      .attr("text-anchor", "middle")
      .attr("font-size", "16px")
      .text("Total Wins");
    // ------------------ Clip ------------------
    var clip = svg
      .append("defs")
      .append("svg:clipPath")
      .attr("id", "clip")
      .append("svg:rect")
      .attr("width", WIDTH - PADDING - PADDING)
      .attr("height", HEIGHT - PADDING)
      .attr("x", PADDING)
      .attr("y", 0);

    var scatter = svg.append("g").attr("clip-path", "url(#clip)");

    // ------------------ Tooltip ------------------
    var Tooltip = d3
      .select("#scatterplot")
      .append("div")
      .attr("class", "tooltip-scatter")
      .style("opacity", 0);

    var mouseover = function (d) {
      Tooltip.style("opacity", 1);
      d3.select(this).style("stroke", "none").style("opacity", 0.8);
    };

    var mousemove = function (event, d) {
      console.log(d);
      const imgUrlStart = "https://cdn.dota2.com/";
      var img_url = imgUrlStart + d.img;

      var att_url = "assets\\attributes\\" + d.primary_attr + ".png";
      Tooltip.html(
        `
        <img class="image1" src="` +
          img_url +
          `">
        <img class="image2" src="` +
          att_url +
          `">
        <ul>
          <li>Base Strength: ` +
          d.base_str +
          `</li>
          <li>Base Agility: ` +
          d.base_agi +
          `</li>
          <li>Base Intelligence: ` +
          d.base_int +
          `</li>
          <li>No. Picks: ` +
          d.total_pick +
          `</li>
          <li>Win Rate: ` +
          d.total_win +
          `</li>
        </ul>`
      )
        .style("left", event.pageX + 70 + "px")
        .style("top", event.pageY + "px");
    };

    var mouseleave = function (d) {
      Tooltip.style("opacity", 0);
      d3.select(this).style("stroke", "black").style("opacity", 1);
    };

    // ------------------ Zoom ------------------
    var zoom = d3
      .zoom()
      .scaleExtent([0.001, 20]) // This control how much you can unzoom (x0.5) and zoom (x20)
      .extent([
        [0, 0],
        [WIDTH, HEIGHT],
      ])
      .on("zoom", updateChart);

    svg
      .append("rect")
      .attr("width", WIDTH)
      .attr("height", HEIGHT)
      .style("fill", "none")
      .style("pointer-events", "all")
      .attr("transform", "translate(" + PADDING + "," + PADDING + ")")
      .lower()
      .call(zoom);

    function updateChart(event) {
      // new scale
      var newX = event.transform.rescaleX(xScale);
      var newY = event.transform.rescaleY(yScale);

      // update axes
      xAxis.call(d3.axisBottom(newX));
      yAxis.call(d3.axisLeft(newY));

      // update circle
      scatter
        .selectAll("image")
        .attr("x", (d) => newX(d.total_pick) - 15)
        .attr("y", (d) => newY(d.total_win) - 15);


      // update tooltip
      Tooltip.style("left", d3.pointer(this)[0] + 70 + "px").style(
        "top",
        d3.pointer(this)[1] + "px"
      );
    }

    // ------------------ Points ------------------
    scatter
      .selectAll("image")
      .data(data)
      .enter()
      .append("image")
      .attr("xlink:href", function (d) {
        const imgUrlStart = "https://cdn.dota2.com/";
        var link= imgUrlStart + d.icon;
        return link;
      })
      .attr("x", function (d) {
        return xScale(d.total_pick) - 15;
      })
      .attr("y", function (d) {
        return yScale(d.total_win) - 15;
      })
      .attr("width", 30)
      .attr("height", 30)
      .on("mouseover", mouseover)
      .on("mousemove", mousemove)
      .on("mouseleave", mouseleave);

    function update() {
      scatter
        .selectAll("circle")
        .transition()
        .duration(2000)
        .attr("r", (d) => 10);
      xAxis.transition().duration(2000).call(d3.axisBottom(xScale));

      yAxis.transition().duration(2000).call(d3.axisLeft(yScale));
    }

    update();
  });
};

var barChart = function (hero_stats) {
  var is30 = false;
  d3.json(hero_stats).then(function (data) {
    // ------------------ Data - level 1 ------------------
    var data_lvl1 = data.map((d) => {
      return {
        id: d.id,
        str: d.base_str,
        agi: d.base_agi,
        int: d.base_int,
        name: d.localized_name,
        img: d.img,
        primary_attr: d.primary_attr,
        sum_stats: d.base_str + d.base_agi + d.base_int,
        lvl: 1,
      };
    });

    // ------------------ Data - level 30 ------------------
    var data_lvl30 = data.map((d) => {
      return {
        id: d.id,
        str: d.str_gain + d.str_gain * 30,
        agi: d.agi_gain + d.agi_gain * 30,
        int: d.int_gain + d.int_gain * 30,
        name: d.localized_name,
        img: d.img,
        primary_attr: d.primary_attr,
        sum_stats:
          d.str_gain +
          d.str_gain * 30 +
          d.agi_gain +
          d.agi_gain * 30 +
          d.int_gain +
          d.int_gain * 30,
        lvl: 30,
      };
    });

    // ------------------ Stack ------------------
    var stack = d3.stack().keys(["str", "agi", "int"]);
    var series_lvl1 = stack(data_lvl1);
    var series_lvl30 = stack(data_lvl30);
    // ------------------ SVG ------------------
    const WIDTH = 800;
    const HEIGHT = 31 * data_lvl1.length;
    const PADDING = 100;

    const svg = d3
      .select("#barChart")
      .append("svg")
      .attr("width", WIDTH)
      .attr("height", HEIGHT)
      .style("font", "14px Montserrat");

    svg
      .append("rect")
      .attr("class", "background")
      .attr("width", "100%")
      .attr("height", "100%")
      .style("fill", "#F5F5F2");

    // ------------------ Scales lvl1 ------------------
    var scaleY_lvl1 = d3
      .scaleOrdinal()
      .domain(data_lvl1.map((d) => d.name))
      .range(d3.range(0, (data_lvl1.length + 1) * 30, 30));
    var scaleX_lvl1 = d3
      .scaleLinear()
      .domain([
        0,
        d3.max(series_lvl1, (d) =>
          d3.max(d, (d) => d.data.str + d.data.agi + d.data.int)
        ),
      ])
      .range([0, WIDTH - PADDING * 2.5]);
    var color = d3
      .scaleOrdinal()
      .domain(["str", "agi", "int"])
      .range(["#ED5B67", "#32a852", "#00cec9"]);

    // ------------------ Scales lvl30 ------------------
    var scaleY_lvl30 = d3
      .scaleOrdinal()
      .domain(data_lvl30.map((d) => d.name))
      .range(d3.range(0, (data_lvl30.length + 1) * 30, 30));
    var scaleX_lvl30 = d3
      .scaleLinear()
      .domain([
        0,
        d3.max(series_lvl30, (d) =>
          d3.max(d, (d) => d.data.str + d.data.agi + d.data.int)
        ),
      ])
      .range([0, WIDTH - PADDING * 2.5]);

    // ------------------ Tooltip ------------------
    var div = d3
      .select("body")
      .append("div")
      .attr("class", "tooltip-bar")
      .style("opacity", 0)
      .style("position", "absolute");

    var shadow = svg
      .append("rect")
      .attr("class", "shadow")
      .attr("position", "absolute")
      .attr("fill", "lightgrey");
    // ------------------ hbars ------------------
    var hbars = svg
      .selectAll("g.hbar")
      .data(series_lvl1)
      .enter()
      .append("g")
      .attr("class", "hbar")
      .attr("fill", (d) => color(d.key))
      .attr("transform", "translate(" + PADDING + "," + PADDING + ")");

    hbars
      .selectAll("rect")
      .data((d) => d)
      .enter()
      .append("rect")
      .attr("x", (d) => scaleX_lvl1(d[0]))
      .attr("y", (d) => scaleY_lvl1(d.data.name) - 10)
      .attr("width", (d) => scaleX_lvl1(d[1]) - scaleX_lvl1(d[0]))
      .attr("height", 20)
      .on("mouseover", function (event, d) {
        var xPos = +d3.select(this).attr("x");
        var yPos = +d3.select(this).attr("y");
        var wid = +d3.select(this).attr("width");
        var hei = +d3.select(this).attr("height");
        d3.select(this)
          .transition("start")
          .duration(300)
          .attr("opacity", ".90")
          .attr("x", xPos - 5)
          .attr("y", yPos - 5)
          .attr("stroke", "lightgrey")
          .attr("stroke-width", "0.5px");

        shadow
          .transition()
          .duration(10)
          .attr("opacity", "0.5")
          .attr("x", xPos)
          .attr("y", yPos)
          .attr("width", wid)
          .attr("height", hei)
          .attr("transform", "translate(" + PADDING + "," + PADDING + ")");

        div.transition().duration("200").style("opacity", 1);
      })
      .on("mousemove", function (event, d) {
        var curr_att_rgb = d3.select(this).style("fill");
        const imgUrlStart = "https://cdn.dota2.com/";
        var img_url = imgUrlStart + d.data.img;

        var att_url = "assets\\attributes\\" + d.data.primary_attr + ".png";
        // round the values to 2 decimal places
        var total_stats_val = Math.round(d.data.sum_stats * 100) / 100;

        var total_stats = `Total Stats: ${total_stats_val}`;
        let curr_stat = "";
        if (curr_att_rgb == "rgb(22, 139, 152)") {
          curr_stat = `Agility: ${d.data.agi}`;
        } else if (curr_att_rgb == "rgb(237, 91, 103)") {
          curr_stat = `Intelligence: ${d.data.int}`;
        } else if (curr_att_rgb == "rgb(89, 111, 126)") {
          curr_stat = `Strength: ${d.data.str}`;
        }

        let html =
          `<div class="tooltip-bar">
                      <img src=` +
          img_url +
          ` alt="Hero Image" />
                      <div class="bar-bottom">
                        <div class="image">
                          <img src=` +
          att_url +
          ` alt="Small image description" />
                        </div>
                        <div class="bar-text">
                          <ul>
                              <li>` +
          total_stats +
          `</li>
                              <li>` +
          curr_stat +
          `</li>
                            </ul>
                        </div>
                  </div>`;

        div
          .html(html)
          .style("left", event.pageX + 10 + "px")
          .style("top", event.pageY - 25 + "px");
      })
      .on("mouseout", function (event, d) {
        if (d.data.lvl == 1) {
          d3.select(this)
            .transition("start")
            .duration(300)
            .attr("opacity", "1")
            .attr("x", scaleX_lvl1(d[0]))
            .attr("width", scaleX_lvl1(d[1]) - scaleX_lvl1(d[0]))
            .attr("y", scaleY_lvl1(d.data.name) - 10)
            .attr("height", 20)
            .attr("stroke", "none");
        } else {
          d3.select(this)
            .transition("start")
            .duration(300)
            .attr("opacity", "1")
            .attr("x", scaleX_lvl30(d[0]))
            .attr("width", scaleX_lvl30(d[1]) - scaleX_lvl30(d[0]))
            .attr("y", scaleY_lvl30(d.data.name) - 10)
            .attr("height", 20)
            .attr("stroke", "none");
        }

        div.transition().duration("200").style("opacity", 0);

        div.style("left", "-1000px").style("top", "-1000px");

        shadow.transition().duration(300).attr("opacity", "0");
      });

    // ------------------ Axis ------------------
    var xAxis = d3.axisTop(scaleX_lvl1);
    var yAxis = d3.axisLeft(scaleY_lvl1);

    svg
      .append("g")
      .attr("class", "axisx")
      .attr("transform", "translate(" + PADDING + "," + (PADDING - 10.5) + ")")
      .call(xAxis);

    svg
      .append("g")
      .attr("class", "axisy")
      .attr("transform", "translate(" + PADDING + "," + PADDING + ")")
      .call(yAxis);

    // ------------------ Legend ------------------
    const legendPadding = 50;

    var legend = svg
      .selectAll(".legend")
      .data(color.domain())
      .enter()
      .append("g")
      .attr("class", "legend")
      .attr("transform", function (d, i) {
        return "translate(0," + i * 28 + ")";
      });

    legend
      .append("rect")
      .attr("x", WIDTH - legendPadding)
      .attr("y", legendPadding * 3)
      .attr("width", 24)
      .attr("height", 24)
      .style("fill", color)
      .attr("stroke", "black");

    legend
      .append("text")
      .attr("x", WIDTH - legendPadding * 2.5)
      .attr("y", legendPadding * 3 + 10)
      .attr("dy", ".35em")
      .style("text-anchor", "start")
      .text(function (d) {
        if (d == "str") return "Strength";
        if (d == "agi") return "Agility";
        if (d == "int") return "Intelligence";
      });

    // ------------------ Title ------------------
    svg
      .append("text")
      .attr("x", WIDTH / 2)
      .attr("y", 0 + PADDING / 4)
      .attr("text-anchor", "middle")
      .style("font-size", "16px")
      .style("text-decoration", "underline")
      .text("Hero Stats");

    // ------------------ Button controls ------------------
    var button_30 = d3.select("button.lvl30").on("click", function () {
      is30 = true;
      var dropdown = d3.select(".primary-attribute");
      var currentOption = dropdown.property("value");
      sort_attr(currentOption);
    });

    var button_1 = d3.select("button.lvl1").on("click", function () {
      is30 = false;

      var dropdown = d3.select(".primary-attribute");
      var currentOption = dropdown.property("value");
      sort_attr(currentOption);
    });

    d3.select(".primary-attribute").on("change", function () {
      var selectedOption = d3.select(this).property("value");
      // do something with the selected option
      if (selectedOption == "str") {
        sort_attr("str");
      }
      if (selectedOption == "agi") {
        sort_attr("agi");
      }
      if (selectedOption == "int") {
        sort_attr("int");
      }
      if (selectedOption == "nameasc") {
        sort_attr("nameasc");
      }
      if (selectedOption == "namedesc") {
        sort_attr("namedesc");
      }
      if (selectedOption == "idasc") {
        sort_attr("idasc");
      }
      if (selectedOption == "iddesc") {
        sort_attr("iddesc");
      }
      if (selectedOption == "sumStatsAsc") {
        sort_attr("sumStatsAsc");
      }
      if (selectedOption == "sumStatsDesc") {
        sort_attr("sumStatsDesc");
      }
    });
    var sort_attr = function (sortBy) {
      if (is30) {
        data_attr = data_lvl30;
        series = series_lvl30;
      } else {
        data_attr = data_lvl1;
        series = series_lvl1;
      }

      if (sortBy == "str") {
        data_attr = data_attr.sort((a, b) => b.str - a.str);
      }
      if (sortBy == "agi") {
        data_attr = data_attr.sort((a, b) => b.agi - a.agi);
      }
      if (sortBy == "int") {
        data_attr = data_attr.sort((a, b) => b.int - a.int);
      }
      if (sortBy == "nameasc") {
        data_attr = data_attr.sort((a, b) => a.name.localeCompare(b.name));
      }
      if (sortBy == "namedesc") {
        data_attr = data_attr.sort((a, b) => b.name.localeCompare(a.name));
      }
      if (sortBy == "idasc") {
        data_attr = data_attr.sort((a, b) => a.id - b.id);
      }
      if (sortBy == "iddesc") {
        data_attr = data_attr.sort((a, b) => b.id - a.id);
      }
      if (sortBy == "sumStatsAsc") {
        data_attr = data_attr.sort(
          (a, b) => a.str + a.agi + a.int - (b.str + b.agi + b.int)
        );
      }
      if (sortBy == "sumStatsDesc") {
        data_attr = data_attr.sort(
          (a, b) => b.str + b.agi + b.int - (a.str + a.agi + a.int)
        );
      }

      var scaleY = d3
        .scaleOrdinal()
        .domain(data_attr.map((d) => d.name))
        .range(d3.range(0, (data_attr.length + 1) * 30, 30));

      var scaleX = d3
        .scaleLinear()
        .domain([
          0,
          d3.max(series, (d) =>
            d3.max(d, (d) => d.data.str + d.data.agi + d.data.int)
          ),
        ])
        .range([0, WIDTH - PADDING * 2.5]);

      var hbars = svg
        .selectAll("g.hbar")
        .data(series)
        .attr("fill", (d) => color(d.key))
        .attr("transform", "translate(" + PADDING + "," + PADDING + ")");
      hbars
        .selectAll("rect")
        .data((d) => d)
        .transition()
        .duration(1000)
        .attr("x", (d) => scaleX(d[0]))
        .attr("y", (d) => scaleY(d.data.name) - 10)
        .attr("width", (d) => scaleX(d[1]) - scaleX(d[0]))
        .attr("height", 20);

      hbars.selectAll("rect").on("mouseout", function (event, d) {
        if (d.data.lvl == 1) {
          d3.select(this)
            .transition("start")
            .duration(300)
            .attr("opacity", "1")
            .attr("x", scaleX_lvl1(d[0]))
            .attr("width", scaleX_lvl1(d[1]) - scaleX_lvl1(d[0]))
            .attr("y", scaleY(d.data.name) - 10)
            .attr("height", 20)
            .attr("stroke", "none");
        } else {
          d3.select(this)
            .transition("start")
            .duration(300)
            .attr("opacity", "1")
            .attr("x", scaleX_lvl30(d[0]))
            .attr("width", scaleX_lvl30(d[1]) - scaleX_lvl30(d[0]))
            .attr("y", scaleY(d.data.name) - 10)
            .attr("height", 20)
            .attr("stroke", "none");
        }

        div.transition().duration("200").style("opacity", 0);

        div.style("left", "-1000px").style("top", "-1000px");

        shadow.transition().duration(300).attr("opacity", "0");
      });

      xAxis_new = d3.axisTop(scaleX);
      yAxis_new = d3.axisLeft(scaleY);

      svg.select("g.axisy").transition().duration(1000).call(yAxis_new);
      svg.select("g.axisx").transition().duration(1000).call(xAxis_new);
    };
  });
};

var lollipopChart = function (hero_stats) {
  var currentHero = "Anti-Mage";
  d3.json(hero_stats).then(function (data) {
    const imgUrlStart = "https://cdn.dota2.com";
    data_by_rank = d3.rollup(
      data,
      (v) => {
        return {
          name: v[0].localized_name,
          img: v[0].img,
          icon: v[0].icon,
          attribute: v[0].primary_attr,
          herald: v[0]["1_win"] / v[0]["1_pick"],
          herald_win: v[0]["1_win"],
          herald_pick: v[0]["1_pick"],
          guardian: v[0]["2_win"] / v[0]["2_pick"],
          guardian_win: v[0]["2_win"],
          guardian_pick: v[0]["2_pick"],
          crusader: v[0]["3_win"] / v[0]["3_pick"],
          crusader_win: v[0]["3_win"],
          crusader_pick: v[0]["3_pick"],
          archon: v[0]["4_win"] / v[0]["4_pick"],
          archon_win: v[0]["4_win"],
          archon_pick: v[0]["4_pick"],
          legend: v[0]["5_win"] / v[0]["5_pick"],
          legend_win: v[0]["5_win"],
          legend_pick: v[0]["5_pick"],
          ancient: v[0]["6_win"] / v[0]["6_pick"],
          ancient_win: v[0]["6_win"],
          ancient_pick: v[0]["6_pick"],
          divine: v[0]["7_win"] / v[0]["7_pick"],
          divine_win: v[0]["7_win"],
          divine_pick: v[0]["7_pick"],
          immortal: v[0]["8_win"] / v[0]["8_pick"],
          immortal_win: v[0]["8_win"],
          immortal_pick: v[0]["8_pick"],
          pro: v[0]["pro_win"] / v[0]["pro_pick"],
          pro_win: v[0]["pro_win"],
          pro_pick: v[0]["pro_pick"],
          turbo: v[0]["turbo_wins"] / v[0]["turbo_picks"],
          turbo_win: v[0]["turbo_wins"],
          turbo_pick: v[0]["turbo_picks"],
        };
      },
      (d) => d.localized_name
    );
    // ------------------ SVG ------------------
    const WIDTH = 1000;
    const HEIGHT = 600;
    const MARGIN = { TOP: 80, BOTTOM: 80, LEFT: 100, RIGHT: 10 };

    var svg = d3
      .select("#lollipopChart")
      .append("svg")
      .attr("width", WIDTH)
      .attr("height", HEIGHT);

    // ------------------ VARIABLES ------------------
    var keys = [
      "herald",
      "guardian",
      "crusader",
      "archon",
      "legend",
      "ancient",
      "divine",
      "immortal",
      "pro",
      "turbo",
    ];

    // ------------------ HELPER FUNC ------------------
    var get_one_hero = function (data, name) {
      var hero = data.get(name);
      // return the key and values of the hero
      return keys.map(function (key) {
        return { key: key, value: hero[key] };
      });
    };

    // ------------------ SCALES ------------------
    var xScale = d3
      .scaleLinear()
      .domain([0, 1])
      .range([MARGIN.LEFT, WIDTH - MARGIN.RIGHT]);

    var yScale = d3
      .scaleBand()
      .domain(keys)
      .range([MARGIN.TOP, HEIGHT - MARGIN.BOTTOM])
      .padding(0.1);

    var color = d3.scaleOrdinal().domain(keys).range(d3.schemeSet2);

    // ------------------ AXES ------------------
    var xAxis = d3.axisBottom(xScale);
    var yAxis = d3.axisLeft(yScale);

    var gxaxis = svg
      .append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + (HEIGHT - MARGIN.BOTTOM) + ")")
      .call(xAxis);

    var gyaxis = svg
      .append("g")
      .attr("class", "y axis")
      .attr("transform", "translate(" + MARGIN.LEFT + ",0)")
      .call(yAxis);

    gyaxis
      .selectAll(".tick")
      .append("image")
      .attr("xlink:href", function (d) {
        return "assets\\rank\\" + d + ".png";
      })
      .attr("x", -30)
      .attr("y", 10)
      .attr("width", 20)
      .attr("height", 20);

    // ------------------ LINES ------------------
    var temp = get_one_hero(data_by_rank, "Anti-Mage");
    svg
      .selectAll("line")
      .data(get_one_hero(data_by_rank, "Anti-Mage"), (d) => d.key)
      .enter()
      .append("line")
      .attr("x1", MARGIN.LEFT)
      .attr("y1", (d) => yScale(d.key) + yScale.bandwidth() / 2)
      .attr("x2", MARGIN.LEFT)
      .attr("y2", (d) => yScale(d.key) + yScale.bandwidth() / 2)
      .transition()
      .duration(1000)
      .attr("x2", (d) => xScale(d.value))
      .attr("y2", (d) => yScale(d.key) + yScale.bandwidth() / 2)
      .attr("stroke", (d) => color(d.key))
      .attr("stroke-width", 2);

    // ------------------ TOOLTIP ------------------
    var tooltip = d3
      .select("body")
      .append("div")
      .attr("class", "tooltip-lollipop")
      .style("position", "absolute")
      .style("opacity", 0);

    // ------------------ CIRCLES ------------------
    var circles = svg
      .selectAll("circle")
      .data(get_one_hero(data_by_rank, "Anti-Mage"), (d) => d.key)
      .enter()
      .append("circle")
      .attr("cx", MARGIN.LEFT)
      .attr("cy", (d) => yScale(d.key) + yScale.bandwidth() / 2)
      .transition()
      .duration(1000)
      .attr("cx", (d) => xScale(d.value))
      .attr("cy", (d) => yScale(d.key) + yScale.bandwidth() / 2)
      .attr("r", 8)
      .attr("fill", (d) => color(d.key))
      .attr("stroke", "black")
      .attr("stroke-width", 0.5);

    d3.selectAll("circle")
      .on("mouseover", function (event, d) {
        var rank = d.key;
        tooltip.transition().duration(200).style("opacity", 1);
        tooltip
          .html(
            "Win Rate: " +
              d.value.toFixed(4) +
              "<br/>" +
              "No. Games: " +
              data_by_rank.get(currentHero)[rank + "_pick"]
          )
          .style("left", event.pageX + 20 + "px")
          .style("top", event.pageY - 28 + "px");
      })
      .on("mouseout", function (d) {
        tooltip.transition().duration(500).style("opacity", 0);
      });

    // ------------------ TITLE ------------------
    svg
      .append("g")
      .attr("id", "title-lollipop")
      .append("text")
      .attr("x", WIDTH / 2)
      .attr("y", MARGIN.TOP / 2)
      .attr("text-anchor", "middle")
      .attr("font-size", "24px")
      .attr("font-weight", "bold")
      .text("Win Rate by Skill Bracket for Anti-Mage");

    d3.select("#title-lollipop")
      .append("image")
      .attr("class", "title-img")
      .attr("xlink:href", imgUrlStart + data_by_rank.get(currentHero).img)
      .attr("x", WIDTH - 27 * MARGIN.RIGHT)
      .attr("y", MARGIN.TOP / 2 - 60)
      .attr("width", 100)
      .attr("height", 100);

    // ------------------ AXIS TITLES ------------------
    svg
      .append("text")
      .attr("x", WIDTH / 2)
      .attr("y", HEIGHT - MARGIN.BOTTOM / 2)
      .attr("text-anchor", "middle")
      .attr("font-size", "16px")
      .attr("font-weight", "bold")
      .text("Win Rate");

    svg
      .append("text")
      .attr("x", -HEIGHT / 2)
      .attr("y", MARGIN.LEFT / 2)
      .attr("text-anchor", "middle")
      .attr("font-size", "16px")
      .attr("font-weight", "bold")
      .attr("transform", "rotate(-90)")
      .text("Skill Bracket");

    // ------------------ MENU ------------------
    var menu = d3
      .select("#lollipopChart")
      .append("div")
      .attr("id", "menu-lollipop")
      .style("opacity", 0)
      .style("left", "-1000px")
      .style("top", "-1000px");

    d3.select("#menu-lollipop")
      .selectAll("option")
      .data(data_by_rank)
      .enter()
      .append("option")
      .attr("value", (d) => d[0])
      .style("background-image", function (d) {
        return "url(" + (imgUrlStart + d[1].img) + ")";
      })
      .text((d) => d[0])
      .on("click", function (event, d) {
        // Update Graph
        svg
          .selectAll("line")
          .data(get_one_hero(data_by_rank, d[0]), (d) => d.key)
          .transition()
          .duration(1000)
          .attr("x2", (d) => xScale(d.value))
          .attr("y2", (d) => yScale(d.key) + yScale.bandwidth() / 2)
          .attr("stroke", (d) => color(d.key))
          .attr("stroke-width", 2);

        svg
          .selectAll("circle")
          .data(get_one_hero(data_by_rank, d[0]), (d) => d.key)
          .transition()
          .duration(1000)
          .attr("cx", (d) => xScale(d.value))
          .attr("cy", (d) => yScale(d.key) + yScale.bandwidth() / 2)
          .attr("r", 8)
          .attr("fill", (d) => color(d.key))
          .attr("stroke", "black")
          .attr("stroke-width", 0.5);

        // Update Title
        d3.select("#title-lollipop")
          .select("text")
          .transition()
          .duration(500)
          .text("Win Rate by Skill Bracket for " + d[0]);

        // Update Title Image
        d3.select("#title-lollipop")
          .select("image")
          .transition()
          .duration(500)
          .attr("xlink:href", imgUrlStart + d[1].img);

        // Update Current Hero
        currentHero = d[0];

        // Remove Menu
        menu.transition().duration(500).style("opacity", 0);

        setTimeout(() => {
          menu.style("left", "-10000px").style("top", "-10000px");
        }, 500);
      })
      .on("mouseover", function (event, d) {
        d3.select(this)
          .style("color", "azure")
          .style("border-color", "azure")
          .style("border-width", "2px")
          .style("border-style", "solid");
      })
      .on("mouseout", function (event, d) {
        d3.select(this)
          .style("color", "white")
          .style("border-color", "black")
          .style("border-width", "2px")
          .style("border-style", "solid");
      });

    // ------------------ BUTTON TO OPEN MENU ------------------
    var button = svg
      .append("g")
      .attr("id", "menu-lollipop-button")
      .append("rect")
      .attr("x", WIDTH - WIDTH / 4 - 20)
      .attr("y", 75)
      .attr("width", 100)
      .attr("height", 50)
      .style("fill", "azure")
      .style("stroke", "black")
      .style("stroke-width", 2)
      .style("cursor", "pointer")
      .attr("rx", 10)
      .attr("ry", 10)
      .on("click", function (event, d) {
        d3.select("#menu-lollipop")
          .transition()
          .duration(500)
          .style("opacity", 1);

        menu
          .style("left", event.pageX - 500 + "px")
          .style("top", event.pageY + "px");
      })
      .on("mouseover", function (event, d) {
        d3.select(this).style("fill", "white").style("stroke", "black");
      })
      .on("mouseout", function (event, d) {
        d3.select(this).style("fill", "azure").style("stroke", "black");
      });

    svg
      .select("#menu-lollipop-button")
      .append("text")
      .attr("x", WIDTH - WIDTH / 4 + 30)
      .attr("y", 105)
      .attr("text-anchor", "middle")
      .attr("font-size", "20px")
      .attr("font-weight", "bold")
      .text("Menu");
  });
};

var geomap = function (proPlayers) {
  d3.json(proPlayers).then(function (data) {
    // ------------------ VAR FOR 2-3ALPHA ------------------
    const alpha3ToAlpha2 = {
      AFG: "AF",
      ALA: "AX",
      ALB: "AL",
      DZA: "DZ",
      ASM: "AS",
      AND: "AD",
      AGO: "AO",
      AIA: "AI",
      ATA: "AQ",
      ATG: "AG",
      ARG: "AR",
      ARM: "AM",
      ABW: "AW",
      AUS: "AU",
      AUT: "AT",
      AZE: "AZ",
      BHS: "BS",
      BHR: "BH",
      BGD: "BD",
      BRB: "BB",
      BLR: "BY",
      BEL: "BE",
      BLZ: "BZ",
      BEN: "BJ",
      BMU: "BM",
      BTN: "BT",
      BOL: "BO",
      BES: "BQ",
      BIH: "BA",
      BWA: "BW",
      BVT: "BV",
      BRA: "BR",
      IOT: "IO",
      UMI: "UM",
      VGB: "VG",
      VIR: "VI",
      BRN: "BN",
      BGR: "BG",
      BFA: "BF",
      BDI: "BI",
      KHM: "KH",
      CMR: "CM",
      CAN: "CA",
      CPV: "CV",
      CYM: "KY",
      CAF: "CF",
      TCD: "TD",
      CHL: "CL",
      CHN: "CN",
      CXR: "CX",
      CCK: "CC",
      COL: "CO",
      COM: "KM",
      COG: "CG",
      COD: "CD",
      COK: "CK",
      CRI: "CR",
      HRV: "HR",
      CUB: "CU",
      CUW: "CW",
      CYP: "CY",
      CZE: "CZ",
      DNK: "DK",
      DJI: "DJ",
      DMA: "DM",
      DOM: "DO",
      ECU: "EC",
      EGY: "EG",
      SLV: "SV",
      GNQ: "GQ",
      ERI: "ER",
      EST: "EE",
      ETH: "ET",
      FLK: "FK",
      FRO: "FO",
      FJI: "FJ",
      FIN: "FI",
      FRA: "FR",
      GUF: "GF",
      PYF: "PF",
      ATF: "TF",
      GAB: "GA",
      GMB: "GM",
      GEO: "GE",
      DEU: "DE",
      GHA: "GH",
      GIB: "GI",
      GRC: "GR",
      GRL: "GL",
      GRD: "GD",
      GLP: "GP",
      GUM: "GU",
      GTM: "GT",
      GGY: "GG",
      GIN: "GN",
      GNB: "GW",
      GUY: "GY",
      HTI: "HT",
      HMD: "HM",
      VAT: "VA",
      HND: "HN",
      HKG: "HK",
      HUN: "HU",
      ISL: "IS",
      IND: "IN",
      IDN: "ID",
      IRN: "IR",
      IRQ: "IQ",
      IRL: "IE",
      IMN: "IM",
      ISR: "IL",
      ITA: "IT",
      CIV: "CI",
      JAM: "JM",
      JPN: "JP",
      JEY: "JE",
      JOR: "JO",
      KAZ: "KZ",
      OSA: "XK",
      KEN: "KE",
      KIR: "KI",
      KWT: "KW",
      KGZ: "KG",
      LAO: "LA",
      LVA: "LV",
      LBN: "LB",
      LSO: "LS",
      LBR: "LR",
      LBY: "LY",
      LIE: "LI",
      LTU: "LT",
      LUX: "LU",
      MAC: "MO",
      MKD: "MK",
      MDG: "MG",
      MWI: "MW",
      MYS: "MY",
      MDV: "MV",
      MLI: "ML",
      MLT: "MT",
      MHL: "MH",
      MTQ: "MQ",
      MRT: "MR",
      MUS: "MU",
      MYT: "YT",
      MEX: "MX",
      FSM: "FM",
      MDA: "MD",
      MCO: "MC",
      MNG: "MN",
      MNE: "ME",
      MSR: "MS",
      MAR: "MA",
      MOZ: "MZ",
      MMR: "MM",
      NAM: "NA",
      NRU: "NR",
      NPL: "NP",
      NLD: "NL",
      NCL: "NC",
      NZL: "NZ",
      NIC: "NI",
      NER: "NE",
      NGA: "NG",
      NIU: "NU",
      NFK: "NF",
      PRK: "KP",
      MNP: "MP",
      NOR: "NO",
      OMN: "OM",
      PAK: "PK",
      PLW: "PW",
      PSE: "PS",
      PAN: "PA",
      PNG: "PG",
      PRY: "PY",
      PER: "PE",
      PHL: "PH",
      PCN: "PN",
      POL: "PL",
      PRT: "PT",
      PRI: "PR",
      QAT: "QA",
      REU: "RE",
      ROU: "RO",
      RUS: "RU",
      RWA: "RW",
      SHN: "SH",
      KNA: "KN",
      LCA: "LC",
      MAF: "MF",
      SPM: "PM",
      VCT: "VC",
      WSM: "WS",
      SMR: "SM",
      STP: "ST",
      SAU: "SA",
      SEN: "SN",
      SRB: "RS",
      SYC: "SC",
      SLE: "SL",
      SGP: "SG",
      SXM: "SX",
      SVK: "SK",
      SVN: "SI",
      SLB: "SB",
      SOM: "SO",
      ZAF: "ZA",
      SGS: "GS",
      SSD: "SS",
      ESP: "ES",
      LKA: "LK",
      SDN: "SD",
      SUR: "SR",
      SJM: "SJ",
      SWZ: "SZ",
      SWE: "SE",
      CHE: "CH",
      SYR: "SY",
      TWN: "TW",
      TJK: "TJ",
      TZA: "TZ",
      THA: "TH",
      TLS: "TL",
      TGO: "TG",
      TKL: "TK",
      TON: "TO",
      TTO: "TT",
      TUN: "TN",
      TUR: "TR",
      TKM: "TM",
      TCA: "TC",
      TUV: "TV",
      UGA: "UG",
      UKR: "UA",
      ARE: "AE",
      GBR: "GB",
      USA: "US",
      UMI: "UM",
      URY: "UY",
      UZB: "UZ",
      VUT: "VU",
      VEN: "VE",
      VNM: "VN",
      VGB: "VG",
      VIR: "VI",
      WLF: "WF",
      ESH: "EH",
      YEM: "YE",
      ZMB: "ZM",
      ZWE: "ZW",
      ALA: "AX",
      KOR: "KR",
      BES: "BQ",
      CUW: "CW",
      GGY: "GG",
      IMN: "IM",
      JEY: "JE",
      MNE: "ME",
      SRB: "RS",
      ABV: "NG",
      SDS: "NG",
    };
    // ------------------ DATA ------------------
    var data_by_country = d3.rollup(
      data,
      (v) => {
        return {
          count: v.length,
          name: v.map((d) => d.name),
          personaName: v.map((d) => d.personaname),
          avatar: v.map((d) => d.avatarfull),
          team_name: v.map((d) => d.team_name),
          profileurl: v.map((d) => d.profileurl),
        };
      },
      (d) => d.loccountrycode
    );

    // drop the entries with no country code
    data_by_country.delete(null);

    // ------------------ DEFINE SVG ------------------
    var WIDTH = 1000;
    var HEIGHT = 500;
    var MARGIN = { TOP: 10, BOTTOM: 10, LEFT: 10, RIGHT: 10 };

    var svg = d3
      .select("#geomap")
      .append("svg")
      .attr("width", WIDTH)
      .attr("height", HEIGHT);

    // ------------------ DEFINE TOOLTIP ------------------
    var tooltip = d3
      .select(".geomap-tooltip")
      .style("opacity", 0)
      .style("left", "-1000px")
      .style("top", "-1000px");

    // ------------------ DEFINE SCALE ------------------
    var color = d3
      .scaleSequential(d3.interpolateBlues)
      .domain([0, d3.max(data_by_country, (d) => d[1].count)]);

    // ------------------ DEFINE MAP ------------------
    var projection = d3
      .geoEquirectangular()
      .scale(150)
      .translate([WIDTH / 2, HEIGHT / 2]);

    var path = d3.geoPath().projection(projection);

    // ------------------ JSON FOR COUNTRY CODES ------------------

    d3.json("assets/world.json").then(function (world) {
      // ------------------ ZOOM ------------------
      var zoom = d3.zoom().scaleExtent([1, 8]).on("zoom", zoomed);

      svg.call(zoom);

      function zoomed(event) {
        svg.selectAll("path").attr("transform", event.transform);
      }

      // ------------------ DRAW MAP ------------------
      console.log(world.features);
      console.log(path);
      svg
        .selectAll("path")
        .data(world.features)
        .enter()
        .append("path")
        .attr("d", path)
        .attr("fill", (d) => {
          if (
            alpha3ToAlpha2[d.id] == null ||
            data_by_country.get(alpha3ToAlpha2[d.id]) == null
          ) {
            return "white";
          } else {
            return color(data_by_country.get(alpha3ToAlpha2[d.id]).count);
          }
        })
        .attr("stroke", "black")
        .attr("stroke-width", 0.5)
        .style("pointer-events", "all")
        .on("mouseover", function (event, d) {
          tooltip.style("opacity", 1);

          if (
            alpha3ToAlpha2[d.id] == null ||
            data_by_country.get(alpha3ToAlpha2[d.id]) == null
          ) {
            tooltip
              .select(".geomap-tooltip-title")
              .html(`<p> IGN: No Data</p>`);

            tooltip
              .select(".geomap-tooltip-image1")
              .html(
                `<img src = \"` +
                  "https://via.placeholder.com/150x150.png?text=Placeholder+Image" +
                  `\"></img>`
              );

            tooltip.select(".geomap-tooltip-image2").html(`<span></span>`);

            tooltip.select(".geomap-tooltip-text").html(`<p>No Data</p>`);
          }

          var random = Math.floor(
            Math.random() * data_by_country.get(alpha3ToAlpha2[d.id]).count
          );
          var alpha2 = alpha3ToAlpha2[d.id];

          tooltip
            .select(".geomap-tooltip-title")
            .html(
              `<p> IGN: ` +
                data_by_country.get(alpha2).personaName[random] +
                `</p>`
            );

          tooltip
            .select(".geomap-tooltip-image1")
            .html(
              `<img src = \"` +
                data_by_country.get(alpha2).avatar[random] +
                `\"></img>`
            );

          tooltip
            .select(".geomap-tooltip-image2")
            .html(`<span class="fi fi-` + alpha2.toLowerCase() + `"></span>`);

          tooltip
            .select(".geomap-tooltip-text")
            .html(
              `<p>` +
                `Real Name: ` +
                data_by_country.get(alpha2).name[random] +
                `<span class="brLarge"></span>` +
                `Team Name: ` +
                data_by_country.get(alpha2).team_name[random] +
                `<span class="brLarge"></span>` +
                `No. Players in Country: ` +
                data_by_country.get(alpha2).count +
                `<span class="brLarge"></span>` +
                "Steam Account: " +
                `<a href=` +
                data_by_country.get(alpha2).profileurl[random] +
                `>` +
                data_by_country.get(alpha2).personaName[random] +
                `</a>` +
                `</p>`
            );
        })
        .on("mousemove", function (event, d) {
          tooltip.transition().duration(200).style("opacity", 1);
          tooltip
            .style("left", event.pageX + 10 + "px")
            .style("top", event.pageY + 10 + "px");
        })
        .on("mouseout", function (event, d) {
          tooltip.transition().duration(200).style("opacity", 0);

          tooltip.style("left", "-1000px").style("top", "-1000px");
        })
        .on("click", function (event, d) {
          if (
            alpha3ToAlpha2[d.id] == null ||
            data_by_country.get(alpha3ToAlpha2[d.id]) == null
          ) {
            return;
          } else {
            var alpha2 = alpha3ToAlpha2[d.id];
            var random = Math.floor(
              Math.random() * data_by_country.get(alpha2).count
            );
            window.open(
              data_by_country.get(alpha2).profileurl[random],
              "_blank"
            );
          }
        });
    });

    // ------------------ DEFINE LEGEND ------------------
    // use color scale and draw rects to represent the legend
    var legend = svg
      .selectAll(".legend")
      .data(color.ticks(10).slice(1).reverse())
      .enter()
      .append("g")
      .attr("class", "legend")
      .attr("transform", function (d, i) {
        return "translate(0," + i * 20 + ")";
      });

    legend
      .append("rect")
      .attr("x", 18)
      .attr("y", HEIGHT / 3)
      .attr("width", 18)
      .attr("height", 18)
      .style("fill", color);

    legend
      .append("text")
      .attr("x", 62)
      .attr("y", HEIGHT / 3 + 9)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function (d) {
        return d;
      });

    // ------------------ TITLE ------------------
    svg
      .append("text")
      .attr("x", WIDTH / 2)
      .attr("y", 20)
      .attr("text-anchor", "middle")
      .style("font-size", "24px")
      .text("Number of Players per Country");
  });
};

var nodelink = function (hero_stats) {
  d3.json(hero_stats).then(function (data) {
    // ------------------ CONSTANT VARIABLES ------------------
    const WIDTH = 1200;
    const HEIGHT = 1400;
    const MARGIN = { TOP: 60, BOTTOM: 60, LEFT: 80, RIGHT: 80 };
    const imgUrlStart = "https://cdn.dota2.com/";
    const QUARTERHEIGHT = HEIGHT / 4 - MARGIN.TOP;

    // ------------------ DATA ------------------
    // Getting the count of each role by extracting all the roles first
    var roles = [];
    data.forEach(function (d) {
      d.roles.forEach(function (role) {
        roles.push(role);
      });
    });

    // count the number of times each role appears
    var role_counts = {};
    roles.forEach(function (x) {
      role_counts[x] = (role_counts[x] || 0) + 1;
    });

    // Prep the roles data to be used in the graph as nodes
    var data_role_nodes = [];
    for (var key in role_counts) {
      data_role_nodes.push({
        id: key,
        group: 2,
        x: 0,
        y: 0,
        count: role_counts[key],
        role_icon: "assets\\roles\\" + key + "-removebg.png",
      });
    }

    // Manually position the roles nodes
    data_role_nodes[0].x = 0 + MARGIN.LEFT * 1.4;
    data_role_nodes[0].y = QUARTERHEIGHT;
    data_role_nodes[1].x = 0 + MARGIN.LEFT * 1.4;
    data_role_nodes[1].y = QUARTERHEIGHT * 2;
    data_role_nodes[2].x = 0 + MARGIN.LEFT * 1.4;
    data_role_nodes[2].y = QUARTERHEIGHT * 3;
    data_role_nodes[3].x = 0 + MARGIN.LEFT * 1.4;
    data_role_nodes[3].y = QUARTERHEIGHT * 4;
    data_role_nodes[4].x = WIDTH - MARGIN.RIGHT * 1.4;
    data_role_nodes[4].y = QUARTERHEIGHT * 1;
    data_role_nodes[5].x = WIDTH - MARGIN.RIGHT * 1.4;
    data_role_nodes[5].y = QUARTERHEIGHT * 2;
    data_role_nodes[6].x = WIDTH - MARGIN.RIGHT * 1.4;
    data_role_nodes[6].y = QUARTERHEIGHT * 3;
    data_role_nodes[7].x = WIDTH - MARGIN.RIGHT * 1.4;
    data_role_nodes[7].y = QUARTERHEIGHT * 4;

    function checkCollision(x, y, nodes) {
      var radius = 30; // or whatever the radius of your nodes is
      for (var i = 0; i < nodes.length; i++) {
        var dx = x - nodes[i].x;
        var dy = y - nodes[i].y;
        var distance = Math.sqrt(dx * dx + dy * dy);
        if (distance < radius * 2) {
          return true; // collision detected
        }
      }
      return false; // no collision detected
    }
    // make a nodes varaible to store the nodes of the graph which will be all the heroes and the nodes
    var nodes = [];
    data.forEach(function (d) {
      var collision = true;
      var x,
        y = 0;
      while (collision) {
        x =
          Math.floor(
            Math.random() * (WIDTH - MARGIN.RIGHT * 3 - MARGIN.LEFT * 3 + 1)
          ) +
          MARGIN.LEFT * 3;
        y =
          Math.floor(
            Math.random() * (HEIGHT - MARGIN.BOTTOM - MARGIN.TOP + 1)
          ) + MARGIN.TOP;

        collision = checkCollision(x, y, nodes);
      }

      d.x = x;
      d.y = y;

      nodes.push({
        id: d.localized_name,
        group: 1,
        icon: d.icon,
        x: d.x,
        y: d.y,
      });
    });

    // make links which will go from each hero to each of their roles
    var links = [];
    data.forEach(function (d) {
      d.roles.forEach(function (role) {
        links.push({
          source: {
            id: d.localized_name,
            group: 1,
            icon: d.icon,
            x: d.x,
            y: d.y,
          },
          target: {
            id: role,
            group: 2,
            count: role_counts[role],
            x: data_role_nodes.find((x) => x.id === role).x,
            y: data_role_nodes.find((x) => x.id === role).y,
          },
          value: 1,
        });
      });
    });
    // ------------------ DEFINE SVG ------------------
    var svg = d3
      .select("#nodelink")
      .append("svg")
      .attr("width", WIDTH)
      .attr("height", HEIGHT);


    // ------------------ TOOLTIP ------------------
    var tooltip = d3
      .select("#nodelink")
      .append("div")
      .attr("class", "nodelink-tooltip")
      .style("opacity", 0)
      .style("position", "absolute")
      .style("background-color", "azure")
      .style("border", "solid")
      .style("border-width", "2px")
      .style("border-radius", "5px")
      .style("padding", "5px");

    // ------------------ SCALE FOR IMAGE SIZE FOR ROLE NODES ------------------
    var scale = d3
      .scaleLinear()
      .domain([
        0,
        d3.max(data_role_nodes, function (d) {
          return d.count;
        }),
      ])
      .range([40, 200]);

    // ------------------ DEFINE LINKS ------------------
    var link = svg
      .append("g")
      .attr("class", "links")
      .selectAll("line")
      .data(links)
      .enter()
      .append("line")
      .attr("stroke-width", 0.5)
      .attr("stroke", "black")
      .style("opacity", 0.2);

    // ------------------ DEFINE NODES HEROES ------------------
    var node_heroes = svg
      .selectAll(".node_heroes")
      .data(nodes)
      .enter()
      .append("g")
      .attr("class", "node_heroes");

    node_heroes
      .append("image")
      .attr("xlink:href", (d) => imgUrlStart + d.icon)
      .attr("width", 40)
      .attr("height", 40)
      .on("mouseover", function (event, d) {
        // show name of hero
        d3.select(this)
          .transition()
          .duration(200)
          .attr("width", 80)
          .attr("height", 80);

        tooltip.transition().duration(200).style("opacity", 0.9);

        tooltip
          .html(d.id)
          .style("left", event.pageX + 28 + "px")
          .style("top", event.pageY - 28 + "px");
      })
      .on("mouseout", function (event, d) {
        // hide name of hero
        d3.select(this)
          .transition()
          .duration(200)
          .attr("width", 40)
          .attr("height", 40);

        tooltip.transition().duration(200).style("opacity", 0);

        tooltip.style("left", "-1000px").style("top", "-1000px");
      });

    // ------------------ DEFINE NODES ROLES ------------------
      var tooltip_role = d3
      .select("#nodelink")
      .append("div")
      .attr("class", "nodelink-tooltip")
      .style("opacity", 0)
      .style("position", "absolute")
      .style("background-color", "azure")
      .style("border", "solid")
      .style("border-width", "2px")
      .style("border-radius", "5px")
      .style("padding", "5px");

    var node_roles = svg
      .selectAll(".node_roles")
      .data(data_role_nodes)
      .enter()
      .append("g")
      .attr("class", "node_roles");

    node_roles
      .append("image")
      .attr("xlink:href", (d) => d.role_icon)
      .attr("width", function (d) {
        return scale(d.count);
      })
      .attr("height", function (d) {
        return scale(d.count);
      })
      .attr("x", function (d) {
        return d.x - scale(d.count) / 2;
      })
      .attr("y", function (d) {
        return d.y - scale(d.count) / 2;
      })
      .on("mouseover", function (event, d) {
        tooltip_role.transition().duration(200).style("opacity", 0.9);

        d3.select(this)
          .transition()
          .duration(200)
          .style('opacity', 0.5)
      })
      .on('mousemove', function (event, d) {
        tooltip_role
          .html("Number of heroes with the role: " + d.count)
          .style("left", event.pageX + 28 + "px")
          .style("top", event.pageY - 28 + "px");
      })
      .on("mouseout", function (event, d) {
        tooltip_role.transition().duration(200).style("opacity", 0);

        d3.select(this)
          .transition()
          .duration(200)
          .style('opacity', 1)
      })
      .lower();

    // ------------------ DEFINE FORCE SIMULATION ------------------
    var simulation = d3
      .forceSimulation();

    // ------------------ SIMULATION ------------------
    simulation.on("tick", function () {
      link
        .attr("x1", function (d) {
          return d.source.x;
        })
        .attr("y1", function (d) {
          return d.source.y;
        })
        .attr("x2", function (d) {
          return d.target.x;
        })
        .attr("y2", function (d) {
          return d.target.y;
        })
        .lower();

      node_heroes
        .attr("transform", function (d) {
          return "translate(" + (d.x - 20) + "," + (d.y - 20) + ")";
        })
        .raise()
        .on("mouseover", function (event, d) {
          // Move node to the center when growing
          d3.select(this)
            .transition()
            .duration(200)
            .attr("transform", function (d) {
              return "translate(" + (d.x - 40) + "," + (d.y - 40) + ")";
            });

          // highlight the links
          link
            .transition()
            .duration(200)
            .style("opacity", function (l) {
              if (l.source.id == d.id) {
                return 1;
              } else {
                return 0.2;
              }
            })
            .attr("stroke-width", function (l) {
              if (l.source.id == d.id) {
                return 4; 
              } else {
                return 0.5;
              }
            });
        })
        .on("mouseout", function (event, d) {
          // Move node back to the original position
          d3.select(this)
            .transition()
            .duration(200)
            .attr("transform", function (d) {
              return "translate(" + (d.x - 20) + "," + (d.y - 20) + ")";
            });

          // unhighlight the links
          link
            .transition()
            .duration(200)
            .style("opacity", 0.2)
            .attr("stroke-width", 0.5);
        });

      node_roles
        .on("mouseover", function (event, d) {
          // highlight the links
          link
            .transition()
            .duration(200)
            .style("opacity", function (l) {
              
        console.log(l)
              if (l.target.id == d.id) {
                return 1;
              } else {
                return 0.2;
              }
            })
            .attr("stroke-width", function (l) {
              if (l.target.id == d.id) {
                return 4;
              } else {
                return 0.5;
              }
            });
        })
        .on("mouseout", function (event, d) {
          // unhighlight the links
          link
            .transition()
            .duration(200)
            .style("opacity", 0.2)
            .attr("stroke-width", 0.5);
        }
      );
    });

    // ------------------ TITLE ------------------
    svg
      .append("text")
      .attr("x", WIDTH / 2)
      .attr("y", 20)
      .attr("text-anchor", "middle")
      .style("font-size", "28px")
      .text("Dota 2 Heroes Roles");
  });
};

import React, { useEffect, useState } from "react";
import Chart from "react-apexcharts";
import ReactApexChart from "react-apexcharts";
import demo from "../demo.json";
// import demo from "../new.json";

// const MyCharts = () => {
//   const [averageTemp, setAverageTemp] = useState([]);
//   const [date, setDate] = useState([]);

//   useEffect(() => {
//     const data = demo;
//     setAverageTemp(data?.map((item) => item.cellsize));

//     setDate(data?.map((item) => item.cellName));
//   }, []);

//   const series = [
//     //data on the y-axis
//     {
//       name: "Temperature in Celsius",
//       data: averageTemp,
//     },
//   ];
//   const options = {
//     //data on the x-axis
//     chart: { id: "bar-chart" },
//     xaxis: {
//       categories: date,
//     },
//   };

//   return (
//     <div>
//       <ReactApexChart
//         options={options}
//         series={series}
//         type="treemap"
//         height={350}
//       />
//     </div>
//   );
// };

// export default MyCharts;

const Apexchart = () => {
  const [dataUser, setDataUser] = useState([]);
  useEffect(() => {
    setDataUser(demo);
    // axios
    //   .get("http://localhost:4000/data")
    //   .then((response) seriesData=> {
    //     setDataUser(response.data);
    //   })
    //   .catch((e) => {
    //     alert(e);
    //   });
  }, []);

  const seriesData = [];
  const options = {
    plotOptions: {
      treemap: {
        enableShades: true,
        shadeIntensity: 0.5,
        reverseNegativeShade: true,
        colorScale: {
          ranges: [
            {
              from: 15,
              to: 25,
              color: "#CD363A",
            },
            {
              from: 0,
              to: 15,
              color: "#52B12C",
            },
          ],
        },
      },
    },
  };

  dataUser.map((val) => {
    seriesData.push({
      x: val.cellName, //
      y: val.cellsize, //
    });
  });

  const series = [{ data: seriesData }];
  return (
    <div>
      <Chart options={options} series={series} height={350} type="treemap" />
    </div>
  );
};

export default Apexchart;

// class ApexChart extends React.Component {
//   constructor(props) {
//     super(props);

//     this.state = {
//       series: [
//         {
//           data: [
//             {
//               x: ["a","b","c","d","e"],
//               y: [1,2,3,4,5]
//             }
//           ],
//         },
//       ],
//       options: {
//         legend: {
//           show: false,
//         },
//         chart: {
//           height: 350,
//           type: "treemap",
//         },
//         title: {
//           text: "Basic Treemap",
//         },
//       },
//     };
//   }

//   render() {
//     return (
//       <div id="chart">
//         <ReactApexChart
//           options={this.state.options}
//           series={this.state.series}
//           type="treemap"
//           height={350}
//         />
//       </div>
//     );
//   }
// }

// export default ApexChart

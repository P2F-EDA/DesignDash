// App.js
import React, { useState } from "react";
import "./App.css";

import ApexChart from "./components/Apexchart";

// import MyCharts from './components/Apexchart'

// import Treemap from "./components/Treemap";
// import demo from "./demo.json";
const dataset = {
  children: [
    {
      cellName: 1,
      children : [
        { cellName: "DFFSRHQX2", cellsize: 22.44 },
        { cellName: "DFFSRHQX2", cellsize: 22.44 },
        { cellName: "DFFSRHQX2", cellsize: 22.44 }
      ],
      colname: "level2",
    },
    {
      cellName: 2,
      children : [
        { cellName: "DFFSRHQX1", cellsize: 15.84 },
        { cellName: "DFFSRHQX1", cellsize: 25.84 },
        { cellName: "DFFSRHQX1", cellsize: 15 }
      ],
      colname: "level2",
    },
    {
      cellName: 3,
      children : [
        { cellName: "DFFSRXL", cellsize: 17.16 },
        { cellName: "DFFSRXL", cellsize: 14 },
        { cellName: "DFFSRXL", cellsize: 10.16 }
      ],
      colname: "level2",
    },
  ],
  cellName: "LEF",
};

function App() {
  return (
    <div className="App">
      {/* {childrenset.className} */}
      {/* <Treemap width={600} height={400} data={dataset} /> */}
      <ApexChart />
      {/* <MyCharts /> */}
    </div>
  );
}

export default App;

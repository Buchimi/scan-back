import { SafeAreaView } from "react-native-safe-area-context";
import { Button, SegmentedButtons, Text } from "react-native-paper";
import { BarChart, LineChart, PieChart } from "react-native-chart-kit";
import { Dimensions, StyleSheet, View } from "react-native";

import { useState } from "react";
export default function AnalyticsPage() {
  const data = {
    labels: ["January", "February", "March", "April", "May", "June"],
    datasets: [
      {
        data: [20, 45, 28, 80, 99, 43],
      },
    ],
  };
  const width = (Dimensions.get("window").width * 9) / 10;
  function barGraphData(data) {
    return {
      labels: data["labels"],
      dataset: data["datasets"],
    };
  }

  function pieChartData(data: {
    labels: string[];
    datasets: {
      data: number[];
    }[];
  }) {
    return data.labels.map((label) => {
      const index = data.labels.indexOf(label);
      const red = Math.random() * 255;
      const green = Math.random() * 255;
      const blue = Math.random() * 255;

      return {
        name: label,
        data: data.datasets[0].data[index],
        color: `rgb(${red}, ${green}, ${blue})`,
        legendFontColor: "#7F7F7F",
        legendFontSize: 15,
      };
    });
  }

  // type chartType = "bar" | "line" | "pie";
  const [track, setTrack] = useState("savings");
  const [chart, setChart] = useState("bar");

  const config = {
    backgroundColor: "#e26a00",
    backgroundGradientFrom: "#fb8c00",
    backgroundGradientTo: "#ffa726",
    decimalPlaces: 2, // optional, defaults to 2dp
    color: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
    labelColor: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
    style: {
      borderRadius: 16,
    },
    propsForDots: {
      r: "6",
      strokeWidth: "2",
      stroke: "#ffa726",
    },
  };

  return (
    <View
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        top: "30%",
      }}
    >
      {chart == "bar" && (
        <BarChart
          data={data}
          height={300}
          width={width}
          yAxisLabel="$"
          yAxisSuffix=""
          chartConfig={config}
          style={styles.graph}
        />
      )}
      {chart == "line" && (
        <LineChart
          data={data}
          height={300}
          width={width}
          style={styles.graph}
          chartConfig={config}
          yAxisLabel="$"
        />
      )}
      {chart == "pie" && (
        <PieChart
          data={pieChartData(data)}
          width={width}
          height={300}
          chartConfig={config}
          accessor="data"
          backgroundColor={"transparent"}
          paddingLeft={"30"}
          // center={[0, 0]}
          // absolute

          style={styles.graph}
        />
      )}
      <SegmentedButtons
        style={styles.segButtons}
        value={track}
        onValueChange={setTrack}
        buttons={[
          { value: "savings", label: "Savings" },
          { value: "expenditure", label: "Expenditure" },
        ]}
      />

      <SegmentedButtons
        style={styles.segButtons}
        value={chart}
        onValueChange={setChart}
        buttons={[
          {
            value: "bar",
            label: "Bar Graph",
          },
          {
            value: "pie",
            label: "Pie chart",
          },
          { value: "line", label: "line" },
        ]}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  graph: {
    paddingHorizontal: "5%",
    marginTop: "2%",
    // paddingLeft: 20,
  },
  row: {
    paddingVertical: 5,
    display: "flex",
    flexDirection: "row",
    alignContent: "space-between",
    justifyContent: "space-around",
  },
  segButtons: {
    margin: 10,
  },
});

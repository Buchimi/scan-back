import { useState } from "react";
import { BottomNavigation } from "react-native-paper";
import CameraPage from "src/pages/Camerapage";
import { SafeAreaProvider } from "react-native-safe-area-context";
import AnalyticsPage from "src/pages/Analytics";
import axios from "axios";
import { getUploadURI } from "@/provider/serverprovider";

const CameraRoute = () => (
  <CameraPage
    onPictureTaken={(base64) => {
      axios({
        url: getUploadURI(),
        data: {
          upload_image: base64,
        },
        method: "post",
      });
    }}
  />
);
const DataRoute = () => <AnalyticsPage />;

export default function App() {
  const [index, setIndex] = useState(0);

  const [routes] = useState([
    {
      key: "Snap",
      title: "Camera",
      focusedIcon: "camera",
      unfocusedIcon: "camera-outline",
    },
    {
      key: "Data",
      title: "Analytics",
      focusedIcon: "graph",
    },
  ]);

  const renderScene = BottomNavigation.SceneMap({
    Snap: CameraRoute,
    Data: DataRoute,
  });

  return (
    <SafeAreaProvider>
      <BottomNavigation
        navigationState={{ index, routes }}
        onIndexChange={setIndex}
        renderScene={renderScene}
      />
    </SafeAreaProvider>
  );
}

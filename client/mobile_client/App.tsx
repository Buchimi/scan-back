import { JSX, useState } from "react";
import { BottomNavigation, Text } from "react-native-paper";
import CameraPage from "src/pages/Camerapage";
import { SafeAreaProvider, SafeAreaView } from "react-native-safe-area-context";
import AnalyticsPage from "src/pages/Analytics";
import axios from "axios";
import { getUploadURI } from "@/provider/serverprovider";
import { GraphIcon, StoreIcon } from "@/icons/icons";
import { useSwipe } from "@/hooks/swipehook";
import { View } from "react-native";
import Store from "src/pages/Store";
const CameraRoute = ({
  onToggleLeft,
  onToggleRight,
}: {
  onToggleLeft: () => void;
  onToggleRight: () => void;
}) => (
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
    onToggleLeft={onToggleLeft}
    onToggleRight={onToggleRight}
  />
);

const DataRoute = () => (
  <SafeArea>
    <AnalyticsPage />
  </SafeArea>
); //<AnalyticsPage />;
const StoreRoute = () => (
  <SafeArea>
    <Store />
  </SafeArea>
);

const SafeArea = ({ children }: { children?: JSX.Element; style?: any }) => (
  <SafeAreaView>{children}</SafeAreaView>
);
export default function App() {
  const [index, setIndex] = useState(1);
  // const maxIndex = 2;
  const [routes] = useState([
    {
      key: "Store",
      title: "Store",
      focusedIcon: StoreIcon,
    },
    {
      key: "Snap",
      title: "Camera",
      focusedIcon: "camera",
      unfocusedIcon: "camera-outline",
    },
    {
      key: "Data",
      title: "Analytics",
      focusedIcon: GraphIcon,
    },
  ]);
  const swipeleft = () => {
    setIndex((index + 2) % 3);
  };
  const swiperight = () => setIndex((index + 1) % 3);
  const { onTouchStart, onTouchEnd } = useSwipe(swipeleft, swiperight);

  const renderScene = BottomNavigation.SceneMap({
    Store: () => <StoreRoute />,
    Snap: () => (
      <CameraRoute onToggleLeft={swipeleft} onToggleRight={swiperight} />
    ),
    Data: DataRoute,
  });

  return (
    <SafeAreaProvider onTouchStart={onTouchStart} onTouchEnd={onTouchEnd}>
      <BottomNavigation
        navigationState={{ index, routes }}
        onIndexChange={setIndex}
        renderScene={renderScene}
      />
    </SafeAreaProvider>
  );
}

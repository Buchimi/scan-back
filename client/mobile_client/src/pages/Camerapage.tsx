import { Dimensions, Image, SafeAreaView, StyleSheet } from "react-native";
import { FAB, Text } from "react-native-paper";
import { Camera, CameraType } from "expo-camera";
import { useState } from "react";
import { Button, TouchableOpacity, View } from "react-native";

type props = {
  onPictureTaken?: (payload: string) => void;
};

export default function App({ onPictureTaken }: props) {
  const [cam, setCamera] = useState<Camera>();
  const [camReady, setCamReady] = useState<boolean>(false);
  const [type, setType] = useState(CameraType.back);
  const [permission, requestPermission] = Camera.useCameraPermissions();

  const [image, setImage] = useState<string>();
  const [showImage, setShowImage] = useState<boolean>(false);

  if (!permission) {
    // Camera permissions are still loading
    return <View />;
  }

  if (!permission.granted) {
    // Camera permissions are not granted yet
    return (
      <View style={styles.container}>
        <Text style={{ textAlign: "center" }}>
          We need your permission to show the camera
        </Text>
        <Button onPress={requestPermission} title="grant permission" />
      </View>
    );
  }

  function toggleCameraType() {
    setType((current) =>
      current === CameraType.back ? CameraType.front : CameraType.back
    );
  }

  return (
    <View style={styles.container}>
      {!showImage && (
        <Camera
          style={styles.camera}
          type={type}
          ref={(cam) => setCamera(cam)}
          onCameraReady={() => setCamReady(true)}
        >
          <View style={styles.buttonContainer}>
            <TouchableOpacity style={styles.button} onPress={toggleCameraType}>
              <Text style={styles.text}>Flip Camera</Text>
            </TouchableOpacity>
          </View>
        </Camera>
      )}
      {showImage && (
        <Image
          width={Dimensions.get("screen").width}
          height={Dimensions.get("screen").height}
          source={{ uri: `data:image/jpg;base64,${image}` }}
        />
      )}

      <FAB
        icon="plus"
        style={styles.FAB}
        onPress={async () => {
          if (camReady) {
            const pic = await cam.takePictureAsync({ base64: true });
            console.log("cam has cammed");

            onPictureTaken(pic.base64);

            setImage(pic.base64);
            setShowImage(true);
            setTimeout(() => {
              setShowImage(false);
            }, 2000);
          }
        }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
  },
  camera: {
    flex: 1,
  },
  buttonContainer: {
    flex: 1,
    flexDirection: "row",
    backgroundColor: "transparent",
    margin: 64,
  },
  button: {
    flex: 1,
    alignSelf: "flex-end",
    alignItems: "center",
  },
  text: {
    fontSize: 24,
    fontWeight: "bold",
    color: "white",
  },
  FAB: {
    position: "absolute",
    bottom: "5%",
    right: "43%",
  },
});

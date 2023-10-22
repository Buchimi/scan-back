import { Dimensions, FlatList, View } from "react-native";
import { Button, Text } from "react-native-paper";
import { Image } from "react-native";
import { useState } from "react";
import { Ionicons } from "@expo/vector-icons";

const icon = () => <Ionicons name="md-cart-outline" size={24} color="black" />;
const FlatListData = [
  {
    name: "eggs",
    price: "6.25",
    url: "https://media.discordapp.net/attachments/811722728310046724/1165661150252367963/aTQ9.png?ex=6547a98b&is=6535348b&hm=4521916528fdc7e08b140d6b991da854c6a7339330283bd021132c629237dd07&=",
  },
  {
    name: "bag",
    price: "20",
    url: "https://images-ext-1.discordapp.net/external/NN4cnWFvqGIfTmsQvDGwBHVNClchQNSFNrvBnusN0dY/https/imgs.search.brave.com/Tr5uaRr0ZkW9Ou-6vm06XTyh9Tl4Lk5AL6lxCbvezGE/rs%3Afit%3A500%3A0%3A0/g%3Ace/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTcx/MjkzNTQ0L3Bob3Rv/L2dyZWVuLWhhbmRi/YWcuanBnP3M9NjEy/eDYxMiZ3PTAmaz0y/MCZjPW80OHdONllQ/TVRRZFV4OEVpR2Np/NjVqLXFpMVhNbEw3/cUxZZTYyUmNkbGc9",
  },
  {
    name: "redbull",
    price: "14",
    url: "https://media.discordapp.net/attachments/811722728310046724/1165662127973994627/VFFPYkJBPQ.png?ex=6547aa74&is=65353574&hm=c06257ce451ff32240d6457f8df63a93d3472836cde4dd88c838e9ec484203c6&=&width=487&height=607",
  },
  {
    name: "boba",
    price: "5",
    url: "https://media.discordapp.net/attachments/811722728310046724/1165663977578184775/Y1dmek9iNTlEX009.png?ex=6547ac2d&is=6535372d&hm=414f8f7e0597c98c1eddb0f42f2c451f290c301ae15cb1fdb368f587783ccd7b&=&width=418&height=607",
  },
  {
    name: "pen",
    price: "2",
    url: "https://media.discordapp.net/attachments/811722728310046724/1165665470486151268/bk1FYzZjNURmM2s9.png?ex=6547ad91&is=65353891&hm=f98f63d6cdadb8d820664d54b552710f6080220f6b33b0c4fd63ac1411a3f6fb&=",
  },
  {
    name: "shirt",
    price: "23",
    url: "https://media.discordapp.net/attachments/811722728310046724/1165665829979951104/LVNUNmVGdlE9.png?ex=6547ade6&is=653538e6&hm=eec675dda99b20f270b81833f5d102a83d91e9d850aa1736ca3b289cf8f9dec8&=",
  },
];
export default function Store() {
  const [amount, setAmount] = useState(0);
  return (
    <View>
      <View
        style={{ display: "flex", flexDirection: "row-reverse", right: "5%" }}
      >
        <Button mode="contained" icon={icon}>
          Cart
        </Button>
        <Text style={{ marginHorizontal: "10%" }}>Shop</Text>
      </View>
      <FlatList
        data={FlatListData}
        renderItem={(item) => (
          <View>
            <Image
              source={{ uri: item.item.url }}
              width={(Dimensions.get("screen").width * 9) / 10}
              height={(Dimensions.get("screen").height * 3) / 10}
            />
            <View
              style={{
                display: "flex",
                flexDirection: "row",
                justifyContent: "space-around",
              }}
            >
              <Text>Name: {item.item.name}</Text>
              <Text>Price: {item.item.price}</Text>
            </View>
            <Button
              onPress={() => {
                setAmount(Number.parseInt(item.item.price) + amount);
              }}
              style={{}}
            >
              Add to cart
            </Button>
          </View>
        )}
      ></FlatList>
    </View>
  );
}

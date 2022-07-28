# 数据说明

项目介绍及数据来源见 Kaggle：[Spaceship Titanic](https://www.kaggle.com/competitions/spaceship-titanic/overview)。

数据详情：

- `data.csv` 训练集样本量约为 8700 人；
- 数据字段详情：
  - 数据字段共有 14 个；
  - 字段详情：
    - `PassengerId`：每个乘客的唯一标识。其形式为 `gggg_pp`，其中 `gggg` 表示乘客一同乘坐的团体，`pp` 是他们在团体中的编号。团体中的个人通常是家庭成员，**但这也不是绝对的**；
    - `HomePlanet`：乘客所离开的星球，通常是他们永久居住的星球；
    - `CryoSleep`：表示乘客是否选择在航行期间进入深度睡眠，处于深度睡眠状态的乘客被限制在他们坐在的船舱内；
    - `Cabin`：乘客所住的船舱及座位号，采取 `甲板/编号/侧面` 的形式编号，其中侧面的 P 代表左舷（船身左半边），S 代表右舷（船身右半边）；
    - `Destination`：乘客此次航行的目的地；
    - `Age`：乘客的年龄；
    - `VIP`：乘客是否为 VIP；
    - `RoomService`，`FoodCourt`，`ShoppingMall`，`Spa`，`VRDeck`：即乘客在太空船的众多豪华设施项中的**花销金额**；
    - `Name`：乘客的名字和姓氏；
    - `Transported`：乘客是否被运送到另一个空间，**这也是训练集的参考答案以及需要在测试集中预测的结果**。

1. tensorflow 2.0下使用1.0的功能
    ```python
    import tensorflow.compat.v1 as tf
    tf.disable_v2_behavior()
    ```
2. 查看tensorflow版本
   ```python
    print(tf.__version__)
   ```
3. 准备MNIST数据集
   ```python
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
   ```
4. 堆叠模型
   ```python
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
   ```
5. 优化器、损失函数、评价指标
   ```python
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrix=['accuracy'])
   ```
6. 训练、评估
   ```python
   model.fit(x_train, y_train, epochs=5)
   model.evaluate(x_test, y_test, verbose=2)

   """
    verbose：用于fit和evaluate的日志显示
    verbose = 0 为不在标准输出流输出日志信息
    verbose = 1 默认情况，为输出进度条记录
    verbose = 2 没有进度条，只是输出一行记录
   """
   ```
7. torch.nn.sparse_softmax_cross_entropy_with_logits
   ```
   # 官方文档
   https://www.tensorflow.org/api_docs/python/tf/nn/sparse_softmax_cross_entropy_with_logits

   # 区别：tf.nn.sparse_softmax_cross_entropy_with_logits()和tf.nn.softmax_cross_entropy_with_logits()
   http://www.4k8k.xyz/article/AgentLjc/79620774

   # 看不到gen_nn_ops.py源码的原因
   https://stackoverflow.com/questions/41147734/looking-for-source-code-of-from-gen-nn-ops-in-tensorflow

   # gen_nn_ops.py源码细节：公式
   https://www.5axxw.com/questions/content/hpmko8

   # 公式细节剖析
   https://freemind.pluskid.org/machine-learning/softmax-vs-softmax-loss-numerical-stability/
   ```
   torch.nn有两个softmax交叉熵损失函数，[sparse_softmax_cross_entropy_with_logits](https://www.tensorflow.org/api_docs/python/tf/nn/sparse_softmax_cross_entropy_with_logits)，[softmax_cross_entropy_with_logits](https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits)。

   首先，二者所接受的label输入不同，前者允许输入label id，后者允许输入label prob。示例如下：
   ```
   label_id = [2, 1, 1, 0]  
   label_prob = [[0.0, 0.0, 1.0],
                 [0.0, 1.0, 0.0],
                 [0.0, 0.9, 0.1],
                 [0.8, 0.2, 0.0]]
   
   # 没有经过softmax运算的score值
   pred_without_softmax = [[0.3, 0.6, 1.6],
                           [1.0, 0.3, 0.0],
                           [0.0, 3.0, 0.6],
                           [2.0, 0.0, 0.0]]

   loss_1 = torch.sparse_softmax_cross_entropy_with_logits(label_id, pred_without_softmax)
   loss_2 = torch.softmax_cross_entropy_with_logits(label_prob, pred_without_softmax)
   ```

   其次，二者的运算过程不同，前者的运算量更小，因此更高效，并且它的**numerical stability**更好。运算细节如下（前者对应第二个公式；后者对应第一个公式）：

   $$\tilde{\ell}(y,z) = -\log\left(\frac{e^{z_y}}{\sum_{j=1}^m e^{z_j}}\right) = \log\left(\sum_{j=1}^m e^{z_j}\right)-z_y$$

   在下面的对比图中，蓝线表示sparse_softmax_cross_entropy_with_logits，黄线表示softmax_cross_entropy_with_logits，数值表示二者的梯度值与真实梯度值的差距，可以发现，黄线在输入值为非常小的负数时，下溢为Nan；而蓝线与真实值非常接近，因此蓝线的**numerical stability**更好。
   ![](https://freemind.pluskid.org/att/2014/11/softmax-loss-discrepancy.svg)

   但是，在上面的对比图中，蓝线在输入值为非常大的正数时，上溢为Nan。如果要解决这个问题，可以在求 exponential 之前将 z 的每一个元素减去 z 的最大值。
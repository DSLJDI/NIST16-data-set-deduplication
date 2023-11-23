import os
from PIL import Image

def outputFolder(pic_name, folder_path, folder_mask_path, dir_path, task_folder, task_mask_folder):
    '''
    pic_name: 为我们清洗好所留下的文件的名字的列表
    folder_path: NIST16原数据集的Tampered image所在的文件夹
    folder_mask_image: NIST16原数据集Ground-truth image所在的文件夹
    dir_path: 指定清洗后的图片所存的主文件夹
    task_folder: 指定清洗后的Tampered image所存的文件夹
    task_mask_folder: 指定清洗后的Ground-truth所存的文件夹
    '''
    # 指定目录和要创建的文件夹名
    # dir_path = './alter_NIST16_task1'

    # 拼接文件夹路径
    folderP = os.path.join(dir_path, task_folder)
    folderP_mask = os.path.join(dir_path, task_mask_folder)

    # 创建相应的文件夹
    os.makedirs(folderP)
    os.makedirs(folderP_mask)
    n = len(pic_name)
    print(n)

    # 将pic_name中有的图片保存到相应的文件夹下
    for i in range(n):
        image_path = os.path.join(folder_path, pic_name[i])
        iamge_mask_path = os.path.join(folder_mask_path, pic_name[i])

        image = Image.open(image_path)
        output_path = os.path.join(folderP, pic_name[i])
        image.save(output_path)

        image_mask = Image.open(iamge_mask_path)
        name = pic_name[i].split(".")
        output_mask_path = os.path.join(folderP_mask, name[0]+'_mask.jpg')
        image_mask.save(output_mask_path)


# task1 Name of the image left after cleaning
task1_pic_name = ['NC2016_1987.jpg', 'NC2016_2262.jpg', 'NC2016_7344.jpg', 'NC2016_4901.jpg', 'NC2016_6802.jpg', 'NC2016_0963.jpg', 'NC2016_3207.jpg', 'NC2016_0211.jpg', 'NC2016_6138.jpg', 'NC2016_3195.jpg', 'NC2016_1758.jpg', 'NC2016_0766.jpg', 'NC2016_4586.jpg', 'NC2016_3576.jpg', 'NC2016_2398.jpg', 'NC2016_4192.jpg', 'NC2016_0481.jpg', 'NC2016_2907.jpg', 'NC2016_1470.jpg', 'NC2016_1857.jpg', 'NC2016_3704.jpg', 'NC2016_4360.jpg', 'NC2016_3001.jpg', 'NC2016_1532.jpg', 'NC2016_5211.jpg', 'NC2016_5275.jpg', 'NC2016_5887.jpg', 'NC2016_0313.jpg', 'NC2016_4962.jpg', 'NC2016_4940.jpg', 'NC2016_1944.jpg', 'NC2016_0130.jpg', 'NC2016_7781.jpg', 'NC2016_0600.jpg', 'NC2016_1966.jpg', 'NC2016_1868.jpg', 'NC2016_2444.jpg', 'NC2016_3627.jpg', 'NC2016_0289.jpg', 'NC2016_5702.jpg', 'NC2016_1759.jpg', 'NC2016_1217.jpg', 'NC2016_2624.jpg', 'NC2016_1917.jpg', 'NC2016_2785.jpg', 'NC2016_4837.jpg', 'NC2016_1255.jpg', 'NC2016_4937.jpg', 'NC2016_0613.jpg', 'NC2016_0048.jpg', 'NC2016_0459.jpg', 'NC2016_2492.jpg', 'NC2016_0254.jpg', 'NC2016_0887.jpg', 'NC2016_2300.jpg', 'NC2016_1755.jpg', 'NC2016_1728.jpg', 'NC2016_3680.jpg', 'NC2016_1125.jpg', 'NC2016_1433.jpg', 'NC2016_6634.jpg', 'NC2016_1546.jpg', 'NC2016_2122.jpg', 'NC2016_1264.jpg', 'NC2016_3304.jpg', 'NC2016_3601.jpg', 'NC2016_3067.jpg', 'NC2016_0830.jpg', 'NC2016_0650.jpg', 'NC2016_4730.jpg', 'NC2016_5042.jpg', 'NC2016_1764.jpg', 'NC2016_6456.jpg', 'NC2016_5512.jpg', 'NC2016_0343.jpg', 'NC2016_1571.jpg', 'NC2016_5334.jpg', 'NC2016_2802.jpg', 'NC2016_1933.jpg', 'NC2016_0342.jpg', 'NC2016_4429.jpg', 'NC2016_2304.jpg', 'NC2016_0484.jpg', 'NC2016_4896.jpg', 'NC2016_1946.jpg', 'NC2016_1616.jpg', 'NC2016_1299.jpg', 'NC2016_1893.jpg', 'NC2016_5739.jpg', 'NC2016_5645.jpg', 'NC2016_4145.jpg', 'NC2016_2023.jpg', 'NC2016_1213.jpg', 'NC2016_1873.jpg', 'NC2016_3850.jpg', 'NC2016_1937.jpg', 'NC2016_4432.jpg', 'NC2016_0859.jpg', 'NC2016_0299.jpg', 'NC2016_6287.jpg', 'NC2016_1986.jpg', 'NC2016_2459.jpg', 'NC2016_5943.jpg', 'NC2016_0278.jpg', 'NC2016_0741.jpg', 'NC2016_3508.jpg', 'NC2016_3953.jpg', 'NC2016_5009.jpg', 'NC2016_0286.jpg', 'NC2016_1165.jpg', 'NC2016_4326.jpg', 'NC2016_3692.jpg', 'NC2016_1396.jpg', 'NC2016_3675.jpg', 'NC2016_0222.jpg', 'NC2016_9073.jpg', 'NC2016_0571.jpg', 'NC2016_3563.jpg', 'NC2016_0871.jpg', 'NC2016_4053.jpg', 'NC2016_0550.jpg', 'NC2016_1967.jpg', 'NC2016_4211.jpg', 'NC2016_2571.jpg', 'NC2016_1437.jpg', 'NC2016_5397.jpg', 'NC2016_3577.jpg', 'NC2016_5064.jpg', 'NC2016_3911.jpg', 'NC2016_4301.jpg', 'NC2016_6260.jpg', 'NC2016_6450.jpg', 'NC2016_3374.jpg', 'NC2016_4993.jpg', 'NC2016_5929.jpg', 'NC2016_0527.jpg', 'NC2016_1804.jpg', 'NC2016_4161.jpg', 'NC2016_0674.jpg', 'NC2016_5239.jpg', 'NC2016_0293.jpg', 'NC2016_2305.jpg', 'NC2016_0016.jpg', 'NC2016_1520.jpg', 'NC2016_2202.jpg', 'NC2016_0796.jpg', 'NC2016_1718.jpg', 'NC2016_0787.jpg', 'NC2016_1094.jpg', 'NC2016_1749.jpg', 'NC2016_0942.jpg', 'NC2016_3119.jpg', 'NC2016_2144.jpg', 'NC2016_1103.jpg', 'NC2016_1515.jpg', 'NC2016_1225.jpg', 'NC2016_2621.jpg', 'NC2016_0408.jpg', 'NC2016_1513.jpg', 'NC2016_6103.jpg', 'NC2016_4498.jpg', 'NC2016_2255.jpg', 'NC2016_2354.jpg', 'NC2016_3389.jpg', 'NC2016_2031.jpg', 'NC2016_2666.jpg', 'NC2016_2126.jpg', 'NC2016_2858.jpg', 'NC2016_0906.jpg', 'NC2016_4228.jpg', 'NC2016_2754.jpg', 'NC2016_6625.jpg', 'NC2016_6849.jpg', 'NC2016_1555.jpg', 'NC2016_0587.jpg', 'NC2016_0444.jpg', 'NC2016_0876.jpg', 'NC2016_0684.jpg', 'NC2016_4507.jpg', 'NC2016_7025.jpg', 'NC2016_4589.jpg', 'NC2016_0596.jpg', 'NC2016_2550.jpg']

# task2 train Name of the image left after cleaning
task2_train_pic_name = ['NC2016_7126.jpg', 'NC2016_6886.jpg', 'NC2016_7344.jpg', 'NC2016_7356.jpg', 'NC2016_9462.jpg', 'NC2016_4901.jpg', 'NC2016_6802.jpg', 'NC2016_6969.jpg', 'NC2016_7872.jpg', 'NC2016_7759.jpg', 'NC2016_4543.jpg', 'NC2016_6619.jpg', 'NC2016_6003.jpg', 'NC2016_3207.jpg', 'NC2016_0211.jpg', 'NC2016_4190.jpg', 'NC2016_5321.jpg', 'NC2016_8350.jpg', 'NC2016_1758.jpg', 'NC2016_3732.jpg', 'NC2016_3854.jpg', 'NC2016_4586.jpg', 'NC2016_3491.jpg', 'NC2016_3576.jpg', 'NC2016_2296.jpg', 'NC2016_4956.jpg', 'NC2016_9822.jpg', 'NC2016_2398.jpg', 'NC2016_4192.jpg', 'NC2016_4867.jpg', 'NC2016_0481.jpg', 'NC2016_7352.jpg', 'NC2016_3059.jpg', 'NC2016_1470.jpg', 'NC2016_4487.jpg', 'NC2016_0569.jpg', 'NC2016_6218.jpg', 'NC2016_7214.jpg', 'NC2016_1857.jpg', 'NC2016_0758.jpg', 'NC2016_7489.jpg', 'NC2016_7095.jpg', 'NC2016_7772.jpg', 'NC2016_3704.jpg', 'NC2016_9759.jpg', 'NC2016_5240.jpg', 'NC2016_4360.jpg', 'NC2016_1545.jpg', 'NC2016_3001.jpg', 'NC2016_0351.jpg', 'NC2016_1289.jpg', 'NC2016_8450.jpg', 'NC2016_9857.jpg', 'NC2016_9437.jpg', 'NC2016_4327.jpg', 'NC2016_8629.jpg', 'NC2016_9009.jpg', 'NC2016_9272.jpg', 'NC2016_6607.jpg', 'NC2016_2864.jpg', 'NC2016_5275.jpg', 'NC2016_7023.jpg', 'NC2016_2487.jpg', 'NC2016_0313.jpg', 'NC2016_9112.jpg', 'NC2016_4962.jpg', 'NC2016_4940.jpg', 'NC2016_4936.jpg', 'NC2016_6888.jpg', 'NC2016_6651.jpg', 'NC2016_5884.jpg', 'NC2016_5444.jpg', 'NC2016_9453.jpg', 'NC2016_1890.jpg', 'NC2016_6005.jpg', 'NC2016_8606.jpg', 'NC2016_6722.jpg', 'NC2016_0130.jpg', 'NC2016_6806.jpg', 'NC2016_5446.jpg', 'NC2016_7781.jpg', 'NC2016_8736.jpg', 'NC2016_4084.jpg', 'NC2016_8253.jpg', 'NC2016_2444.jpg', 'NC2016_3092.jpg', 'NC2016_0994.jpg', 'NC2016_4875.jpg', 'NC2016_6309.jpg', 'NC2016_3627.jpg', 'NC2016_7894.jpg', 'NC2016_9629.jpg', 'NC2016_0289.jpg', 'NC2016_7065.jpg', 'NC2016_1759.jpg', 'NC2016_3475.jpg', 'NC2016_3187.jpg', 'NC2016_1217.jpg', 'NC2016_8236.jpg', 'NC2016_6426.jpg', 'NC2016_6505.jpg', 'NC2016_1917.jpg', 'NC2016_6796.jpg', 'NC2016_4175.jpg', 'NC2016_2785.jpg', 'NC2016_4837.jpg', 'NC2016_4604.jpg', 'NC2016_4804.jpg', 'NC2016_1255.jpg', 'NC2016_4937.jpg', 'NC2016_7152.jpg', 'NC2016_6453.jpg', 'NC2016_9790.jpg', 'NC2016_0613.jpg', 'NC2016_5243.jpg', 'NC2016_7511.jpg', 'NC2016_4549.jpg', 'NC2016_0048.jpg', 'NC2016_8618.jpg', 'NC2016_9317.jpg', 'NC2016_8714.jpg', 'NC2016_0459.jpg', 'NC2016_2492.jpg', 'NC2016_0254.jpg', 'NC2016_2300.jpg', 'NC2016_1755.jpg', 'NC2016_3680.jpg', 'NC2016_9789.jpg', 'NC2016_9653.jpg', 'NC2016_9781.jpg', 'NC2016_8796.jpg', 'NC2016_6634.jpg', 'NC2016_2722.jpg', 'NC2016_1732.jpg', 'NC2016_1546.jpg', 'NC2016_2122.jpg', 'NC2016_7989.jpg', 'NC2016_1264.jpg', 'NC2016_1720.jpg', 'NC2016_9628.jpg', 'NC2016_3067.jpg', 'NC2016_2456.jpg', 'NC2016_1293.jpg', 'NC2016_6011.jpg', 'NC2016_0650.jpg', 'NC2016_4363.jpg', 'NC2016_5042.jpg', 'NC2016_5257.jpg', 'NC2016_6312.jpg', 'NC2016_1764.jpg', 'NC2016_6456.jpg', 'NC2016_4247.jpg', 'NC2016_0343.jpg', 'NC2016_3938.jpg', 'NC2016_4049.jpg', 'NC2016_8769.jpg', 'NC2016_2802.jpg', 'NC2016_0202.jpg', 'NC2016_7691.jpg', 'NC2016_9463.jpg', 'NC2016_3204.jpg', 'NC2016_2606.jpg', 'NC2016_7834.jpg', 'NC2016_0342.jpg', 'NC2016_5270.jpg', 'NC2016_4528.jpg', 'NC2016_8058.jpg', 'NC2016_5809.jpg', 'NC2016_2304.jpg', 'NC2016_0484.jpg', 'NC2016_9445.jpg', 'NC2016_4896.jpg', 'NC2016_8065.jpg', 'NC2016_9868.jpg', 'NC2016_6040.jpg', 'NC2016_2051.jpg', 'NC2016_6002.jpg', 'NC2016_1616.jpg', 'NC2016_2040.jpg', 'NC2016_1825.jpg', 'NC2016_6704.jpg', 'NC2016_7956.jpg', 'NC2016_7437.jpg', 'NC2016_2564.jpg', 'NC2016_5645.jpg', 'NC2016_7146.jpg', 'NC2016_4145.jpg', 'NC2016_2023.jpg', 'NC2016_6910.jpg', 'NC2016_9647.jpg', 'NC2016_1572.jpg', 'NC2016_4642.jpg', 'NC2016_9186.jpg', 'NC2016_1873.jpg', 'NC2016_3850.jpg', 'NC2016_6069.jpg', 'NC2016_7890.jpg', 'NC2016_8517.jpg', 'NC2016_9691.jpg', 'NC2016_1937.jpg', 'NC2016_0516.jpg', 'NC2016_6438.jpg', 'NC2016_7312.jpg', 'NC2016_4432.jpg', 'NC2016_0859.jpg', 'NC2016_7587.jpg', 'NC2016_0299.jpg', 'NC2016_6287.jpg', 'NC2016_2459.jpg', 'NC2016_9573.jpg', 'NC2016_4571.jpg', 'NC2016_9415.jpg', 'NC2016_4427.jpg', 'NC2016_4076.jpg', 'NC2016_9807.jpg', 'NC2016_4621.jpg', 'NC2016_7921.jpg', 'NC2016_0278.jpg', 'NC2016_5182.jpg', 'NC2016_0741.jpg', 'NC2016_7572.jpg', 'NC2016_3508.jpg', 'NC2016_4188.jpg', 'NC2016_6116.jpg', 'NC2016_1165.jpg', 'NC2016_9347.jpg', 'NC2016_7338.jpg', 'NC2016_4620.jpg', 'NC2016_4599.jpg', 'NC2016_4326.jpg', 'NC2016_8754.jpg', 'NC2016_5730.jpg', 'NC2016_3692.jpg', 'NC2016_4883.jpg', 'NC2016_1396.jpg', 'NC2016_5937.jpg', 'NC2016_3675.jpg', 'NC2016_2372.jpg', 'NC2016_7339.jpg', 'NC2016_3004.jpg', 'NC2016_6391.jpg', 'NC2016_0222.jpg', 'NC2016_0571.jpg', 'NC2016_3563.jpg', 'NC2016_6890.jpg', 'NC2016_0871.jpg', 'NC2016_4053.jpg', 'NC2016_2441.jpg', 'NC2016_0550.jpg', 'NC2016_3829.jpg', 'NC2016_7504.jpg', 'NC2016_3612.jpg', 'NC2016_2835.jpg', 'NC2016_5290.jpg', 'NC2016_0589.jpg', 'NC2016_1437.jpg', 'NC2016_8834.jpg', 'NC2016_7429.jpg', 'NC2016_5397.jpg', 'NC2016_3432.jpg', 'NC2016_2090.jpg', 'NC2016_9962.jpg', 'NC2016_4699.jpg', 'NC2016_9541.jpg', 'NC2016_3577.jpg', 'NC2016_0800.jpg', 'NC2016_5064.jpg', 'NC2016_3911.jpg', 'NC2016_4301.jpg', 'NC2016_6260.jpg', 'NC2016_6889.jpg', 'NC2016_8738.jpg', 'NC2016_4993.jpg', 'NC2016_5929.jpg', 'NC2016_1804.jpg', 'NC2016_4161.jpg', 'NC2016_0674.jpg', 'NC2016_9381.jpg', 'NC2016_1379.jpg', 'NC2016_4300.jpg', 'NC2016_9811.jpg', 'NC2016_5597.jpg', 'NC2016_5239.jpg', 'NC2016_6347.jpg', 'NC2016_0293.jpg', 'NC2016_8586.jpg', 'NC2016_2305.jpg', 'NC2016_6414.jpg', 'NC2016_1814.jpg', 'NC2016_2812.jpg', 'NC2016_8051.jpg', 'NC2016_6217.jpg', 'NC2016_2080.jpg', 'NC2016_4534.jpg', 'NC2016_5343.jpg', 'NC2016_1520.jpg', 'NC2016_7865.jpg', 'NC2016_1777.jpg', 'NC2016_4651.jpg', 'NC2016_2202.jpg', 'NC2016_0796.jpg', 'NC2016_0623.jpg', 'NC2016_2942.jpg', 'NC2016_0280.jpg', 'NC2016_9994.jpg', 'NC2016_0787.jpg', 'NC2016_1094.jpg', 'NC2016_1749.jpg', 'NC2016_5174.jpg', 'NC2016_0942.jpg', 'NC2016_5881.jpg', 'NC2016_9257.jpg', 'NC2016_6412.jpg', 'NC2016_2144.jpg', 'NC2016_1475.jpg', 'NC2016_1103.jpg', 'NC2016_1515.jpg', 'NC2016_9235.jpg', 'NC2016_6487.jpg', 'NC2016_1225.jpg', 'NC2016_9725.jpg', 'NC2016_4512.jpg', 'NC2016_0408.jpg', 'NC2016_2649.jpg', 'NC2016_0957.jpg', 'NC2016_4166.jpg', 'NC2016_8411.jpg', 'NC2016_1513.jpg', 'NC2016_4428.jpg', 'NC2016_6103.jpg', 'NC2016_4498.jpg', 'NC2016_4544.jpg', 'NC2016_6811.jpg', 'NC2016_0128.jpg', 'NC2016_7563.jpg', 'NC2016_2512.jpg', 'NC2016_2354.jpg', 'NC2016_3389.jpg', 'NC2016_9091.jpg', 'NC2016_2031.jpg', 'NC2016_6673.jpg', 'NC2016_9055.jpg', 'NC2016_2666.jpg', 'NC2016_6555.jpg', 'NC2016_2858.jpg', 'NC2016_0906.jpg', 'NC2016_6817.jpg', 'NC2016_8909.jpg', 'NC2016_3010.jpg', 'NC2016_1562.jpg', 'NC2016_1879.jpg', 'NC2016_4399.jpg', 'NC2016_9173.jpg', 'NC2016_8148.jpg', 'NC2016_5218.jpg', 'NC2016_1555.jpg', 'NC2016_7534.jpg', 'NC2016_5913.jpg', 'NC2016_5781.jpg', 'NC2016_5442.jpg', 'NC2016_0229.jpg', 'NC2016_0444.jpg', 'NC2016_7094.jpg', 'NC2016_0876.jpg', 'NC2016_0684.jpg', 'NC2016_5196.jpg', 'NC2016_1633.jpg', 'NC2016_0625.jpg', 'NC2016_7652.jpg', 'NC2016_7882.jpg', 'NC2016_4717.jpg', 'NC2016_7067.jpg', 'NC2016_8980.jpg', 'NC2016_0596.jpg', 'NC2016_5749.jpg', 'NC2016_3868.jpg', 'NC2016_8067.jpg', 'NC2016_7881.jpg', 'NC2016_9766.jpg', 'NC2016_2550.jpg', 'NC2016_6640.jpg', 'NC2016_8500.jpg', 'NC2016_4503.jpg']

# task2 test Name of the image left after cleaning
task2_test_pic_name = ['NC2016_1987.jpg', 'NC2016_2262.jpg', 'NC2016_6880.jpg', 'NC2016_7420.jpg', 'NC2016_6495.jpg', 'NC2016_3832.jpg', 'NC2016_0963.jpg', 'NC2016_7752.jpg', 'NC2016_6138.jpg', 'NC2016_3195.jpg', 'NC2016_8371.jpg', 'NC2016_4463.jpg', 'NC2016_6142.jpg', 'NC2016_7298.jpg', 'NC2016_0766.jpg', 'NC2016_8183.jpg', 'NC2016_6757.jpg', 'NC2016_2907.jpg', 'NC2016_7737.jpg', 'NC2016_3801.jpg', 'NC2016_9176.jpg', 'NC2016_1198.jpg', 'NC2016_6233.jpg', 'NC2016_9984.jpg', 'NC2016_8682.jpg', 'NC2016_1532.jpg', 'NC2016_6253.jpg', 'NC2016_6479.jpg', 'NC2016_4437.jpg', 'NC2016_5211.jpg', 'NC2016_4219.jpg', 'NC2016_9108.jpg', 'NC2016_5887.jpg', 'NC2016_4232.jpg', 'NC2016_4009.jpg', 'NC2016_1944.jpg', 'NC2016_8091.jpg', 'NC2016_0600.jpg', 'NC2016_1966.jpg', 'NC2016_1148.jpg', 'NC2016_8965.jpg', 'NC2016_1868.jpg', 'NC2016_6014.jpg', 'NC2016_6518.jpg', 'NC2016_5702.jpg', 'NC2016_3595.jpg', 'NC2016_2624.jpg', 'NC2016_2403.jpg', 'NC2016_2901.jpg', 'NC2016_8127.jpg', 'NC2016_9651.jpg', 'NC2016_6572.jpg', 'NC2016_0887.jpg', 'NC2016_8266.jpg', 'NC2016_1728.jpg', 'NC2016_1125.jpg', 'NC2016_7398.jpg', 'NC2016_1433.jpg', 'NC2016_3842.jpg', 'NC2016_6733.jpg', 'NC2016_1543.jpg', 'NC2016_3304.jpg', 'NC2016_3601.jpg', 'NC2016_8457.jpg', 'NC2016_0830.jpg', 'NC2016_3707.jpg', 'NC2016_4730.jpg', 'NC2016_6326.jpg', 'NC2016_5512.jpg', 'NC2016_1571.jpg', 'NC2016_7747.jpg', 'NC2016_5334.jpg', 'NC2016_3666.jpg', 'NC2016_0394.jpg', 'NC2016_4981.jpg', 'NC2016_3253.jpg', 'NC2016_1933.jpg', 'NC2016_4429.jpg', 'NC2016_5313.jpg', 'NC2016_4434.jpg', 'NC2016_1946.jpg', 'NC2016_1299.jpg', 'NC2016_5131.jpg', 'NC2016_1893.jpg', 'NC2016_5739.jpg', 'NC2016_1213.jpg', 'NC2016_7262.jpg', 'NC2016_7564.jpg', 'NC2016_7390.jpg', 'NC2016_2438.jpg', 'NC2016_7561.jpg', 'NC2016_1986.jpg', 'NC2016_2618.jpg', 'NC2016_5943.jpg', 'NC2016_6238.jpg', 'NC2016_6519.jpg', 'NC2016_2772.jpg', 'NC2016_3953.jpg', 'NC2016_9109.jpg', 'NC2016_8926.jpg', 'NC2016_5009.jpg', 'NC2016_3851.jpg', 'NC2016_0286.jpg', 'NC2016_7480.jpg', 'NC2016_3397.jpg', 'NC2016_3688.jpg', 'NC2016_9073.jpg', 'NC2016_1967.jpg', 'NC2016_7048.jpg', 'NC2016_4211.jpg', 'NC2016_2571.jpg', 'NC2016_5892.jpg', 'NC2016_7539.jpg', 'NC2016_9904.jpg', 'NC2016_3725.jpg', 'NC2016_9534.jpg', 'NC2016_8814.jpg', 'NC2016_5345.jpg', 'NC2016_2167.jpg', 'NC2016_3906.jpg', 'NC2016_5048.jpg', 'NC2016_8581.jpg', 'NC2016_3312.jpg', 'NC2016_7654.jpg', 'NC2016_7580.jpg', 'NC2016_1141.jpg', 'NC2016_6565.jpg', 'NC2016_6450.jpg', 'NC2016_3374.jpg', 'NC2016_7359.jpg', 'NC2016_0527.jpg', 'NC2016_7666.jpg', 'NC2016_6623.jpg', 'NC2016_5307.jpg', 'NC2016_9818.jpg', 'NC2016_6058.jpg', 'NC2016_1332.jpg', 'NC2016_0016.jpg', 'NC2016_9513.jpg', 'NC2016_9241.jpg', 'NC2016_3042.jpg', 'NC2016_5921.jpg', 'NC2016_4274.jpg', 'NC2016_2027.jpg', 'NC2016_6725.jpg', 'NC2016_1718.jpg', 'NC2016_9727.jpg', 'NC2016_3119.jpg', 'NC2016_3476.jpg', 'NC2016_3660.jpg', 'NC2016_2621.jpg', 'NC2016_5847.jpg', 'NC2016_8720.jpg', 'NC2016_5300.jpg', 'NC2016_3382.jpg', 'NC2016_7673.jpg', 'NC2016_2255.jpg', 'NC2016_2126.jpg', 'NC2016_9191.jpg', 'NC2016_8265.jpg', 'NC2016_4228.jpg', 'NC2016_2754.jpg', 'NC2016_6625.jpg', 'NC2016_7151.jpg', 'NC2016_6849.jpg', 'NC2016_5154.jpg', 'NC2016_5604.jpg', 'NC2016_6343.jpg', 'NC2016_0587.jpg', 'NC2016_7878.jpg', 'NC2016_7953.jpg', 'NC2016_7354.jpg', 'NC2016_8900.jpg', 'NC2016_4507.jpg', 'NC2016_8897.jpg', 'NC2016_7025.jpg', 'NC2016_9038.jpg', 'NC2016_4589.jpg', 'NC2016_9402.jpg', 'NC2016_9014.jpg', 'NC2016_3335.jpg']

# 得到经过task1清洗后的图片
outputFolder(task1_pic_name, "./NIST16_1024/Tp", "./NIST16_1024/Gt", "./alter_NIST16_task1", "task1", "task1_mask")

# 得到经过task2清洗后的训练图片
outputFolder(task2_train_pic_name, "./NIST16_1024/Tp", "./NIST16_1024/Gt", "./alter_NIST16_task2", "task2_train", "task2_train_mask")

# 得到经过task1清洗后的测试图片
outputFolder(task2_test_pic_name, "./NIST16_1024/Tp", "./NIST16_1024/Gt", "./alter_NIST16_task2", "task2_test", "task2_test_mask")
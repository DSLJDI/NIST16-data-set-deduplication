# Two methods to deduplicate NIST16 tamper detection data sets
This repository includes resources below:

* **NIST16** Image Tampering Detection Evaluation Dataset.
* Ground-truth of NIST16,  Accurate labels or data used to train and evaluate models.

## Introduce

The NIST16 data set is a commonly used tamper detection data set, containing 564 tampered images, in which the tampering types of copy-move, splicing and Inpainting are distributed. And compared to other tampering detection data sets, its images are very clear. So overall it is a data set with good tampering quality. However, this data set has a very fatal flaw. It uses  **"extremely similar" tampering  patterns for the same original picture  , and there are often a very large number of "a group of similar pictures"**.

## Problems in deep learning based on NIST16

Some examples of similar images:

![](D:\nist16\output_next1\48\NC2016_1148.jpg)

This brings about a problem. When training a deep learning model, the model does not really need to pay attention to the traces related to tampering. It often only needs to learn the pattern of "there is a black object on the yellow background in the lower left corner of the image", and then activate the output accordingly. A "bird-shaped mask" can achieve a very high accuracy, which is obviously not what we want to see.



In terms of experimental results, there are many papers that use the method of randomly dividing the training set and test set for evaluation on the NIST16 data set. According to the above conclusion, a large number of pictures and masks are very similar, so they are randomly assigned to the training set and the test set at the same time, resulting in a very serious data leakage. Therefore, almost all current methods that randomly split the training set and test set have exceptionally high metrics and performance on the NIST16 dataset. In contrast, if you first train on other datasets and then test using NIST16, you will not achieve such performance.



## work that needs to be done

In order to eliminate the impact of Data leakage, it is necessary to filter the NIST16 data set to a certain extent. Based on such a demand, we proposed two solutions:

* For "each group of similar images", only one image-mask pair is retained.
* For "each group of similar images", keep all images. However, a division of the training set and the test set must be given to ensure that the "same group" of similar images will not appear in both the training set and the test set. In contrast, there may be some images that are similar, but the masks are not. We should try our best to make them distributed in the training set and the test set to increase the difficulty of training.



## Download of the modified NIST16 dataset

For method one, in principle we choose the pictures that “look the most real” to keep. This allows the model to not only focus on tampering traces, but also "cheat" through the pattern of the image. This is used to solve the "data leakage" problem.

Here we place the download address of the NIST16 data set filtered by method 1 xxxxxxxxxxxxxxxx，you can **DOWNLOAD** it through the link above.

For method two, "a group of similar pictures" are either placed only in the training set or only in the test set. This can make the data of the training set and the test set as different as possible. It is also in line with our goal of solving "data leakage".

Here we place the download address of the NIST16 data set filtered by method 12xxxxxxxxxxxxxxxx，you can **DOWNLOAD** it through the link above.

Files in the ZIP are organized as follows:

```python
|——Tp        #Tampered images
|——Gt        #Ground-truth images
```



## A brief introduction to our definition of similarity

### Consider similar situations

1. The pictures and masks are very similar:

   

2. There is only a small amount of displacement in the tampered area, and the overall "pattern" is consistent.

   

3. For the same tampered area, only tamper in different ways

   

4. The mask looks different, but the tampering pattern of the original image is almost exactly the same

   

5. In a similar position, something with a similar pattern is placed

   

### Consider different situations

1. Although the pictures are roughly the same, there are some significant outline differences

   

2. The images look almost identical, but the masks are completely different

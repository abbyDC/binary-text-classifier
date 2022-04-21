# TensorFlow 2 Binary Text Classifier
This contains the scripts and data needed to run the text classifier demo. The aim is to train a model which can identify whether a given text is in Tagalog or English.

This was used for the Google Solutions Challenge UP Diliman 2021: TensorFlow Workshop.

Accompanying slides can be found here: [Slides Link](https://drive.google.com/file/d/1JiIHx35AXcpvhUgveyR6fbCtpDezI7Ph/view?usp=sharing)

Recorded talk can be viewed here (1:40:14 mark): [Tensorflow/Machine Learning Workshop](https://www.facebook.com/GDSCupdiliman/videos/181924306867950)\

## I. Dataset

A dataset was already prepared in `en_tl_data.csv`

## II. Training and Inference

Refer to `binary_text_classifier_demo.ipynb` for training and inference

## III. TensorFlow Serving

1. Make sure you've downloaded the trained model and take note of the path where it was saved

2. Run the ff on yout local machine

```
sudo docker pull tensorflow/serving
```
```
sudo docker run -t --rm -p 8501:8501 \
	-v "[path_to_model]:/models/tf_nnlm" \
	-e MODEL_NAME=tf_nnlm \
	--name tf-serving tensorflow/serving

e.g.
sudo docker run -t --rm -p 8501:8501 \
	-v "/home/abbydc/tf_nnlm:/models/tf_nnlm" \
	-e MODEL_NAME=tf_nnlm \
	--name tf-serving tensorflow/serving
```

to stop the tf-serving container:
```
sudo docker stop tf-serving
```

3.You may change the example in `text_classifier_tf_serving.py` and then run it with this command

```
python3 text_classifier_tf_serving.py
```

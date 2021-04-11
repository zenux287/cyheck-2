from imageai.Classification.Custom import CustomImageClassification
import os

execution_path = os.getcwd()

prediction = CustomImageClassification()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath("model_ex-008_acc-0.990866.h5")
prediction.setJsonPath("model_class.json")
prediction.loadModel(num_objects=2)
def pred(img):
    predictions, probabilities = prediction.classifyImage(img, result_count=2)
    pred.res = predictions[0]

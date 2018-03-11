python $HOME/TJHSST/12thGrade/Projects/OcuVision/tensorflow/take_image.py
python3 tensorflow/tensorflow/examples/label_image/label_image.py \
--graph=/Users/Sidhu/TJHSST/12thGrade/Projects/OcuVision/tensorflow/tensorflow/examples/label_image/output_graph.pb --labels=/Users/Sidhu/TJHSST/12thGrade/Projects/OcuVision/tensorflow/tensorflow/examples/label_image/output_labels.txt \
--input_layer=Mul \
--output_layer=final_result \
--input_mean=128 --input_std=128 \
--image=$HOME/TJHSST/12thGrade/Projects/OcuVision/tensorflow/image.jpg

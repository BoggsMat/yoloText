# yoloText
Modified version of yolo tensor flow from https://github.com/hizhangp/yolo_tensorflow designed to recognize text

Uses the YOLO object detection framework on simple synthetic text data. 

The training images can be generated using the imageGen.py script
	The script will generate images with words from small dictionary using random colors and fonts
	The script also generates annotation xmls in the style of PASCAL_VOC annotation 

To generate images: 
	python imageGen.py

	--num can be added to specify the number of images and annotations to be generated (default = 45): 
	python imageGen.py --num=45

To train the model: 
	python train.py

	--weights can be added to specify the location of the weights to use for training (default = "YOLO_small.ckpt"): 
	python train.py --weights=Save.ckpt

To test the model: 
	python test.py 

	--weights can be added to specify the location of the weights to use for testing (default = "YOLO_small.ckpt"): 
	python train.py --weights=Save.ckpt
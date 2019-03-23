# m223b
Bioengineering m223b: CT needle ID

* included packages:
    * pandas
    * numpy
    * scikit-learn
    * scikit-image
    * keras

* three different data folders:
	* 'data-full' for whole image analysis of entire dataset
	* 'data-culled' for masked image analysis
		* removed images from original dataset with any preprocessing 
		* does not include zoomed or cropped images
	* 'data' for k-fold cross-validation development
		* still under development

* codebase contains model development and image preprocessing scripts
	* image preprocessing:
		* loading images
		* separating images based on label
		* moving images to appropriate data folders
		* conversion from rgb to grayscale
		* image augmentation to increase sample size
		* includes lung segmentation pipeline
		* two different versions depending on application:
			* 'fullset' for images in 'data-full' folder
			* 'masked' for images in 'data-culled' folder
				* includes lung segmentation pipeline
	* models includes development space for machine learning models:
		* VGG16
		* ResNet50
		* ResNet16
		* VGG16 with k-fold cross-validation attempts



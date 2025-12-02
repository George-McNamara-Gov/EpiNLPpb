## [1.1.0](https://github.com/andreasonny83/twilio-remote-cli/compare/v0.0.1...v0.0.2) (02-12-2025)

> This update improves the implementation of data pre-processing and expands the machine learning techniques available. Data import and pre-processing are now implemented with pandas DataFrames instead of Lists. This has changed the format of some NLP constructor arguments as detailed below. New machine learning techniques have been made available to assist in handling imbalanced training data and improving performance. New techniques include under- and over-sampling of training data, regularisation of classifiers, class weighting, and ensemble learning methods.

### Upgrade Steps
Update dependencies by running...
```
pip install -r requirements.txt
```
  OR
```
pip install --proxy http://<USERNAME>:<PASSWORD>@<PROXY>:<PORT> --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```
  ...from the EpiNLPpb directory.

### Breaking Changes
* The 'fileType' keyword argument in the NLP object constructor has been removed. File type can now be infered from the file path(s) provided.
* The 'minAge' and 'maxAge' keyword arguments in the NLP object constructor have been replaced by an 'ageBounds' keyword argument which is a tuple of integers with format (minAge, maxAge).
* The 'minYear' and 'maxYear' keyword arguments in the NLP object constructor have been replaced by a 'yearBounds' keyword argument which is a tuple of integers with format (minYear, maxYear).
* The 'sex' keyword argument in the NLP object constructor was specified by a string, 'ALL', 'MALE' or 'FEMALE', in version 1.0.0. It is now specified by an integer, 0 for 'ALL', 1 for 'MALE', or 2 for 'FEMALE', in version 1.1.0.
* The 'trainPosPercent' and 'testPosPercent' keyword arguments in the NLP object constructor have been removed.
* The macLearnInput constructor parameter has changed from a list to a dictionary. For example, to specify a Support Vector Machine using a sigmoid kernel with a gamma value of 0.1 and an r value of 2.5 in version 1.0.0, macLearnInput would be given by...
```
macLearnInput = [
  'SIGMOID',
  0.1,
  2.5
]
```
  In version 1.1.0 to specify the same ML model, macLearnInput would be given by...
```
macLearnInput= {
  'kernel' : 'sigmoid',
  'gamma' : 0.1,
  'r' : 2.5
}
```
* When using 'DECISIONTREE' for mlAlgType, the previous valid inputs for 'impurity' were 'GINI', 'ENTROPY' and 'LOGLOSS'. The valid inputs for 'impurity' are now 'gini', 'entropy' and 'log_loss'.
* When using 'SVMACHINE' for mlAlgType, the previous valid inputs for 'kernel' were 'LINEAR', 'SIGMOID', 'POLYNOMIAL', and 'RBF'. The valid inputs for 'kernel' are now 'linear', 'sigmoid', 'poly', and 'rbf'.
* The approximateComplexities() method has been removed from the NLP object.

### New Features
* All ML models can now have class weights specified through the macLearnInput dictionary. The 'class_weight' key in the macLearnInput dictionary should have a dictionary as its value with weights associated with classes in the form {class_label: weight} as in [Sci-Kit Learn](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html). For example, to specify a Decision Tree using the gini impurity measure with a weight of 0.8 for class label 0 and a weight of 1.2 for class label 1, macLearnInput would be given by...
```
macLearnInput= {
  'impurity' : 'gini',
  'class_weight' : {
    0 : 0.8,
    1 : 1.2
  }
}
```
* Additional hyper-parameters can be provided to the Decision Tree ML model through the macLearnInput dictionary. Users can now specify 'max_depth' and 'min_samples_split' as in [Sci-Kit Learn](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html). For example, to specify a Decision Tree using the gini impurity measure with a maximum depth of 50 and the minimum samples required for a split being 20, macLearnInput would be given by...
```
macLearnInput= {
  'impurity' : 'gini',
  'max_depth' : 50,
  'min-samples_split' : 20
}
```
* An additional hyper-parameter can be provided to the Support Vector Machine ML model through the macLearnInput dictionary. Users can now specify the regularisation parameter 'C' as in [Sci-Kit Learn](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html). For example, to specify a Support Vector Machine using a radial basis function kernel with a gamma value of 0.1 and a C value of 10, macLearnInput would be given by...
```
macLearnInput= {
  'kernel' : 'rbf',
  'gamma' : 0.1,
  'C' : 10
}
```
* Two new ML model types have been added. The mlAlgType constructor parameter has additional valid inputs 'RANDOMFOREST' and 'RUSBOOST'. Both of these models require 'impurity' and 'ratio' values to be specified in the macLearnInput dictionary. These ensemble methods utilise Decision Trees as their base classifiers. Hence the macLearnInput dictionary can also include 'max_depth', 'min_samples_split', and 'class_weight' keys. The number of estimators to use in the ensemble can be specified by the 'n_estimators' key in the macLearnInput dictionary with any integer value. Additionally, for an mlAlgType of 'RUSBOOST' a learning rate can be specified through the 'learning_rate' key in the macLearnInput dictionary with any positive float value. For example, to specify an Random Under-Sampling Gradient Boosted model using the entropy impurity measure with under-sampling to achieve a minority to majority class ratio 0.6, 100 estimators, a learning rate of 0.01 and a maximum depth of 30, macLearnInput would be given by...
```
macLearnInput= {
  'impurity' : 'entropy',
  'ratio' : 0.6,
  'n_estimators' : 100,
  'learning_rate' : 0.01,
  'max_depth' : 30
}
```
* Over-sampling of training data can now be utilised when training ML models. To utilise over-sampling, provide the NLP constructor with a keyword argument called 'overSamplesOps'. The value for this argument should be a dictionary with a 'method' key and a 'ratio' key. Valid values for the 'method' key are 'SMOTE', 'BorderSMOTE' and 'ADASYN'. Any number between 0 and 1 is a valid value for the 'ratio' key. Additional keys can be provided for further customisation. See the overSample() method in package/mlearn/mlearn.py for details. For example, to over-sample the training data to achieve a minority to majority class ratio of 0.7 using the SMOTE method, overSampleOps would be given by...
```
overSampleOps= {
  'method' : 'SMOTE',
  'ratio' : 0.7
}
```
* Under-sampling of training data can now be implemented when training ML models. To utilise under-sampling, provide the NLP constructor with a keyword argument called 'underSampleOps'. The value for this argument should be a dictionary containing a 'method' key. Valid values for the 'method' key are 'RandomUnder', 'Tomek', 'ClusterCentroid' and 'NCL'. Additional keys can be provided for further customisation. See the underSample() method in package/mlearn/mlearn.py for details. For example, to under-sample using the Neighbourhood Cleaning Rule considering the 5 nearest neighbours, underSampleOps would be given by...
```
underSampleOps= {
  'method' : 'NCL',
  'n_neighbours' : 5
}
```
* NLP programs can now be trained and evaluated in a cross-validated fashion. Once an NLP object is created it can be trained an evaluated using cross-validation by using the crossValidate() method. The crossValidate() method accepts one argument which is an integer to specify the number of folds.

### Performance Improvements
* The Importer package now stores data in pandas DataFrames rather than Lists.

### Other Changes
* The incomplete Graphical User Interface package has been removed until it is finished.
* The complexity approximation funcitonality in the evaluate package has been removed.

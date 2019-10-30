package tp6;

import java.io.File;
import java.io.IOException;
import java.util.Random;

import weka.classifiers.Classifier;
import weka.classifiers.bayes.NaiveBayesMultinomial;
import weka.classifiers.evaluation.Evaluation;
import weka.classifiers.functions.SMO;
import weka.classifiers.trees.J48;
import weka.core.Instances;
import weka.core.converters.CSVLoader;

public class TP6 {
	
	public static void main(String[] args) throws Exception {
		
		CSVLoader loader = new CSVLoader();
		
		File train = new File(System.getProperty("user.home")+"/Bureau/M1/RI/TP6/nobel.train.csv");
		File test = new File(System.getProperty("user.home")+"/Bureau/M1/RI/TP6/nobel.test.csv");
		
		Instances trainData, testData;

		loader.setFile(train); trainData = loader.getDataSet();		
		loader.setFile(test); testData = loader.getDataSet();
		
		trainData.setClassIndex(trainData.numAttributes()-1);
		testData.setClassIndex(testData.numAttributes()-1);
		
		J48 j48 = new J48();
		j48.setOptions(new String[] {"-R"});
		
		NaiveBayesMultinomial naiveBayes = new NaiveBayesMultinomial();
		
		SMO svm = new SMO();
		
		Evaluation evaluation = new Evaluation(trainData);

		/* Avec la cross validation*/
		//evaluation.crossValidateModel(j48, trainData, 10, new Random(1));
		//evaluation.crossValidateModel(naiveBayes, trainData, 10, new Random(1));
		//evaluation.crossValidateModel(svm, trainData, 10, new Random(1));
		
		//System.out.println(evaluation.toSummaryString());
		
		/* Avec le jeu de test */
		//j48.buildClassifier(trainData);
		//evaluation.evaluateModel(j48, testData);
		
		//naiveBayes.buildClassifier(trainData);
		//evaluation.evaluateModel(naiveBayes, testData);
		
		svm.buildClassifier(trainData);
		evaluation.evaluateModel(svm, testData);
		
		System.out.println(evaluation.toSummaryString());

	}

}

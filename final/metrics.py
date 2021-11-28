import numpy as np

def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''

    precision = np.sum(np.logical_and(prediction == ground_truth, prediction == True)) / np.sum(prediction)
    recall = np.sum(np.logical_and(prediction == ground_truth, prediction == True)) / np.sum(ground_truth)
    accuracy = np.sum(prediction == ground_truth) / len(prediction)
    f1 = 2 * precision*recall/(precision + recall)
    
    #Precision = TP/(TP+FP)
    #Sensitivity(recall)=TP/(TP+FN)
    #Specificity=TN/(TN+FP)
    #Accuracy=(TP+TN)/(TP+TN+FP+FN)

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    # https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9
    
    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    print(prediction, ground_truth)
    return np.sum(prediction == ground_truth) / len(prediction)

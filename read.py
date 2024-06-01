import pandas as pd

# Read the CSV file
data = pd.read_csv("data.csv")


# Define function to calculate TP, TN, FP, FN
def calculate_metrics(y_act, y_pred):
    TP = sum((y_act == 1) & (y_pred >= 0.55))
    TN = sum((y_act == 0) & (y_pred < 0.55))
    FP = sum((y_act == 0) & (y_pred >= 0.55))
    FN = sum((y_act == 1) & (y_pred < 0.55))
    return TP, TN, FP, FN


# Calculate metrics for y_pred_random_forest
TP_rf, TN_rf, FP_rf, FN_rf = calculate_metrics(
    data["y_act"], data["y_pred_random_forest"]
)

# Calculate metrics for y_pred_logistic
TP_log, TN_log, FP_log, FN_log = calculate_metrics(
    data["y_act"], data["y_pred_logistic"]
)

# Print the results
print("Random Forest Metrics:")
print("TP:", TP_rf)
print("TN:", TN_rf)
print("FP:", FP_rf)
print("FN:", FN_rf)

print("\nLogistic Regression Metrics:")
print("TP:", TP_log)
print("TN:", TN_log)
print("FP:", FP_log)
print("FN:", FN_log)


# Calculate Accuracy
def calculate_accuracy(TP, TN, FP, FN):
    return (TP + TN) / (TP + TN + FP + FN)


# Calculate Recall
def calculate_recall(TP, FN):
    return TP / (TP + FN)


# Calculate Precision
def calculate_precision(TP, FP):
    return TP / (TP + FP)


# Calculate F1 Score
def calculate_f1_score(precision, recall):
    return 2 * (precision * recall) / (precision + recall)


# Calculate metrics for Random Forest
accuracy_rf = calculate_accuracy(TP_rf, TN_rf, FP_rf, FN_rf)
recall_rf = calculate_recall(TP_rf, FN_rf)
precision_rf = calculate_precision(TP_rf, FP_rf)
f1_score_rf = calculate_f1_score(precision_rf, recall_rf)

# Calculate metrics for Logistic Regression
accuracy_log = calculate_accuracy(TP_log, TN_log, FP_log, FN_log)
recall_log = calculate_recall(TP_log, FN_log)
precision_log = calculate_precision(TP_log, FP_log)
f1_score_log = calculate_f1_score(precision_log, recall_log)

# Print results
print("\nRandom Forest Metrics:")
print("Accuracy:", accuracy_rf)
print("Recall:", recall_rf)
print("Precision:", precision_rf)
print("F1 Score:", f1_score_rf)

print("\nLogistic Regression Metrics:")
print("Accuracy:", accuracy_log)
print("Recall:", recall_log)
print("Precision:", precision_log)
print("F1 Score:", f1_score_log)

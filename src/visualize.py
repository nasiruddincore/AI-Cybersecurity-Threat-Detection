import matplotlib.pyplot as plt

def plot_results(y_test, y_pred):
    plt.scatter(range(len(y_test)), y_test, label="Actual")
    plt.scatter(range(len(y_pred)), y_pred, label="Predicted")
    plt.legend()
    plt.title("Prediction vs Actual")
    plt.show()
from src.data_preprocessing import load_data, preprocess_data
from src.model import train_model

def main():
    df = load_data("data/kdd.csv")
    df = preprocess_data(df)
    train_model(df)

if __name__ == "__main__":
    main()
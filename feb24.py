import pandas as pd
import seaborn as sns


def main():
    try:
        df = pd.read_csv("data.csv")
        source = "data.csv"
    except FileNotFoundError:
        df = sns.load_dataset("titanic")
        source = "seaborn titanic"

    print(f"Dataset source: {source}")
    print("Top rows:")
    print(df.head(5))

    numeric = df.select_dtypes(include="number")
    if numeric.empty:
        print("No numeric columns found.")
        max_col = None
    else:
        max_col = numeric.max().idxmax()
        print(f"Column with highest single value: {max_col}")
        print(f"Highest value: {numeric[max_col].max()}")

    missing = df.isna().sum()
    print("Missing values per column:")
    print(missing[missing > 0])
    print(f"Total missing values: {missing.sum()}")

    insights = []
    insights.append(f"Dataset has {df.shape[0]} rows and {df.shape[1]} columns.")
    if missing.sum() > 0:
        insights.append(f"Most missing data is in '{missing.idxmax()}' with {missing.max()} missing values.")
    else:
        insights.append("No missing values found.")

    if not numeric.empty:
        insights.append(f"Numeric columns cover {len(numeric.columns)} of {len(df.columns)} total columns.")
        insights.append(f"Highest value appears in '{max_col}' column.")
    else:
        insights.append("No numeric columns are available to identify a highest value column.")

    top_nonnull = df.notna().sum().sort_values(ascending=False).head(3)
    insights.append(f"Most complete columns: {', '.join(map(str, top_nonnull.index))}.")

    print("\nInsights:")
    for i, insight in enumerate(insights, 1):
        print(f"Insight {i}: {insight}")


if __name__ == "__main__":
    main()

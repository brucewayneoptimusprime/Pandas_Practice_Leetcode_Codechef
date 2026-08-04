from pandas.api.types import is_numeric_dtype

for column in df.columns:

    if is_numeric_dtype(df[column]):
        df[column] = df[column].fillna(
            df[column].mean()
        )

    else:
        df[column] = df[column].fillna(
            df[column].mode().iloc[0]
        )

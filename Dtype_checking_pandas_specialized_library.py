from pandas.api.types import (
    is_numeric_dtype,
    is_integer_dtype,
    is_float_dtype,
    is_bool_dtype,
    is_string_dtype,
    is_object_dtype,
    is_datetime64_any_dtype,
    is_timedelta64_dtype
)

for column in df.columns:

    if is_numeric_dtype(df[column]):
        df[column] = df[column].fillna(
            df[column].mean()
        )

    else:
        df[column] = df[column].fillna(
            df[column].mode().iloc[0]
        )

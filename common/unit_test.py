import pandas as pd
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation, CanConvertValidation, MatchesPatternValidation, InRangeValidation, InListValidation, CustomElementValidation
import numpy as np
null_validation = [CustomElementValidation(lambda d: d is not np.nan, 'this field cannot be null')]

schema = Schema([
    Column('NAME',null_validation),
    Column('ADDRESS'),
    Column('CITY'),
    Column('STATE'),
    Column('ZIP'),
    Column('CENSUS_CODE'),
    Column('LATITUDE'),
    Column('LONGITUDE'),
    Column('LOCATION_TY')
])
def check_column_matches_schema(df,unit_schema=schema) -> None:
    unit_schema = schema.get_column_names()
    input_data_col = list(df.columns)
    bool = unit_schema == input_data_col
    assert bool == True, f"Schema not matching expectations."

def validate_column_rules(df,unit_schema=schema) -> None:
    unit_schema = schema
    errors = schema.validate(df)
    if (len(errors) > 0):
        for error in errors:
            print(error)
        return False
    return True
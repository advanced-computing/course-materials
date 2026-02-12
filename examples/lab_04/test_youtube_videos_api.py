import pandas as pd 
from flask_lab_example import filter_by_value
from flask_lab_example import apply_limit_offset
from flask_lab_example import convert_to_format
import io

def get_test_df():
    data = {
        'Rank': [1,2,3,4,5],
        'Video': ['Baby Shark Dance','Despacito','Shape of You','See You Again','Masha and the Bear'],
        'VideoViews': [9.04,7.46,5.46,5.26,4.45],
        'Likes' : [22.7,23.3,27.3,34.4,19.3],
        'Dislikes' : [11.0,2.3,0.7,0.4,1.2],
        'Category': ['Music','Music','Music','Music','Entertainment'],
        'Published': [1800,2017,2017,2015,2016]
    }
    df = pd.DataFrame(data)
    return df

def test_filter_by_value():
    df = get_test_df()
    result = filter_by_value(df,'Rank',1)
    expected_output = pd.DataFrame({
        'Rank': [1],
        'Video': ['Baby Shark Dance'],
        'VideoViews': [9.04],
        'Likes' : [22.7],
        'Dislikes' : [11.0],
        'Category': ['Music'],
        'Published': [1800]
    })
    assert result.equals(expected_output)

def test_apply_limit_offset():
    df = get_test_df()
    result = apply_limit_offset(df,2,1).reset_index(drop=True)
    expected_output = pd.DataFrame({
        'Rank': [2,3],
        'Video' : ['Despacito','Shape of You'],
        'VideoViews': [7.46,5.46],
        'Likes' : [23.3,27.3],
        'Dislikes' : [2.3,0.7],
        'Category': ['Music','Music'],
        'Published': [2017,2017]
    })
    assert result.equals(expected_output)

def test_convert_to_format_csv():
    df = get_test_df().head(2)
    result = convert_to_format(df,'csv')

    # we wil convert back to dataframe from the csv and then compare
    result = pd.read_csv(io.StringIO(result), sep=",")
    expected_output = df
    assert result.equals(expected_output)

def test_convert_to_format_json():
    df = get_test_df().head(2)
    result = convert_to_format(df,'json')
    
    # we wil convert back to dataframe from the json and then compare
    result = pd.read_json(io.StringIO(result))
    expected_output = df
    assert result.equals(expected_output)

def test_convert_to_format_invalid():
    df = get_test_df().head(2)
    result = convert_to_format(df,'invalid')
    
    expected_output = "Invalid format"
    assert result == expected_output

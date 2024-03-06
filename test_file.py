import subprocess


def test_case_0():
    input_data = "5.2 3.4"
    expected_result = "8.6"
    cast_type = type(expected_result)

    result = subprocess.run(
        "./main",
        input=input_data.encode(),
        stdout=subprocess.PIPE,  
    )
    assert cast_type(result.stdout.decode()) == expected_result
    
def test_case_1():
    input_data = "10.2 5.3"
    expected_result = "15.5"
    cast_type = type(expected_result)

    result = subprocess.run(
        "./main",
        input=input_data.encode(),
        stdout=subprocess.PIPE,  
    )
    assert cast_type(result.stdout.decode()) == expected_result
    
def test_case_2():
    input_data = "0 0"
    expected_result = "0"
    cast_type = type(expected_result)

    result = subprocess.run(
        "./main",
        input=input_data.encode(),
        stdout=subprocess.PIPE,  
    )
    assert cast_type(result.stdout.decode()) == expected_result
    
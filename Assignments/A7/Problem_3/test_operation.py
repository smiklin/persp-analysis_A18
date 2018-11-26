import pytest
import operation

def test_operation():
    assert operation.operate(4,2,'+') == 6, "addition"
    assert operation.operate(4,2,'-') == 2, "subtraction"
    assert operation.operate(4,2,'*') == 8, "multiplication"
    assert operation.operate(4,2,'/') == 2, "integer division"
    assert operation.operate(5,2,'/') == 2.5, "float division"
    with pytest.raises(ZeroDivisionError) as excinfo:
        operation.operate(a=4, b=0, oper = '/')
    assert excinfo.value.args[0] == "division by zero is undefined"
    with pytest.raises(ValueError) as excinfo:
        operation.operate(a=4, b=0, oper = 'n')
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"

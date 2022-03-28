import calc

def test_areaofrectangle():
    x = 20
    y = 10
    result = calc.areaofrectangle(x,y)
    assert x*y==result
def test_perimeterofrectangle():
    x = 10
    y = 5
    result = calc.primeterofrectangle(x,y)
    assert 2*(x+y)==result
def test_areaofsquare():
    x = 20
    result= calc.areaofsquare(x)
    assert x*x==result


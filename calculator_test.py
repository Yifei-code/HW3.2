import calculator

def test_add():
    assert calculator.add(1,6) == "1 + 6 = 7"
    assert calculator.add(5,7) == "5 + 7 = 12"
    assert calculator.add(100,234) == "100 + 234 = 334"
    
def test_sub():
    assert calculator.subtract(6,1) == "6 - 1 = 5"
    assert calculator.subtract(2,17) == "2 - 17 = -15"
    
    
if __name__ == "__main__":
    test_add()
    test_sub()
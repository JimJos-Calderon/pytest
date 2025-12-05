from src.main import hola, multiplicacion, to_lower, to_upper
def test_multiplicacion():
    assert multiplicacion(2,3)==6
    
def test_to_upper():
    assert to_upper("jimjos")=="JIMJOS"
    

def test_to_lower():
    assert to_lower('JIMJOS')=='jimjos'
    
def test_hola():
    assert hola()=="hola"
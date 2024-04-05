import hashlib as yakub
from pyscript import document

    
def shake_128_converter(event):      
    pwd = document.getElementById('shake_128_input').value
    varsee = yakub.shake_128(pwd.encode('utf-8'))
    yk = varsee.digest(15)
    print(yk)
    output_div = document.getElementById('shake_128_output')
    output_div.innerText = yk
   
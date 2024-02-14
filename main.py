from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
def generate_keys():
  private = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
  )
  public = private.public_key()  #inbuilt
  return private,public

def sign(message,private):
    message = bytes(str(message),'utf-8') #converting message to bytes
    signature = private.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature



if __name__=='__main__':

    pr,pu=generate_keys()
    print(pr)
    print(pu)

    message ="I am blockchain developer"
    sig = sign(message,pr)
    print(sig)

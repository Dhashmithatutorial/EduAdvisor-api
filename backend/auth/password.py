from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):
    print("=" * 50)
    print("PASSWORD:", repr(password))
    print("TYPE:", type(password))
    print("LENGTH:", len(password))
    print("=" * 50)

    return pwd_context.hash(password)

def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
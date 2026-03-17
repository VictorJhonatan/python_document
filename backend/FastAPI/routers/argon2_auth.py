"""
Argon2 ganó la Password Hashing 
Competition en 2015. Sus ventajas 
principales son que puede usar
 memoria RAM además de CPU 
 (lo que lo hace resistente a 
 ataques con hardware especializado 
 como GPUs/ASICs), tiene tres variantes 
 (Argon2i, Argon2d, Argon2id — la recomendada), 
 y permite configurar memoria, iteraciones 
 y paralelismo por separado."""

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt                          # pip install pyjwt   (antes: python-jose)
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash     # pip install "pwdlib[argon2]"
from pwdlib.hashers.argon2 import Argon2Hasher
from datetime import datetime, timedelta, timezone


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1
SECRET = "be574619c9a15b1e65580155d8a79ec67606d837bd3c77795eb8e8cc122e07ba"

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# ── Argon2id con pwdlib ──────────────────────────────────────────────────────
# Argon2Hasher usa Argon2id por defecto (la variante más recomendada).
# Parámetros opcionales que puedes ajustar:
#   time_cost      → iteraciones de CPU   (default: 3)
#   memory_cost    → RAM en KiB           (default: 65536 = 64 MB)  ← ventaja vs bcrypt
#   parallelism    → hilos paralelos      (default: 4)
pwd_hasher = PasswordHash([Argon2Hasher()])
# Para generar un hash nuevo:  pwd_hasher.hash("mi_contraseña")
# Para verificar:              pwd_hasher.verify("texto_plano", "hash_almacenado")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserInDB(User):
    password: str


# ── Base de datos simulada ───────────────────────────────────────────────────
# Hashes generados con:  pwd_hasher.hash("1234")  (Argon2id)
user_db = {
    "victor": {
        "username": "victor",
        "full_name": "Victor Robles",
        "email": "victor@victor.com",
        "disabled": False,
        "password": pwd_hasher.hash("1234"),   # en producción ya vendrían hasheados
    },
    "analu": {
        "username": "ana",
        "full_name": "Ana García",
        "email": "ana@ana.com",
        "disabled": True,
        "password": pwd_hasher.hash("1234"),
    },
    "luis": {
        "username": "luis",
        "full_name": "Luis Martínez",
        "email": "luis@luis.com",
        "disabled": False,
        "password": pwd_hasher.hash("1234"),
    },
}


# ── Helpers ──────────────────────────────────────────────────────────────────
def search_user(username: str):
    if username in user_db:
        return UserInDB(**user_db[username])

def search_users(username: str):
    if username in user_db:
        return User(**user_db[username])


# ── Dependencias JWT ─────────────────────────────────────────────────────────
async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # PyJWT usa jwt.decode directamente (sin algorithms como lista es válido también)
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise exception
    except InvalidTokenError:       # reemplaza JWTError de python-jose
        raise exception

    return search_users(username)


async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo",
        )
    return user


# ── Rutas ────────────────────────────────────────────────────────────────────
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    if form.username not in user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto",
        )

    user = search_user(form.username)

    # ✅ Verificación con Argon2 (pwdlib)
    if not pwd_hasher.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Contraseña incorrecta",
        )

    # ✅ PyJWT recomienda timezone-aware datetime (evita DeprecationWarning)
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode({"sub": user.username, "exp": expire}, SECRET, algorithm=ALGORITHM)

    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
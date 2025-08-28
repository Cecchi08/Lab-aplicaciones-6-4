const msj = prompt("Ingrese el mensaje a encriptar:");
let encrypted_msj = "";

const diccionarioIndiceNumero = new Map();
const diccionarioNumeroIndice = new Map();

for (let i = 1; i <= 26; i++) {
  diccionarioIndiceNumero.set(i, String.fromCharCode(i + 96));    
  diccionarioIndiceNumero.set(i + 26, String.fromCharCode(i + 64));

  diccionarioNumeroIndice.set(String.fromCharCode(i + 96), i);   
  diccionarioNumeroIndice.set(String.fromCharCode(i + 64), i + 26); 
}

for (let i = 0; i < msj.length; i++) {
  const c = msj[i];

  if (c !== " ") {
    let indiceActual = diccionarioNumeroIndice.get(c);

    if (indiceActual === 24) indiceActual = 1;
    else if (indiceActual === 25) indiceActual = 2;
    else if (indiceActual === 26) indiceActual = 3;
    else if (indiceActual === 50) indiceActual = 27;
    else if (indiceActual === 51) indiceActual = 28;
    else if (indiceActual === 52) indiceActual = 29;

    let indiceEncriptado = indiceActual + 3;
    if (indiceEncriptado > 52) {
      indiceEncriptado -= 52; 
    }

    encrypted_msj += diccionarioIndiceNumero.get(indiceEncriptado);
  }
}

alert("El mensaje encriptado es: " + encrypted_msj);

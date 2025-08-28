#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    string msj;
    cout << "Ingrese el mensaje a encriptar: ";
    getline(cin, msj); 
    string encrypted_msj = "";

    unordered_map<int, char> diccionarioIndiceNumero;
    unordered_map<char, int> diccionarioNumeroIndice;

    for (int i = 1; i <= 26; ++i) {
        diccionarioIndiceNumero[i] = char(i + 96);   
        diccionarioIndiceNumero[i + 26] = char(i + 64); 
        
        diccionarioNumeroIndice[char(i + 96)] = i;  
        diccionarioNumeroIndice[char(i + 64)] = i + 26; 
    }

    for (char c : msj) {
        if (c != ' ') {
            int indiceActual = diccionarioNumeroIndice[c];

            if (indiceActual == 24) indiceActual = 1;
            else if (indiceActual == 25) indiceActual = 2;
            else if (indiceActual == 26) indiceActual = 3;
            else if (indiceActual == 50) indiceActual = 27;
            else if (indiceActual == 51) indiceActual = 28;
            else if (indiceActual == 52) indiceActual = 29;

            int indiceEncriptado = indiceActual + 3;
            if (indiceEncriptado > 52) {
                indiceEncriptado -= 52; 
            }

            encrypted_msj += diccionarioIndiceNumero[indiceEncriptado];
        }
    }
    cout << "El mensaje encriptado es: " << encrypted_msj << endl;

    return 0;
}

#include <iostream>
#include <string>

using namespace std;

int main() {
    string username, password;
    cout << "Kerem adja meg a felhasznalonevet: ";
    cin >> username;
    cout << "Kerem adja meg a jelszot: ";
    cin >> password;
    if (password == "titkosjelszo") {
        cout << "Sikeres belepes. Udvozoljuk, " << username << "!" << endl;
    } else {
        cout << "Hibas jelszo. A belépés nem sikerült." << endl;
    }
    return 0;
}

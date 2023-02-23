#include "iostream"
#include "string"

using namespace std;


struct Fecha{
    int dia;
    int mes;
    int anio;
};


string fechaToString(Fecha f)
{
    string s = to_string(f.dia)+"/"+to_string(f.mes)+"/"+to_string(f.anio);
    return s;
}

Fecha fechaCreate(int d, int m, int a)
{
    Fecha f;

    f.dia = d;
    f.mes = m;
    f.anio = a;

    return f;
}

int fechaCmp(Fecha f1, Fecha f2)
{
    if (f1.anio == f2.anio)
    {
        if(f1.mes == f2.mes)
        {
            return f1.dia - f2.dia;
        }
        return f1.mes - f2.mes;
    }
    return f1.anio - f2.anio;
}

int main()
{
    Fecha f1, f2;

    f1.dia = 1;
    f1.mes = 2;
    f1.anio = 2023;

    f2 = fechaCreate(2,3,2024);

    cout << f1.dia << "/" << f1.mes << "/" << f1.anio << endl;
    cout << fechaToString(f1) << endl;
    cout << fechaToString(f2) << endl;

    cout << fechaCmp(f1,f2) << endl;

    return 0;
}
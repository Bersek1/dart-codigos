import 'dart:io';

void main() {
  List<String> nombres = [];
  List<String> rut = [];

  for (int i = 0; i < 3; i++) {
    print("Ingrese el nombre de la persona ${i + 1}: ");
    String nombre = stdin.readLineSync()!;
    nombres.add(nombre);

    print("Ingrese el RUT de la persona ${i + 1}: ");
    String rutPersona = stdin.readLineSync()!;
    rut.add(rutPersona);
  }

  print("\nNombres ingresados:");
  print(nombres);

  print("\nRUT ingresados:");
  print(rut);

  nombres.sort(); te
  rut.sort(); 

  print("\nNombres ordenados alfabéticamente:");
  print(nombres);

  print("\nRUT ordenados ascendentemente:");
  print(rut);
}

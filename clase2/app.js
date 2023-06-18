// let a = 7;
// let b = '7';

// //Mismo tipo y valor
// if(a === b)
//     console.log("Son iguales");
// else
//     console.log('No son iguales');

//     //mismo valor
// if(a == b)
//     console.log("Son iguales");
// else
//     console.log('No son iguales');

// let edad = prompt('Ingrese su edad');

// if(edad >= 18)
//     console.log('Es mayor de edad');
// else 
//     console.log('No es mayor de edad');

let nota = parseInt(prompt('Ingrese su nota'));
console.log(typeof(nota));

switch(nota){
    case 8:
        console.log("Excelente");
        break;
    case 7: 
        console.log('Muy bien');
        break;
    case 3:
        console.log('Desaprobado');
    default:
        console.log('No se ingreso nota');

}


// let expr = prompt('Ingrese una fruta');

// switch (expr) {
//     case 'Naranjas':
//       console.log('El kilogramo de naranjas cuesta $0.59.');
//       break;
//     case 'Manzanas':
//       console.log('El kilogramo de manzanas cuesta $0.32.');
//       break;
//     case 'Platanos':
//       console.log('El kilogramo de platanos cuesta $0.48.');
//       break;
//     case 'Cerezas':
//       console.log('El kilogramo de cerezas cuesta $3.00.');
//       break;
//     case 'Mangos':
//     case 'Papayas':
//       console.log('El kilogramo de mangos y papayas cuesta $2.79.');
//       break;
//     default:
//       console.log('Lo lamentamos, por el momento no disponemos de ' + expr + '.');
//   }
  
//   if(expr == 'Naranjas')
//     console.log('precio');
//   else 
//      if(expr == 'Pera')
//         console.log('precio pera');
//      else
//         if(expr == 'Manzana')
//             console.log('Precio de manzana');



// if (nota < 4) {
//     calificacion = "suspendido";
//     } else {
//     calificacion = "aprobado";
//     }
// console.log("Estoy", calificacion)  

// let calificacion = nota < 4 ? "suspendido" : "aprobado";
// console.log("Estoy", calificacion);


let edad = 14;
let altura = 1.65;


if(edad > 18 && altura > 1.70)
    //SI O SI tiene que cumpplir las 2 condiciones
    console.log('Se puede subir al juego');
else
    console.log('No se puede');

if(edad > 18 || altura > 1.60){
    //Se tiene que cumplir una de las 2 condiciones
    console.log('Puede ingresar pero con un adulto');
}
else{
    console.log('No se puede');
}



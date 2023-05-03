// // let persona2 = {
// //     nombre: "Juan",
// //     edad: 30,
// //     dni: "3354897811",
// //     direccion: "Calle False 123",

// //     //metodos
// //     saludar: function(){
// //         console.log(`Hola, mi nombre es ${this.nombre} y tengo ${this.edad} años`);
// //     },
// //     domicilio: function(){
// //         return `Vivo en ${this.direccion}`;
// //     },
// //     anios: function(){
// //         // debugger;
// //        return this.edad;
// //     }
// // };



// // persona.saludar();
// // let domicilio = persona.domicilio();
// // console.log(domicilio);
// // //  debugger;
// // // console.log(persona.anios());

// // if( persona.anios() > 18)
// //     console.log("Es mayor de 18 años")
// // else
// //     console.log("No puedo ingresar por ser menor de edad")



// // let auto = {
// //     marca: "Chevrolet",
// //     modelo: "Chevy",
// //     patente: "XX123BV",
// //     anio: 1975,
// //     ruedas: 4,
// // }

// // //mi auto  objeto Generico
// // let miAuto = new Object()
// // miAuto.marca = "VW";
// // miAuto.modelo = "Gol",
// // miAuto.puertas = 4;
// // miAuto.ruedas = 4;
// // miAuto.airbags = 2;

// // console.log(persona.nombre);
// // console.log(persona.direccion)
// // console.log(auto.anio);
// // console.log(auto.marca);
// // console.log(auto.ruedas);

// let persona = {
//     nombre: '',
//     apellido: '',
//     edad: '',
//     //Obtener informacion del objeto
//     get nombreCompleto(){
//         return `nombre: ${this.nombre} apellido: ${this.apellido}` -->> Sin ``  "nombre: " + this.nombre + ' ' +  "apellido: " + this.apellido
//     },

//     get getEdad(){
//         debugger;
//         return this.edad;
//     },
//     //Para setear informacion
//     set nombreCompleto(nombre)
//         {    // Mario Luis  -->> partes[0] = Mario, partes[1]= Luis
//             let partes = nombre.split(' ');
//             this.nombre = partes[0];
//             this.apellido = partes[1];
//         },
//     set setEdad(num){
//         this.edad = num;
//     }
// }

// // persona.nombreCompleto = prompt("Ingrese su nombre Completo");
// persona.setEdad = parseInt(prompt("Ingrese su Edad"));
// debugger;
// // console.log(persona.nombreCompleto);
// console.log(persona.getEdad);
// // console.log(persona.nombre);
// // console.log(persona.apellido);


// class Auto{
//     constructor(modelo,anio,tranmision){
//         this.modelo = modelo,
//         this.anio = anio,
//         this.tranmision = tranmision
//     }
//     //GETTER

//     //Setters
// }

// let auto1 = new Auto("Chevy","1979","MT");
// let auto2 = new Auto("Falcon","2000","AT");

// console.log(auto1.anio);



let cadena = "   Esto es un objeto string    ";

console.log(cadena.length);
console.log(cadena.toLocaleUpperCase());;
console.log(cadena.indexOf("o"));
console.log(cadena.repeat(5));
console.log(cadena.split(' '));


console.log(Math.PI)
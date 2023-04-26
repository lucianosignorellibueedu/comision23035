// // // function nombre_funcion(){
// //     // codigo de la funcion
// // // }
// // // nombre_funcion()


// // // ----- FUNCIONES-----
// // function saludarSinParamentrosNiReturn(){
// //     let date = new Date();
// //     let hs = date.getHours();
// //     if( hs> 12)
// //         console.log("Buenas Tardes comision 23035!!");
// //     else
// //         console.log("Buenas días comision 23035!!");
// // }


// // function saludarSinParamentrosWithReturn(){
// //     let date = new Date();
// //     let hs = date.getHours();
// //     if( hs> 12)
// //        return "Buenas Tardes comision 23035!!";
// //     else
// //         return "Buenas días comision 23035!!";
// // }

// // function ingresarNum(){
// //     return parseInt(prompt("Ingrese un numero"));
// // }

// // function sumar(){
// //     let num1 = ingresarNum()
// //     let num2 = ingresarNum();
// //     console.log(num1 + num2);
// // }

// // function sumarConParametrosConReturn(a,b){
// //     return a + b;
// // }
// // function sumarConParametrosSinReturn(a,b){
// //     console.log( a + b);
// // }

// // function sumarConParametrosUnoOpcional(a,b=5){
// //     console.log( a + b);
// // }


// // // ----- FIN FUNCIONES-----

// // // sumar();
// // // saludar();

// // // let saludar = saludarSinParamentrosWithReturn();
// // console.log(saludarSinParamentrosWithReturn());

// // let sumar = sumarConParametrosConReturn(8,4)
// // console.log("sumarConParametrosConReturn",sumar);
// // sumarConParametrosSinReturn(12,6)
// // sumarConParametrosUnoOpcional(20);

// // // function sumar(){
// // //     let num1 = ingresarNum()
// // //     let num2 = ingresarNum();
// // //     console.log(num1 + num2);
// // // }

// // //nombreFuncion = (parm1,parm2) => Operacion Funcion
// // let sumar = (a,b) => a + b
// // console.log("funciones flecha => ",sumar(8,3));

// // let multiplicar = (a,b) => a * b;
// // console.log("funciones flecha => ",multiplicar(8,3));

// // let suma2 = () => {
// //     let num1 = ingresarNum();
// //     let num2 = ingresarNum();
// //     return num1 + num2;
// // }
// // console.log("funciones flecha => ",suma2());

// function getNombreScopeLocal(){
//     let nombre = prompt("ingrese nombre");
//     console.log(nombre);
//     console.log(nombre + "pepe");
//     console.log(nombre + "pepe" + "jorge");
//     nombre = "Alberto";
//     console.log(nombre)
// }
// // getNombreScopeLocal();



// function getNombreScopeGlobal(){
//     nombreGlobal = prompt("ingrese nombre");
//     console.log(nombreGlobal);
//     console.log(nombreGlobal + "pepe");
//     console.log(nombreGlobal + "pepe" + "jorge");
//     nombreGlobal = "Alberto";
//     console.log(nombreGlobal)
// // }

// // getNombreScopeGlobal()
// // let nombreGlobal = "Mario Luis";
// // console.log(nombreGlobal)
// // console.log(nombreGlobal)


// function saludar(nombre) {
//     alert('Hola ' + nombre)
// }
// function procesarEntradaUsuario(callback) {
//     let nombre = prompt('Por favor ingresa tu nombre.')
//     callback(nombre)
// }
// procesarEntradaUsuario(saludar)


function contador(){
    let cont = 0;
    return function(){
        cont++;
        console.log(cont);
    }
}

const incrementar = contador();
incrementar(); // 1
incrementar(); // 2
incrementar(); // 3
incrementar(); // 4
incrementar(); // 5

// Variables

let oficialCompra = document.querySelector('#oficialCompra')
let oficialVenta = document.querySelector('#oficialVenta')
let blueCompra = document.querySelector('#blueCompra')
let blueVenta = document.querySelector('#blueVenta')
let liqui = document.querySelector('#liqui')
let promCompra = document.querySelector('#promCompra')
let promVenta = document.querySelector('#promVenta')
let bolsa = document.querySelector('#bolsa')
let turista = document.querySelector('#turista')
let oficialVar = document.querySelector('#oficialVar')
let blueVar = document.querySelector('#blueVar')
let liquiVar = document.querySelector('#liquiVar')
let promVar = document.querySelector('#promVar')
let bolsaVar = document.querySelector('#bolsaVar')
let turistaVar = document.querySelector('#turistaVar')
let fecha = document.querySelectorAll('.fecha')
let dia = new Date()

// Código

init()

addingDate()

// Funciones

function init(){

    fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales').then(data => data.json()).then(data => {

        for(i = 0; i < data.length; i++){

            if(data[i].casa.nombre == "Dolar Oficial"){
                oficialCompra.textContent = `$ ${data[i].casa.compra}`
                oficialVenta.textContent = `$ ${data[i].casa.venta}`
                if(parseFloat(data[i].casa.variacion.replace(/,/g, '.')) > 0){
                    oficialVar.innerHTML = `↑ VARIACION +${data[i].casa.variacion}%`
                }
                else if(parseFloat(data[i].casa.variacion.replace(/,/g, '.')) < 0){
                    oficialVar.innerHTML = `↓ VARIACION ${data[i].casa.variacion}%`
                }
                else{
                    oficialVar.innerHTML = `= VARIACION ${data[i].casa.variacion}%`
                }
                
            }

            else if(data[i].casa.nombre == "Dolar Blue"){
                blueCompra.textContent = `$ ${data[i].casa.compra}`
                blueVenta.textContent = `$ ${data[i].casa.venta}`
                if(parseFloat(data[i].casa.variacion.replace(/,/g, '.')) > 0){
                    blueVar.innerHTML = `↑ VARIACION +${data[i].casa.variacion}%`
                }
                else if(parseFloat(data[i].casa.variacion.replace(/,/g, '.')) < 0){
                    blueVar.innerHTML = `↓ VARIACION ${data[i].casa.variacion}%`
                }
                else{
                    blueVar.innerHTML = `= VARIACION ${data[i].casa.variacion}%`
                }
                
            }

            else if(data[i].casa.nombre == "Dolar Contado con Liqui"){
                liqui.textContent = `$ ${data[i].casa.venta}`
                if(parseFloat(data[i].casa.variacion.replace(/,/g, '.')) > 0){
                    liquiVar.innerHTML = `↑ VARIACION +${data[i].casa.variacion}%`
                }
                else if(parseFloat(data[i].casa.variacion.replace(/,/g, '.')) < 0){
                    liquiVar.innerHTML = `↓ VARIACION ${data[i].casa.variacion}%`
                }
                else{
                    liquiVar.innerHTML = `= VARIACION ${data[i].casa.variacion}%`
                }
                
            }

            else if(data[i].casa.nombre == "Dolar"){
                promCompra.textContent = `$ ${data[i].casa.compra}`
                promVenta.textContent = `$ ${data[i].casa.venta}`
                data[i].casa.variacion = data[0].casa.variacion
                if(parseFloat(data[i].casa.variacion.replace(/,/g, '.')) > 0){
                    promVar.innerHTML = `↑ VARIACION +${data[i].casa.variacion}%`
                }
                else if(parseFloat(data[i].casa.variacion.replace(/,/g, '.')) < 0){
                    promVar.innerHTML = `↓ VARIACION ${data[i].casa.variacion}%`
                }
                else{
                    promVar.innerHTML = `= VARIACION ${data[i].casa.variacion}%`
                }
                
            }

            else if(data[i].casa.nombre == "Dolar Bolsa"){
                bolsa.textContent = `$ ${data[i].casa.compra}`
                if(parseFloat(data[i].casa.variacion.replace(/,/g, '.')) > 0){
                    bolsaVar.innerHTML = `↑ VARIACION +${data[i].casa.variacion}%`
                }
                else if(parseFloat(data[i].casa.variacion.replace(/,/g, '.')) < 0){
                    bolsaVar.innerHTML = `↓ VARIACION ${data[i].casa.variacion}%`
                }
                else{
                    bolsaVar.innerHTML = `= VARIACION ${data[i].casa.variacion}%`
                }
                
            }

            else if(data[i].casa.nombre == "Dolar turista"){
                turista.textContent = `$ ${data[i].casa.venta}`
                if(parseFloat(data[i].casa.variacion.replace(/,/g, '.')) > 0){
                    turistaVar.innerHTML = `↑ VARIACION +${data[i].casa.variacion}%`
                }
                else if(parseFloat(data[i].casa.variacion.replace(/,/g, '.')) < 0){
                    turistaVar.innerHTML = `↓ VARIACION ${data[i].casa.variacion}%`
                }
                else{
                    turistaVar.innerHTML = `= VARIACION ${data[i].casa.variacion}%`
                }
                
            }


        }

    });
}

function addingDate(){

    if(dia.getMinutes()<10 && dia.getHours()<10){
        for( i = 0; i < fecha.length; i++){
            fecha[i].textContent = `ACTUALIZADO: ${dia.getDate()}/${dia.getMonth()+1}/${dia.getFullYear()} 0${dia.getHours()}:0${dia.getMinutes()}`
        }
    }

    else if(dia.getMinutes()<10){
        for( i = 0; i < fecha.length; i++){
            fecha[i].textContent = `ACTUALIZADO: ${dia.getDate()}/${dia.getMonth()+1}/${dia.getFullYear()} ${dia.getHours()}:0${dia.getMinutes()}`
        }
    }

    else if(dia.getHours()<10){
        for( i = 0; i < fecha.length; i++){
            fecha[i].textContent = `ACTUALIZADO: ${dia.getDate()}/${dia.getMonth()+1}/${dia.getFullYear()} 0${dia.getHours()}:${dia.getMinutes()}`
        }
    }
    else{
        for( i = 0; i < fecha.length; i++){
            fecha[i].textContent = `ACTUALIZADO: ${dia.getDate()}/${dia.getMonth()+1}/${dia.getFullYear()} ${dia.getHours()}:${dia.getMinutes()}`
        }
    }

}
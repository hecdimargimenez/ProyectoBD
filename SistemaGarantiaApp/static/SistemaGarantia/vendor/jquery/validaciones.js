(function(){

    const btnEliminar = document.querySelectorAll(".btnEliminar");

btnEliminar.forEach(btn => {
    btn.addEventListener('click', (e) =>{

        const confirmar = confirm('¿Seguro que desea eliminar el ticket?');

        if(!confirmar){
            e.preventDefault();
        }

    })
});

})();
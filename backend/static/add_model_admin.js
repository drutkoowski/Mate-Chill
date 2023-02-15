
window.addEventListener('load', () => {
    const parentInput = document.querySelector('#id_parent')
    parentInput.addEventListener('change', (e) => {
        const elementsToHide = [document.querySelector('.field-manufacturer'),
                document.querySelector('.field-country'),
                document.querySelector('.field-description'),
            ]
        if (e.target.value){
            elementsToHide.map(element => element.style.display = 'none')
        }
        else{
            elementsToHide.map(element => element.style.removeProperty('display'))
        }


    })
})

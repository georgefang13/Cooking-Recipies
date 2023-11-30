function addIngredient() {
    const ingredientContainer = document.querySelector("#ingredient-container");
    const newIngredient = document.createElement('div');
    newIngredient.classList.add('ingredient');
    newIngredient.innerHTML = `
        <input type="text" name="ingredient" placeholder="Name, Qty" required>
        <button type="button" onclick="removeIngredient(this)">Remove</button>
    `;
    ingredientContainer.appendChild(newIngredient);
}

function removeIngredient(button) {
    const ingredientContainer = document.querySelector("#ingredient-container");
    ingredientContainer.removeChild(button.parentNode);
}

function addStep() {
    const stepContainer = document.querySelector("#step-container");
    const newStep = document.createElement('li');
    newStep.classList.add('step');
    newStep.innerHTML = `
        <input type="text" name="step" required>
        <button type="button" onclick="removeStep(this)">Remove</button>
    `;
    stepContainer.appendChild(newStep);
}

function removeStep(button) {
    const stepContainer = document.querySelector("#step-container");
    stepContainer.removeChild(button.parentNode);
}
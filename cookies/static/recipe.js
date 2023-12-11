function addIngredient() {
    const ingredientContainer = document.querySelector("#ingredient-container");
    const newIngredient = document.createElement('div');
    newIngredient.classList.add('ingredient');
    newIngredient.innerHTML = `
        <input type="text" name="ingredients[]" placeholder="Name" required>
        <input type="text" name="units[]" placeholder="Unit" required>
        <input type="text" name="quantities[]" placeholder="Quantity" required>
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

function toggleBookmark(button) {
    //  the button starts as unbookmarked, when pressed it changes to bookmarked, and vice versa
    if (button.textContent === 'Bookmark') {
        button.textContent = 'Unbookmark';
    } else {
        button.textContent = 'Bookmark';
    }
}

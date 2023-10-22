/*
    This recipe is extracted from Classic
    Chocolate Chip Cookies recipe
    from https://youtu.be/loqCY9b7aec

    STEPS:
    1. [ 2 Minutes] Mix the flour, baking soda, and salt in a large bowl.
    2. [10 Minutes] Allow the butter and egg to reach room temperature.
    3. [ 3 Minutes] Mix the butter (at room temperature), sugar, brown sugar,
                    egg (at room temperature), and vanilla in a bowl.
    4. [ 5 Minutes] Combine the dry and wet ingredients.
    5. [ 1 Minute ] Add the chocolate chips.
    6. [60 Minutes] Chill the dough.
    7. [10 Minutes] Roll the dough into balls.
    8. [15 Minutes] Preheat the oven.
    9. [15 Minutes] Bake the cookies.
*/

let tasks = [
    {
        order: 0,
        id: "mix-the-dry-ingredients",
        content: "Mix the dry ingredients",
        time: 2,
        prerequisites: [],
        occupies_chef: true,
    },
    {
        order: 1,
        id: "allow-ingredients-to-reach-room-temperature",
        content: "Allow the butter and egg to reach room temperature",
        time: 10,
        prerequisites: [],
        occupies_chef: false,
    },
    {
        order: 2,
        id: "mix-the-wet-ingredients",
        content: "Mix the butter, sugar, egg, and vanilla in a bowl",
        time: 3,
        prerequisites: ["allow-ingredients-to-reach-room-temperature"],
        occupies_chef: true,
    },
    {
        order: 3,
        id: "combine-the-dry-and-wet-ingredients",
        content: "Combine the dry and wet ingredients",
        time: 5,
        prerequisites: ["mix-the-dry-ingredients", "mix-the-wet-ingredients"],
        occupies_chef: true,
    },
    {
        order: 4,
        id: "add-the-chocolate-chips",
        content: "Add the chocolate chips",
        time: 1,
        prerequisites: ["combine-the-dry-and-wet-ingredients"],
        occupies_chef: true,
    },
    {
        order: 5,
        id: "chill-the-dough",
        content: "Chill the dough",
        time: 60,
        prerequisites: ["add-the-chocolate-chips"],
        occupies_chef: false,
    },
    {
        order: 6,
        id: "roll-the-dough-into-balls",
        content: "Roll the dough into balls",
        time: 10,
        prerequisites: ["chill-the-dough"],
        occupies_chef: true,
    },
    {
        order: 7,
        id: "preheat-the-oven",
        content: "Preheat the oven",
        time: 15,
        prerequisites: [],
        occupies_chef: false,
    },
    {
        order: 8,
        id: "bake-the-cookies",
        content: "Bake the cookies",
        time: 15,
        prerequisites: ["roll-the-dough-into-balls", "preheat-the-oven"],
        occupies_chef: false,
    }
];

tasks.forEach((task) => {
    task.start = 0;
    task.end = 0;
    task.completed = true;
});

function createTasks() {
    const taskContainer = document.querySelector('.task-container');

    tasks.forEach((task) => {
        const taskElement = document.createElement('div');
        taskElement.classList.add('task');
        taskElement.classList.add('unselectable');
        taskElement.textContent = task.content;
        taskContainer.appendChild(taskElement);
        // add chef icon if task occupies chef
        if (task.occupies_chef) {
            const chefElement = document.createElement('img');
            chefElement.src = 'chef.png';
            chefElement.classList.add('chef');
            taskElement.appendChild(chefElement);
        }
        const timeElement = document.createElement('div');
        timeElement.classList.add('time');
        timeElement.classList.add('unselectable');
        timeElement.textContent = `${task.time} min`;
        taskElement.appendChild(timeElement);
        const prerequisitesElement = document.createElement('div');
        prerequisitesElement.classList.add('prerequisites');
        prerequisitesElement.classList.add('unselectable');
        prerequisitesElement.textContent = task.prerequisites.join(', ');
        taskElement.appendChild(prerequisitesElement);
        const taskIdElement = document.createElement('div');
        taskIdElement.classList.add('task-id');
        taskIdElement.classList.add('unselectable');
        taskElement.appendChild(taskIdElement);
        const formElement = document.createElement('form');
        formElement.classList.add('form');
        taskContainer.appendChild(formElement);
        const inputElement = document.createElement('input');
        inputElement.classList.add('input');
        inputElement.type = 'number';
        inputElement.name = task.id;
        inputElement.min = 0;
        inputElement.max = 120;
        inputElement.step = 1;
        // calculate the total time before this task
        let totalTime = 0;
        for (let i = 0; i < task.order; i++) {
            totalTime += tasks[i].time;
        }
        inputElement.value = totalTime;
        taskIdElement.appendChild(inputElement);
    });
}

function calculateTime() {
    const inputs = document.querySelectorAll('.input');
    let totalTime = 0;
    inputs.forEach((input) => {
        const task = tasks.find((task) => task.id === input.name);
        task.start = parseInt(input.value);
        task.end = task.start + task.time;
    });
    // check if prerequisites are met
    tasks.forEach((task) => {
        task.completed = true;
    });
    let errorMessages = [];
    tasks.every( (task) => {
        let prerequisitesMet = true;
        task.prerequisites.forEach((prerequisite) => {
            const prerequisiteTask = tasks.find((task) => task.id === prerequisite);
            if (prerequisiteTask.end > task.start) {
                prerequisitesMet = false;
                console.log(task.id, 'prerequisites not met');
                errorMessages.push(`Prerequisites of ${task.id} are not met`);
                task.completed = false;
                return false;
            }
            if (!prerequisiteTask.completed) {
                prerequisitesMet = false;
                console.log(task.id, 'prerequisites not met');
                errorMessages.push(`Prerequisites of ${task.id} are not met`);
                task.completed = false;
                return false;
            }
        });
        if (prerequisitesMet) {
            let chefOccupied = false;
            tasks.forEach((otherTask) => {
                if (task.occupies_chef && otherTask.occupies_chef) {
                    if (otherTask !== task) {
                        if (otherTask.start < task.end && otherTask.end > task.start) {
                            chefOccupied = true;
                            console.log(task.id, 'chef occupied');
                            errorMessages.push(`Chef is not available for ${task.id}`);
                            task.completed = false;
                            return false;
                        }
                    }
                }
            });
        }
        return true;
    });
    // calculate total time but starting time values can be overlapping
    tasks.forEach((task) => {
        if (task.completed) {
            totalTime = Math.max(totalTime, task.end);
        }
    });
    console.log(totalTime);
    // show the results in result-container
    const resultContainer = document.querySelector('.result-container');
    resultContainer.innerHTML = '';
    // show if there are errors
    tasks.forEach((task) => {
        console.log(task.id, task.completed);
    });
    const errors = tasks.filter((task) => !task.completed);
    if (errors.length > 0) {
        errorMessages.forEach((errorMessage) => {
            const errorElement = document.createElement('div');
            errorElement.classList.add('error');
            errorElement.classList.add('unselectable');
            errorElement.textContent += `${errorMessage}`;
            resultContainer.appendChild(errorElement);
        });
    }
    else {
        const cookingTimeElement = document.createElement('img');
        cookingTimeElement.src = 'cooking-time.png';
        cookingTimeElement.classList.add('cooking-time');
        resultContainer.appendChild(cookingTimeElement);
        const resultElement = document.createElement('div');
        resultElement.classList.add('result');
        resultElement.classList.add('unselectable');
        resultElement.textContent = `Your recipe  took ${totalTime} minutes to cook`;
        resultContainer.appendChild(resultElement);
    }
}

createTasks();
calculateTime();

const inputs = document.querySelectorAll('.input');
inputs.forEach((input) => {
    input.addEventListener('change', () => {
        calculateTime();
    });
});
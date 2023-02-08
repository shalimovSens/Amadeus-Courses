const ide = ace.edit('editor');
// IDE Options
const taskValuesForIde = {
    '1': '// Put your code here',
    '3': 'let V = 24; // Скорость\nlet t = 2; // Время',
    '2'   : 'console.log(5 _ (2 _ 6) _ 2);',
    '4': '// Put your code here',
}
let ideDefaultValue = '1234'.includes(location.href.split('/')[4]) ? taskValuesForIde[location.href.split('/')[4]] : '// Put your code here';
ide.setValue(ideDefaultValue);
ide.setTheme('ace/theme/clouds');
ide.session.setMode('ace/mode/javascript');
ide.setOptions({
    fontSize: '18px',
    enableBasicAutocompletion: true,
    enableLiveAutocompletion: true,
});

// Main funcional buttons
let outputToConsoleBtn = document.querySelector('.resultBtn');
let resetBtn = document.querySelector('.resetBtn');


const getCodeResult = () => {
    let input = ide.getValue();
    let str = 'const originalLog = console.log;console.log = function (...value) {originalLog.apply(console, value);return value;};'
    // input = 'out = "";console.log = function(val){out = out + " " + val; return out;};' + input;
    input = str + input;
    try {
        input = eval(input);
    } catch (err) {
        input = err;
    }
    return input
};


outputToConsoleBtn.addEventListener('click', (event) => {
    addLogs(getCodeResult());
});


resetBtn.addEventListener('click', (event) => {
    ide.setValue(ideDefaultValue);
});


// Консоль
const consoleLogs = document.querySelector('.consoleLogs');
const resetConsole = document.querySelector('.console > .Btn');


const addLogs = (input) => {
    const log = document.createElement('li');
    if (input.length > 1) {
        log.textContent = `>  ${input}`;
    } else {
        if (typeof input[0] == 'string') {
                log.textContent = `>  '${input[0]}'`;
        } else if (Array.isArray(input[0])) {
            log.textContent = `>  [${input[0]}]`;
        } else {
            log.textContent = `>  ${input[0]}`;
        }
    }
    consoleLogs.appendChild(log);
};


resetConsole.addEventListener('click', (event) => {
    consoleLogs.innerHTML = '';
})


// Проверка Решения
const completeBtn = document.querySelector('.completeBtn');
const ideContainer = document.querySelector('.editorContainer');
const ideBtnsGoup = document.querySelector('.ideBtnWrap');
const tastCompleteResult = document.createElement('div')
tastCompleteResult.className = 'notification';


const rightTestValue = {
    '1' : 'Hello, World!',
    '3' : 48,
    '2' : 38,
    '4' : 'Смузихлеб Иван - лучший фронт'
};


const completeTask = () => {
    const keyOfTestValue = location.href.split('/')[4];
    addLogs(getCodeResult());
    if (getCodeResult()[0] === rightTestValue[keyOfTestValue]) {
        completeBtn.textContent = 'Решить еще раз';
        tastCompleteResult.style.backgroundColor = 'rgba(89, 138, 118, 0.6)';
        tastCompleteResult.textContent = 'Задание выполнено';
    } else if (keyOfTestValue == '4') {
        tastCompleteResult.style.backgroundColor = 'rgba(89, 138, 118, 0.6)';
        tastCompleteResult.textContent = 'Задание выполнено';
    } else {
        tastCompleteResult.style.backgroundColor = 'rgba(164, 50, 64, 0.5)';
        tastCompleteResult.textContent = 'Попробуйте еще раз';
    }
    ideContainer.insertBefore(tastCompleteResult, ideBtnsGoup);
}   
completeBtn.addEventListener('click', completeTask);
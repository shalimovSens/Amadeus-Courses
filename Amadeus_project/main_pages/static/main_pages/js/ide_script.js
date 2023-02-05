const ide = ace.edit('editor');
// IDE Options
let ideDefaultValue = '// Put your code here';
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
    if (typeof input[0] == 'string') {
            log.textContent = `>  '${input[0]}'`;
    }else if (typeof input[0] == 'number') {
        log.textContent = `>  ${input[0]}`;
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
    'task1' : 'Hello, World!',
    'task3' : 48,
    'task2' : 38,
};


const completeTask = () => {
    const keyOfTestValue = location.href.split('/')[3];
    addLogs(getCodeResult());
    if (getCodeResult()[0] === rightTestValue[keyOfTestValue]) {
        completeBtn.textContent = 'Решить еще раз'
        tastCompleteResult.style.backgroundColor = 'rgba(89, 138, 118, 0.6)'
        tastCompleteResult.textContent = 'Задание выполнено'
    } else {
        tastCompleteResult.style.backgroundColor = 'rgba(164, 50, 64, 0.5)'
        tastCompleteResult.textContent = 'Попробуйте еще раз'
    }
    ideContainer.insertBefore(tastCompleteResult, ideBtnsGoup);
}   
completeBtn.addEventListener('click', completeTask);

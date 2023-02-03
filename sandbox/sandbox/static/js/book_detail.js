let pausebutton;
let cword;
stop = true;
let text_display = document.getElementById('text_display');

const timer = ms => new Promise(res => setTimeout(res, ms));
var text_words = text.split(' ');

let new_text = parse_words(text_words);
text_display.innerHTML = new_text;

go_forward();

function parse_words(text_words) {
    let new_text = ''

    for (var i in text_words) {
        new_text += 
        '<span id=\'word' + i + '\' onclick="word_click(this.id)">' + 
            text_words[i] + 
        '</span> '
    }

    return new_text
}

function pauser() {
    return new Promise(resolve => {
        let playbuttonclick = function () {
            if (stop == false) {
                stop = true;
                pausebutton.innerHTML = 'Start'
                                              
            }
            else {                 
                stop = false;
                pausebutton.innerHTML = 'Stop'                    
            }
            resolve('resolved')
        }
        pausebutton.addEventListener('click', playbuttonclick)
    })
}

function word_click(word_id) {
    className = word_id;
    id = word_id.substring(4,);
    prev_iterator = iterator;
    iterator = id;

    highlighter(prev_iterator, 'transparent')
    highlighter(iterator, 'beige')
}

async function go_forward() {
    pausebutton = document.getElementById('pausebutton')
    cword = document.getElementById('cword')
            
    for (iterator = 0; iterator < text_words.length; iterator++) {
        cword.innerHTML = text_words[iterator]

        if (iterator < 1) {
            prevword = '';
        }
        else {        
            thisword = highlighter(iterator, 'beige');
            thisword.scrollIntoView({block: 'center'});
            first_word_highlight()

            await timer(200); // then the created Promise can be awaited
        }
        if (stop == true) await pauser();
    }
}

async function word_highlight_logic(iterator) {
    cword.innerHTML = text_words[iterator]

    if (iterator < 1) {
        prevword = '';
    }
    else {
        thisword = highlighter(iterator, 'beige');
        thisword.scrollIntoView({block: 'center'});
        first_word_highlight()

        await timer(200); // then the created Promise can be awaited
    }
}

function highlighter(id,colour) {
    thisword = document.getElementById('word'+ id)
    thisword.style.backgroundColor = colour;   
    return thisword
}

function first_word_highlight() {
    try {
        highlighter((iterator-1), 'transparent')
    }
    catch {console.log('oops')}
}

let stop = true;
let page_iterator;
let word_iterator;

let text = unescape(JSON.parse(document.getElementById('book_json').textContent))

let text_display = document.getElementById('text_display');

let pausebutton = document.getElementById('pausebutton');
let forwardbutton = document.getElementById('forwardbutton');
let backbutton = document.getElementById('backbutton');

let cword = document.getElementById('cword');

forwardbutton.addEventListener('click', page_forward);
backbutton.addEventListener('click', page_backward);

const timer = ms => new Promise(res => setTimeout(res, ms));

var pages = text.split('PAGE');

start_forward();

function word_click(word_id) {
    className = word_id;
    id = word_id.substring(4,);
    prev_word_iterator = word_iterator;
    word_iterator = id;

    highlighter(prev_word_iterator, 'transparent')
    highlighter(word_iterator, 'beige')
}

async function start_forward() {
    for (page_iterator = 0; page_iterator < pages.length; page_iterator++) {
        display_page(page_iterator);

        for (word_iterator = 0; word_iterator < page_length; word_iterator++) {
            if (stop == true) await pauser();
            cword.innerHTML = text_words[word_iterator]
            //We need to reset this loop when we go to a new page
            if (word_iterator < 1) {
                prevword = '';
            }
            else {        
                thisword = highlighter(word_iterator, 'beige');
                thisword.scrollIntoView({block: 'center'});
                first_word_highlight()

                await timer(200); // then the created Promise can be awaited
            }
        }
    }
}

function page_forward() {
    if (page_iterator < pages.length) {
        page_iterator += 1;
    }
    display_page(page_iterator);
}

function page_backward() {
    if (page_iterator > 1) {
        page_iterator -= 1;
    }
    display_page(page_iterator);
}

function display_page(page_iterator) {
    text_words = pages[page_iterator].split(' ');
    text_display.innerHTML = parse_words(text_words);
    page_length = text_words.length
    word_iterator = 0;
}

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

async function word_highlight_logic(word_iterator) {
    cword.innerHTML = text_words[word_iterator]

    if (word_iterator < 1) {
        prevword = '';
    }
    else {
        thisword = highlighter(word_iterator, 'beige');
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
        highlighter((word_iterator-1), 'transparent')
    }
    catch {console.log('oops')}
}

function pauser() {
    return new Promise(resolve => {
        let playbuttonclick = function () {
            if (stop == false) {
                stop = true;
                pausebutton.innerHTML = 'Start'
                                              
            }
            else if (stop == true) {                 
                stop = false;
                pausebutton.innerHTML = 'Stop'                    
            }
            resolve('resolved')
        }
        pausebutton.addEventListener('click', playbuttonclick)
    })
}

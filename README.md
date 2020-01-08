gtranslate
==========

Free Google Translate API. It works with two providers Google API and Browser (chrome).


Requirements:
-------------
- python 3.6 > 
- slenium
- googletrans
- chromedriver-binary

Features
--------

- Text list translation

Installation
------------
``` sh
  $ pip install git+https://github.com/lcmonteiro/tool-gtranslate.git
```

Example usage
-------------
``` python
from pprint               import pprint
from gtranslate           import Translator
from gtranslate.providers import GoogleAPI
from gtranslate.providers import GoogleBrowser

data = [
    'Amor é fogo que arde sem se ver', 
    'Amor é fogo que arde sem se ver;', 
    'É ferida que dói e não se sente;', 
    'É um contentamento descontente;', 
    'É dor que desatina sem doer;', 
    'É um não querer mais que bem querer;', 
    'É solitário andar por entre a gente;', 
    'É nunca contentar-se de contente;', 
    'É cuidar que se ganha em se perder;', 
    'É querer estar preso por vontade;', 
    'É servir a quem vence, o vencedor;', 
    'É ter com quem nos mata lealdade.', 
    'Mas como causar pode seu favor', 
    'Nos corações humanos amizade,', 
    'Se tão contrário a si é o mesmo Amor?'
]

provider   = GoogleBrowser()
translated = provider.translate(data)
pprint(translated)

provider   = GoogleAPI()
translated = provider.translate(data)
pprint(translated)

engine     = Translator()
translated = engine.translate(data)
pprint(translated)
```
Output
------
``` python
['Love is fire that burns without being seen',
 'Love is fire that burns without being seen;',
 'It wound that hurts and does not feel;',
 'It is an unhappy joy;',
 'It desatina pain without hurting;',
 "It's a not want more than good will;",
 "It's lonely walk among us;",
 'It is never content themselves with joy;',
 'It is care that is gained about getting lost;',
 'You want to be trapped by the will;',
 'It serves who wins, the winner;',
 'Have someone kill us, loyalty.',
 'But how can cause your favor',
 'In human hearts friendship,',
 'If so contrary to itself is the same love?']
```

Author
------
[Luis Monteiro @ linkdin](<https://www.linkedin.com/in/luis-monteiro-918a3033/>)

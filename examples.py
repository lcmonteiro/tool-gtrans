from pprint import pprint

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

from gtranslate.providers import GoogleAPI
from gtranslate.providers import GoogleBrowser

provider   = GoogleBrowser()
translated = provider.translate(data)
pprint(translated)

translated = provider.translate(data)
pprint(translated)
translated = provider.translate(data)
pprint(translated)
translated = provider.translate(data)
pprint(translated)
translated = provider.translate(data)
pprint(translated)
translated = provider.translate(data)
pprint(translated)
translated = provider.translate(data)
pprint(translated)
translated = provider.translate(data)
pprint(translated)
translated = provider.translate(data)
pprint(translated)
translated = provider.translate(data)
pprint(translated)
translated = provider.translate(data)
pprint(translated)

provider   = GoogleAPI()
translated = provider.translate(data)
pprint(translated)





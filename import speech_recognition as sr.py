import speech_recognition as sr
from nltk.corpus import cmudict
from nltk.corpus import stopwords

def analisar_frase(frase):
    # Analisar velocidade
    palavras = frase.split()
    velocidade = len(palavras) / len(frase.split())

    # Analisar compreensão fonológica
    dicionario = cmudict.dict()
    palavras_foneticas = [pronunciations for word, pronunciations in dicionario.items() if word in palavras]
    compreensao_fonologica = len(palavras_foneticas) / len(palavras)

    # Verificar fala clara
    fala_clara = True  # Implemente sua própria lógica para verificar se a fala é clara

    # Verificar fluidez
    fluidez = True  # Implemente sua própria lógica para verificar a fluidez

    # Verificar precisão e acurácia (requer reconhecimento de fala)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale algo para verificar precisão e acurácia:")
        audio = r.listen(source)

    try:
        texto_reconhecido = r.recognize_google(audio, language='pt-BR')
        precisao = len(set(frase.split()).intersection(texto_reconhecido.split())) / len(frase.split())
        acuracia = precisao * compreensao_fonologica
    except sr.UnknownValueError:
        print("Não foi possível reconhecer a fala.")
        precisao = 0
        acuracia = 0
    except sr.RequestError as e:
        print("Erro ao solicitar o serviço de reconhecimento de fala: {0}".format(e))
        precisao = 0
        acuracia = 0

    # Retornar resultados
    resultados = {
        'velocidade': velocidade,
        'compreensao_fonologica': compreensao_fonologica,
        'fala_clara': fala_clara,
        'fluidez': fluidez,
        'precisao': precisao,
        'acuracia': acuracia
    }
    return resultados

# Frase para análise
frase = "A rápida raposa marrom pula sobre o cachorro preguiçoso"

resultados = analisar_frase(frase)
print(resultados)
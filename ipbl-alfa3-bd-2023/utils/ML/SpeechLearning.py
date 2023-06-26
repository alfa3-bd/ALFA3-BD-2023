import speech_recognition as sr
import wave
import contextlib
import numpy as np
import soundfile as sf
import core.models
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher

class SpeechLearning:

    def __init__(self) -> None:
        super().__init__()

    def analyze_audio(self,file_name,texto_padrao):
        file = os.path.join("./downloads/", file_name)
        print(file)
        print(texto_padrao)
        r = sr.Recognizer()
        # Carrega o arquivo de áudio
        with sr.AudioFile(file) as source:
            audio = r.record(source)
        try:
            # Reconhece o áudio usando o Google Speech Recognition
            texto = r.recognize_google(audio, language='pt-BR')
            tamanho_texto=len(texto.split())
            with contextlib.closing(wave.open(file,'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
                velocidade = tamanho_texto/duration

                # Tokenização e vetorização das sentenças
                vectorizer = TfidfVectorizer()
                tfidf_matrix = vectorizer.fit_transform([texto, texto_padrao])
                result_cos = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)

                pontuacao=(result_cos[0][1]*0.7+ (velocidade/1.90)*0.3)*100

            self.update_db(file_name,pontuacao)
            os.remove(file)

        except sr.UnknownValueError:
            print("Não foi possível reconhecer o áudio.")
        except sr.RequestError as e:
            print("Erro ao solicitar o serviço de reconhecimento de fala: {0}".format(e))

    def update_db(self,file_name,metric):
        coleta = core.models.Coleta.objects.get(col_audio = file_name)
        coleta.col_metrica = metric
        coleta.save()

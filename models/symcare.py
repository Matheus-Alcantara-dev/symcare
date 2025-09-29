import numpy as np
import pandas as pd

class SymCare:
    def __init__(self):
        # Lista de sintomas que o usuário pode selecionar
        self.sintomas_lista = ["Dor de cabeça", "Febre", "Tosse", "Dor muscular", "Cansaço", "Náusea", "Gripe"]

        # Lista de medicamentos disponíveis para recomendação
        self.medicamentos_lista = ["Paracetamol", "Ibuprofeno", "Dipirona", "Xarope para tosse", "Benzydamina", 
                                 "Ambroxol", "Cafeína", "Ginseng", "Vitaminas C e B12", "Dramin", "Plasil", 
                                 "Soro fisiológico", "Oseltamivir"]

        # Dicionário que mapeia sintomas aos medicamentos recomendados
        self.medicamentos_por_sintoma = {
            "Dor de cabeça": ["Paracetamol", "Ibuprofeno", "Dipirona"],
            "Febre": ["Paracetamol", "Dipirona", "Ibuprofeno"],
            "Tosse": ["Xarope para tosse", "Benzydamina", "Ambroxol"],
            "Dor muscular": ["Dipirona", "Ibuprofeno", "Paracetamol"],
            "Cansaço": ["Cafeína", "Ginseng", "Vitaminas C e B12"],
            "Náusea": ["Dramin", "Plasil", "Soro fisiológico"],
            "Gripe": ["Paracetamol", "Ibuprofeno", "Oseltamivir"]
        }

        # Preços dos medicamentos (adicionando essa informação para o sistema)
        self.precos_medicamentos = {
            "Paracetamol": 15.90,
            "Ibuprofeno": 18.50,
            "Dipirona": 12.90,
            "Xarope para tosse": 25.90,
            "Benzydamina": 22.50,
            "Ambroxol": 28.90,
            "Cafeína": 15.90,
            "Ginseng": 45.90,
            "Vitaminas C e B12": 35.90,
            "Dramin": 19.90,
            "Plasil": 16.90,
            "Soro fisiológico": 8.90,
            "Oseltamivir": 89.90
        }

        self._criar_matriz_recomendacao()
        self._criar_dataframe()

    def _criar_matriz_recomendacao(self):
        """Cria a matriz de recomendação de medicamentos por sintomas"""
        self.matriz_recomendacao = np.zeros((len(self.sintomas_lista), len(self.medicamentos_lista)))
        
        for i, sintoma in enumerate(self.sintomas_lista):
            for j, medicamento in enumerate(self.medicamentos_lista):
                if medicamento in self.medicamentos_por_sintoma[sintoma]:
                    self.matriz_recomendacao[i, j] = 1

    def _criar_dataframe(self):
        """Cria o DataFrame com as recomendações"""
        dados = {
            'Sintoma': self.sintomas_lista,
            'Medicamentos Recomendados': [', '.join(self.medicamentos_por_sintoma[sintoma]) 
                                        for sintoma in self.sintomas_lista]
        }
        self.df = pd.DataFrame(dados)

    def get_recomendacoes(self, sintoma):
        """Retorna os medicamentos recomendados para um sintoma específico"""
        if sintoma in self.medicamentos_por_sintoma:
            return [
                {
                    'nome': med,
                    'preco': self.precos_medicamentos[med]
                }
                for med in self.medicamentos_por_sintoma[sintoma]
            ]
        return []

    def buscar_medicamento(self, termo_busca):
        """Busca medicamentos pelo nome"""
        termo_busca = termo_busca.lower()
        return [
            {
                'nome': med,
                'preco': self.precos_medicamentos[med]
            }
            for med in self.medicamentos_lista
            if termo_busca in med.lower()
        ]

    def get_preco_medicamento(self, medicamento):
        """Retorna o preço de um medicamento específico"""
        return self.precos_medicamentos.get(medicamento)
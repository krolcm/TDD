import unittest
from unittest.mock import patch
from io import StringIO

from tdd import Aluno  

class TestAluno(unittest.TestCase):
    @patch('builtins.input', side_effect=['74', '70', '0'])
    def teste_caso_base(self, mock_input):
        aluno = Aluno()
        resultado = aluno.determinarAprovação(74, 70, 0)
        self.assertEqual(resultado, "Reprovado (frequência < 75%)")

    @patch('builtins.input', side_effect=['75', '60', '0'])
    def teste_demais_casos(self, mock_input):
        aluno = Aluno()
        resultado = aluno.determinarAprovação(75, 60, 0)
        self.assertEqual(resultado, "Aprovado")

    @patch('builtins.input', side_effect=['-75', '-50', '-5'])
    def teste_casos_excepcionais(self, mock_input):
        aluno = Aluno()
        resultado = aluno.determinarAprovação(-75, -50, -5)
        self.assertEqual(resultado, "Reprovado (parâmetro negativo)")    

if __name__ == '__main__':
    unittest.main()
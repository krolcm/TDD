class Aluno:
    def determinarAprovação(self, frequencia, notaFinal, notaEspecial):
        if frequencia < 0 or notaFinal < 0 or notaEspecial < 0:
            return "Reprovado (parâmetro negativo)"
        elif frequencia < 75:
            return "Reprovado (frequência < 75%)"
        elif notaFinal >= 60 or (notaFinal + notaEspecial) / 2 >= 60:
            return "Aprovado"
        else:
            return "Reprovado"
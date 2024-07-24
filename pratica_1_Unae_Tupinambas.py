##### dicionário -  JSON

import json

def main():
    dict_alunos={}

    dict_alunos["a1"] = {'nome': 'Unae', 'idade': 25, 'curso': 'Sistemas de Informacao', 'disciplinas': ['Programacao', 'Banco de Dados', 'Redes de Computadores']}
    dict_alunos["a2"] = {'nome': 'Joao', 'idade': 20, 'curso': 'Engenharia de Software', 'disciplinas': ['Programacao', 'Banco de Dados', 'Redes de Computadores']}
    dict_alunos["a3"] = {'nome': 'Maria', 'idade': 22, 'curso': 'Sistemas de Informacao', 'disciplinas': ['Programacao', 'Banco de Dados', 'Redes de Computadores']}
    dict_alunos["a4"] = {'nome': 'Jose', 'idade': 21, 'curso': 'Engenharia de Software', 'disciplinas': ['Programacao', 'Banco de Dados', 'Redes de Computadores']}

    print("######## DADOS DO DICIONÁRIO INICIAL ########")
    print("Quantidade de Alunos: %d" % len(dict_alunos))
    for aluno_ID in dict_alunos:
        print("######## ALUNO ########")
        print("Código: %s" % aluno_ID)
        print("Nome: %s" % dict_alunos[aluno_ID]['nome'])
        print("Idade: %d" % dict_alunos[aluno_ID]['idade'])
        print("Curso: %s" % dict_alunos[aluno_ID]['curso'])
        print("Disciplinas: ")
        lista_disciplinas = dict_alunos[aluno_ID]['disciplinas']
        for disciplina in lista_disciplinas:
            print("%s" % disciplina)        
        print("")

    print("Todo o dicionário: %s" % dict_alunos)

    input("O programa vai sair em um arquivo JSON, aperte ENTER para continuar...")
    ########### SALVANDO O JSON ###########
    with open('dict_alunos.json', 'w') as f:
        json.dump(dict_alunos, f)
# alternativa: f.write(json.dumps(dict_alunos))

    input("O programa vai ler o arquivo JSON, aperte ENTER para continuar...")
    ########### LENDO O JSON ###########
    dicionario_lido = {}
    with open('dict_alunos.json') as f:
        dicionario_lido = json.load(f)
#alternativa: dicionario_lido = json.loads(f.read())

        for aluno_ID in dicionario_lido:
            print("######## ALUNO ########")
            print("Código: %s" % aluno_ID)
            print("Nome: %s" % dicionario_lido[aluno_ID]['nome'])
            print("Idade: %d" % dicionario_lido[aluno_ID]['idade'])
            print("Curso: %s" % dicionario_lido[aluno_ID]['curso'])
            print("Disciplinas: ")
            lista_disciplinas = dicionario_lido[aluno_ID]['disciplinas']
            for disciplina in lista_disciplinas:
                print("%s" % disciplina)        
            print("")

#### SALVAR CADA ALUNO EM UMA LINHA ####
    input("Vamos salvar cada aluno em uma linha, aperte ENTER para continuar...")
    with open('dict_alunos_linha.json', 'w') as f:
        for aluno_ID in dict_alunos:
            f.write('%s\n' % (json.dumps({aluno_ID: dicionario_lido[aluno_ID]})))

#### LER CADA ALUNO EM UMA LINHA ####
    input("O programa vai ler linha por linha o arquivo JSON, aperte ENTER para continuar...")
    print("##### LENDO O JSON LINHA POR LINHA #####")
    with open('dict_alunos_linha.json') as f:
        for linha in f:
            linha = linha.strip()
            json_linha = json.loads(linha)
            print(json_linha.keys())
            aluno_ID = list(json_linha.keys()).pop()
            aluno_data = json_linha[aluno_ID]
            print("%s:%s" % (aluno_ID, aluno_data)) 
            
#### salvando como TSV ####

    input("O programa vai salvar o arquivo TSV, aperte ENTER para continuar...")    
    with open('dict_alunos_tsv.tsv', 'w') as f:
        f.write('ID\tNome\tIdade\tCurso\tDisciplinas\n')
        for aluno_ID in dicionario_lido:
            lista_disciplinas = dicionario_lido[aluno_ID]['disciplinas']
            num_disciplinas = len(lista_disciplinas)
            f.write('%s\t%s\t%d\t%s\t%d\n' % (aluno_ID, dicionario_lido[aluno_ID]['nome'], 
                                              dicionario_lido[aluno_ID]['idade'], 
                                              dicionario_lido[aluno_ID]['curso'],
                                              num_disciplinas))
            
#### lendo como TSV ####

    input("O programa vai ler o arquivo TSV, aperte ENTER para continuar...")      
    print("##### LENDO O TSV #####")
    with open('dict_alunos_tsv.tsv') as f:
        header = f.readline().strip().split('\t')
        print(header)
        for linha in f:
            print(linha.strip())
            elementos = linha.strip().split('\t')
            print(elementos)   
           
##padrao main
if __name__ == "__main__":
    main()
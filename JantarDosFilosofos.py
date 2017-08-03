# -*- coding: utf-8 -*-

#======================================================#
#                 JantarDosFilosofos.py                #
#   UENP - Universidade Estadual do Norte do Paraná    #
#   CCT  - Centro de Ciências Tecnológicas             #
#   SI   - Sistemas de Informação                      #
#   SO   - Sistemas Operacionais                       #
#                                                      #
#   Bruno Tsurushima, 868                              #
#   Fernando Queiroz                                   #
#   Lucas Cassanho, 879                                #
#                                                      #
#   "Não tente ser uma pessoa de sucesso.              #
#   Em vez disso, seja uma pessoa de valor"            #
#                        – Albert Einstein             #
#======================================================#

import thread
import time, random
import threading
import os, sys
import termcolor

# CRIA UM VETOR GARFO
garfo = list()
# INSERE NO VETOR 5 SEMAFOROS
for i in range(5):
    garfo.append(threading.Semaphore(1))

def pegaGarfo(f):
    # PEGA GARFO DA ESQUERDA
    garfo[f].acquire()
    # PEGA GARFO DA DIREITA
    garfo[(f + 1) % 5].acquire()

def largaGarfo(f):
    # SOLTA GARFO DA ESQUERDA
    garfo[f].release()
    # SOLTA GARFO DA DIREITA
    garfo[(f + 1) % 5].release()

# CADA THREAD(FILHOS) VAI FICAR RODANDO EM LOOP INFINITO NESSE METODO
# É O METODO PRINCIPAL
def filosofo(f):
    try:
        while True:
            # CHAMA O MÉTODO PEGA GARFO PARA O FILOSOFO SE PREPARAR PARA COMER
            pegaGarfo(f)
            print termcolor.colored('[+]', 'red'), 'Filosofo ' + termcolor.colored(str(f+1), 'red') + ' pegou os garfos.'
            #print '[+] Filosofo '+str(f) + ' pegou os garfos.'
            print termcolor.colored('[*]', 'yellow'), 'Filosofo ' + termcolor.colored(str(f+1), 'yellow') + ' está comendo.\r'
            # CRIA UM SLEEP(DELAY) ALEATORIO DE 1 A 5 SEGUNDOS
            time.sleep(random.randint(1, 10))
            # CHAMA O MÉTODO LARGA GARFO PARA APOS O FILOSOFO COMER
            # PARA LIBERAR O RECURSO
            largaGarfo(f)
            print termcolor.colored('[-]', 'green'), 'Filosofo '+ termcolor.colored(str(f+1), 'green') + ' largou os garfos.'
            # CRIA UM SLEEP(DELAY) ALEATORIO DE 1 A 5 SEGUNDOS PARA O FILOSOFO PENSAR
            print termcolor.colored('[=]', 'blue'), 'Filosofo ' + termcolor.colored(str(f+1), 'blue') + ' está pensando.'
            time.sleep(random.randint(1, 10))
    except KeyboardInterrupt:
        print ('[!] Saindo!', 'red')
        sys.exit(0)

# FOR INDO DE 0 A 4(RODANDO 5 VEZES) PARA CRIAR 5 FILOSOFOS
for i in range(5):
    # LANÇA UMA NOVA THREAD RODANDO COM O MÉTODO FILOSOFO E PASSANDO O i COMO PARAMETRO
    # PARA SER O IDENTIFICADOR DA THREAD
    thread.start_new_thread(filosofo, tuple([i]))

# A THREAD(PAI) FICARÁ EM LOOP INFINITO NESTE MOMENTO, SEM EXECUTAR NADA NO LOOP
# APENAS PARA MANTER O PROCESSO PAI VIVO, E OS FILHOS EXECUTANDO O MÉTODO
try:
    while True:
        pass
except KeyboardInterrupt:
    print termcolor.colored('[!] Saindo', 'red')
    sys.exit(0)

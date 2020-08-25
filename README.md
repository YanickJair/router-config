# Teste

## Desenvolvimento de configurador router

### Características:
    - Criação de Backoffice (utilizar admin django);
    - Cadastro de equipamentos (router) organizado em árvore com os campos: nome e layout;
    - Página no admin para inserção dos campos (nome do cliente, ip, hostname, morada) e seleção do equipamento;
    - Botão para gerar a configuração. Ao clicar no botão, os campos inseridos deverão ser substituídos pela macro inserida no layout do equipamento selecionado.

### Lista de equipamentos (Opcional):

#### Pode-se criar o cadasto de equipamentos em arvore
```
.
├── Marca A
│   └── internet
│   └── vpn
├── Marca B
│   └── internet
│   └── vpn
└── Marca C
    └── internet
    └── vpn
```

### layout exemplo
```txt
## ATENÇÃO ##############################################################
## POR FAVOR, SEGUIR AS INDICAÇÕES DO MANUAL DURANTE A INSTALAÇÃO!      #
##                                                                      #
## ATENÇÃO ##############################################################
!------------------------------------------------------------------------------------------------------------------
!------------------------------------------------------------------------------------------------------------------
!
! IP: {{ IP }}
! hostname: {{ HOSTNAME }}
!
! CLIENTE: {{ CLIENT_NAME }}
!
! MORADA: {{ MORADA }}
!
! Contacto Técnico:  - 
!
!------------------------------------------------------------------------------------------------------------------
```

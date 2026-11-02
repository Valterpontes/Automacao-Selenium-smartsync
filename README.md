# Automação de testes — SmartSync

Script em Python com Selenium que simula um usuário usando o [SmartSync](https://smartsync.app.br) do início ao fim, para testar o fluxo principal da aplicação.

## O que o script faz

1. Abre o Chrome e acessa o SmartSync
2. Faz login com as credenciais de teste
3. Entra em **Contratos** → contrato **UNIFG** → **Bloco 1**
4. Preenche data e hora e liga o dispositivo do 1º andar
5. Troca para o 2º andar e repete o processo
6. Abre a página **Sobre** e faz logout

O fluxo roda duas vezes seguidas, para checar se a aplicação se comporta igual em execuções repetidas.

## Tecnologias

- Python 3
- Selenium WebDriver (com `WebDriverWait` para esperar elementos ficarem clicáveis)
- Google Chrome

## Como rodar

1. Instale o Selenium:

   ```bash
   pip install selenium
   ```

2. Defina as credenciais de teste como variáveis de ambiente (elas não ficam no código):

   ```bash
   # Windows (PowerShell)
   $env:SMARTSYNC_EMAIL = "seu-email-de-teste"
   $env:SMARTSYNC_SENHA = "sua-senha-de-teste"
   ```

3. Execute:

   ```bash
   python automacao.py
   ```

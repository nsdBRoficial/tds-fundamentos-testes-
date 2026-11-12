# 🎓 Tutorial Mastigado: Como Fazer a Atividade de Testes (Sem Mistério!)

E aí, pessoal! Esse guia aqui é o **passo a passo bem mastigado** para você conseguir fazer a atividade de hoje do começo ao fim sem travar. Se seguir na ordem, vai dar tudo certo! 🚀

---

## 🤔 1. Qual é a ideia da atividade?

A gente tem um arquivinho Python chamado `exercicio.py` que faz três coisas simples:
1. `calcular_media(notas)` → Calcula a média de uma lista de notas (de 0 a 10).
2. `classificar_aluno(media)` → Diz se o aluno está `"Aprovado"`, em `"Recuperação"` ou `"Reprovado"`.
3. `dividir_premio(valor_total, participantes)` → Divide um prêmio em dinheiro entre várias pessoas.

O seu trabalho hoje **não é** mudar o `exercicio.py`!
O seu trabalho é:
1. Criar um arquivo só seu dentro da pasta `respostas/`.
2. Responder **3 perguntas** sobre testes (com as suas palavras, em formato de comentário `#`).
3. Escrever **3 testes usando `assert`** para provar que o código funciona (e também falha do jeito certo quando recebe coisa errada).
4. Mandar tudo por **Pull Request (PR)** no GitHub.

---

## 💻 2. Baixando o projeto e criando sua branch

Abra o terminal (PowerShell, Git Bash ou o terminal do VS Code) e rode um comando de cada vez:

```bash
# 1. Baixa o projeto do GitHub para o seu computador
git clone https://github.com/nsdBRoficial/tds-fundamentos-testes.git

# 2. Entra na pasta do projeto
cd tds-fundamentos-testes

# 3. Cria uma branch só sua (troque "joao" pelo seu nome, sem espaços!)
git checkout -b entrega-joao
```

> 💡 **Dica de ouro:** Nunca trabalhe direto na branch `main`! Criar a branch `entrega-seu-nome` garante que você não vai bagunçar o trabalho dos colegas.

---

## 📄 3. Criando o seu arquivo de resposta

Dentro da pasta `respostas/`, crie um arquivo chamado `resposta_<seu_nome>.py` (exemplo: `respostas/resposta_joao.py`).

Copie e cole o modelo que está lá no [README.md](README.md) dentro desse arquivo novo.

---

## ✍️ 4. Preenchendo a Parte 1 (Teoria)

No começo do arquivo tem 3 perguntas comentadas com `#`. Você só precisa escrever a sua resposta logo abaixo de cada `# Resposta:`:

```python
# 1. Por que não devemos confiar apenas em testes manuais executados no terminal?
# Resposta: Porque testar na mão toda hora cansa, a gente esquece casos importantes e, quando o código cresce, fica impossível testar tudo de novo manualmente.
```

> 💡 **Sem neura:** Escreva com as suas palavras, do jeito que você entendeu! O importante é mostrar que você pegou a ideia.

---

## 🧪 5. Entendendo e rodando a Parte 2 (Os testes com `assert`)

O `assert` é tipo um fiscal: você diz *"eu espero que isso aqui dê X"*.
- Se der X mesmo → ele fica quietinho e passa para a próxima linha.
- Se NÃO der X → ele trava o programa na hora e mostra a mensagem de erro que você escreveu!

No seu arquivo, você vai testar 3 situações:
1. **Caminho Feliz:** tudo certinho, notas `[6.0, 8.0]` tem que dar média `7.0`.
2. **Casos de Borda:** bem na linha de corte! Média `7.0` exata aprova? Média `5.0` exata deixa em recuperação?
3. **Tratamento de Exceção:** se tentar dividir um prêmio por `0` pessoas, o código tem que dar `ZeroDivisionError` (e não quebrar de forma estranha).

Para rodar o seu arquivo e ver se passou, digite no terminal:

```bash
python respostas/resposta_joao.py
```

*(Lembrando: troque `joao` pelo seu nome!)*

Se aparecer:
```text
Iniciando testes...
✅ Todos os testes passaram com sucesso!
```
**Deu bom!** Pode partir para a entrega! 🎉

---

## 🚀 6. Enviando para o GitHub (Commit + Push + Pull Request)

Agora vamos salvar e mandar a sua branch para o GitHub:

```bash
# 1. Adiciona o seu arquivo novo
git add respostas/resposta_joao.py

# 2. Salva (commita) com uma mensagem clara
git commit -m "docs e testes: entrega teorica de joao"

# 3. Envia a sua branch para o GitHub
git push origin entrega-joao
```

Depois do `git push`:
1. Abra o repositório no navegador: `https://github.com/nsdBRoficial/tds-fundamentos-testes`
2. Vai aparecer um botão verde **"Compare & pull request"** — clique nele!
3. Coloque o título do PR assim: `[ENTREGA] - Seu Nome` (ex: `[ENTREGA] - João Silva`).
4. Clique em **"Create pull request"**.

Pronto! Atividade entregue! 👏


# 365 • Fé para cada dia

Aplicativo web de Bergues Travassos, preparado para GitHub Pages, inclusive em endereços com subpasta.

## Recursos

- 365 devocionais, contexto bíblico, aplicação e oração.
- 12 roteiros temáticos de estudo.
- Busca, filtros por mês, favoritos e progresso de leitura.
- Anotações com salvamento automático e backup JSON.
- Tema claro e escuro, ajuste de texto e layout responsivo.
- Seleção dos 66 livros e capítulos para abrir a ARA no YouVersion.

## Publicar no GitHub Pages

1. Extraia este ZIP e crie um repositório chamado `365-devocionais`, com branch `main`.
2. Envie o conteúdo desta pasta para a raiz do repositório, incluindo `.github/workflows/pages.yml`, `dist/` e `scripts/`. Envie os arquivos extraídos, não o ZIP nem uma pasta extra envolvendo o projeto.
3. Abra **Settings > Pages > Build and deployment > Source** e selecione **GitHub Actions**.
4. Abra **Actions > Publicar aplicativo no GitHub Pages > Run workflow**, selecione `main` e execute.
5. Após o sucesso, o endereço aparece no job `deploy` e em **Settings > Pages**. Os próximos envios para `main` publicam automaticamente.

No plano gratuito, use repositório público. A disponibilidade para repositórios privados depende do plano da conta. Se a primeira execução falhar antes de ativar Pages, conclua o passo 3 e execute novamente. Se usar outra branch, ajuste `branches: [main]` no workflow.

Documentação oficial: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## Enviar pelo Git no computador

Abra o terminal nesta pasta:

```sh
git init
git branch -M main
git add .
git commit -m "Preparar aplicativo 365 Devocionais para GitHub Pages"
```

Na página do repositório criado, copie e execute o comando `git remote add origin` que o próprio GitHub apresenta. Em seguida:

```sh
git push -u origin main
```

Autentique pela sua conta. Nenhuma chave, senha ou token pessoal deve ser colocado no código.

## Executar localmente

```sh
python3 -m http.server 8000 --directory dist
```

Abra http://localhost:8000. O aplicativo carrega os devocionais por `fetch`, então não abra o HTML por duplo clique.

## Validar

```sh
python3 scripts/validate.py
node --check dist/app.js
```

Não há dependências para instalar nem compilação. O workflow verifica o projeto e publica `dist/`.

## Traduções e fontes

Os botões bíblicos abrem a Almeida Revista e Atualizada, ARA, no YouVersion em outra aba. O texto integral da ARA não está incluído no projeto. Os versículos das meditações continuam identificados como JFA, edição de 1911, conforme o livro original. Não foram rotulados como ARA.

O conteúdo vem do livro “365 Dias de Sabedoria, Fé e Domínio Próprio”, de Bergues Travassos. As referências estão em `dist/fontes.json` e na tela Sobre.

## Anotações, privacidade e mudança de endereço

Favoritos, progresso e notas ficam no navegador e dispositivo. Não há login nem sincronização. Quem utiliza o mesmo perfil de navegador consegue acessar as notas.

Os dados ficam vinculados ao endereço do aplicativo. Antes de mudar do endereço atual para o GitHub Pages, exporte o backup em Anotações no aplicativo antigo. Depois restaure-o no aplicativo novo. Faça o mesmo antes de trocar de aparelho, limpar o navegador ou mudar o domínio.

A leitura bíblica externa requer conexão. Não há cache offline, mesmo ao criar um atalho na tela inicial.

## Organização

| Arquivo | Função |
| --- | --- |
| `dist/index.html` | Entrada e estrutura |
| `dist/app.js` | Navegação e funções |
| `dist/style.css` | Estilos e adaptação às telas |
| `dist/devocionais.json` | 365 devocionais |
| `dist/fontes.json` | Referências do livro |
| `dist/manifest.webmanifest` | Identificação como aplicativo web |
| `.github/workflows/pages.yml` | Publicação automática |
| `scripts/validate.py` | Validação do pacote |

## Direitos

Conteúdo devocional de Bergues Travassos. Não foi atribuída licença de código aberto. Consulte `DIREITOS.md`. Aplicativo independente, sem vínculo oficial com o YouVersion, a Sociedade Bíblica do Brasil ou a Igreja Adventista.

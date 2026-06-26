# abnercopadomundo2ds

Site simples sobre a Copa do Mundo, com páginas estáticas por ano mostrando campeão e vice-campeão.

Como executar localmente

1. Abra um terminal na pasta do projeto.
2. Inicie um servidor HTTP simples (Python 3):

```bash
python3 -m http.server 8000
```

3. Abra no navegador: `http://localhost:8000` ou use o comando:

```bash
$BROWSER http://localhost:8000
```

Páginas disponíveis

- 1930.html
- 1934.html
- 1938.html
- 1950.html
- 1954.html
- 1958.html
- 1962.html
- 1966.html
- 1970.html
- 1974.html
- 1978.html
- 1982.html
- 1986.html
- 1990.html
- 1994.html
- 1998.html
- 2002.html
- 2006.html
- 2010.html
- 2014.html
- 2018.html
- 2022.html

Contribuições

Sinta-se à vontade para editar ou abrir issues com melhorias.

Gerar páginas automaticamente

Se preferir gerar (ou atualizar) as páginas a partir dos dados em JSON, use o script:

```bash
python3 scripts/generate_pages.py
```

Requisitos: Python 3 (já incluso na maioria dos sistemas). O script escreve os arquivos `YYYY.html` na raiz do projeto a partir de `data/worldcups.json`.

Validação HTML

Para checar a validade HTML localmente, instale `tidy` e rode:

```bash
tidy -e *.html
```



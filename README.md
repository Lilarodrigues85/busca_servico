# Busca Serviço

Este projeto realiza uma busca automática por serviços específicos, usando **RPA** para automatizar tarefas de pesquisa e coleta de dados de plataformas de serviço. A aplicação foi desenvolvida com **Python** e **Selenium** para navegar e extrair informações automaticamente, salvando os resultados em um arquivo JSON para fácil acesso e análise.

## Índice
- [Sobre o Projeto](#sobre-o-projeto)

## Sobre o Projeto
O projeto foi desenvolvido com o objetivo de otimizar a pesquisa por serviços específicos, poupando tempo e facilitando a análise de resultados. A ferramenta coleta informações relevantes e organiza tudo em um arquivo JSON. Pode ser configurado para buscar diferentes tipos de serviços e informações, tornando-o flexível para várias necessidades.

### Objetivos
- Automatizar a pesquisa de serviços em plataformas.
- Exportar os resultados em um arquivo JSON para fácil análise e manipulação.
- Permitir configurações personalizadas de pesquisa, como tipo de serviço e localização.

## Pré-requisitos
- Python 3.6 ou superior
- Selenium
- Navegador Chrome (ou outro navegador compatível)
- [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) (ou driver correspondente ao seu navegador)

## Instalação
Clone o repositório e instale as dependências:
```bash
git clone https://github.com/Lilarodrigues85/busca_servico.git
cd busca_servico
pip install -r requirements.txt

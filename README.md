# SymCare - Sistema de Autoatendimento Farmacêutico

Sistema web desenvolvido em Python/Flask para autoatendimento em farmácias, permitindo que usuários busquem medicamentos por sintomas ou nome, visualizem recomendações e realizem pagamentos.

## Funcionalidades

- Busca de medicamentos por nome
- Recomendações baseadas em sintomas
- Sistema de pagamento integrado
- Interface moderna e responsiva
- Visualização de ofertas
- Categorias populares de medicamentos

## Tecnologias Utilizadas

- Python 3.13
- Flask
- NumPy
- Pandas
- Bootstrap 4
- Font Awesome
- jQuery

## Estrutura do Projeto

```
projeto/
├── app.py              # Aplicação Flask principal
├── models/
│   └── symcare.py     # Lógica do sistema
├── static/
│   └── css/
│       └── style.css  # Estilos personalizados
└── templates/         # Templates HTML
    ├── base.html     # Template base
    ├── index.html    # Página inicial
    ├── buscar.html   # Busca de medicamentos
    ├── recomendacao.html  # Recomendações
    └── pagamento.html     # Página de pagamento
```

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/symcare.git
cd symcare
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
python app.py
```

O sistema estará disponível em `http://localhost:5000`

## Screenshots

[Adicionar screenshots do sistema aqui]

## Contribuição

Sinta-se à vontade para contribuir com o projeto. Abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
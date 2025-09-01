# SPLOVE - Acompanhantes de Luxo em São Paulo

Site moderno e responsivo para anúncio de acompanhantes de luxo em São Paulo, baseado no design do SPLOVE.

## 🚀 Características

- **Design Moderno**: Interface escura e elegante
- **Responsivo**: Otimizado para desktop, tablet e mobile
- **Performance**: Carregamento rápido e otimizado
- **Acessibilidade**: Navegação por teclado e leitores de tela
- **UX/UI**: Experiência do usuário intuitiva

## 📱 Funcionalidades

### Header
- Logo SPLOVE com destaque em laranja
- Ícones de navegação (filtro, pesquisa, perfil, menu)
- Menu hambúrguer para mobile

### Seções Principais
- **Modelos em Destaque**: Carrossel com 2 modelos principais
- **Stories**: Perfis circulares roláveis horizontalmente
- **Grid de Modelos**: Grade responsiva de modelos
- **Informações**: Texto sobre o serviço e tags
- **Footer**: Links organizados por categorias

### Interatividade
- Navegação suave entre seções
- Efeitos hover nos cards
- Gestos de toque para mobile
- Lazy loading de imagens
- Estados de carregamento

## 🛠️ Tecnologias

- **HTML5**: Estrutura semântica
- **CSS3**: Design responsivo com Grid e Flexbox
- **JavaScript**: Funcionalidades interativas
- **Fontes**: Inter (Google Fonts)
- **Ícones**: SVG inline

## 📁 Estrutura do Projeto

```
/
├── index.html          # Página principal
├── css/
│   └── style.css       # Estilos principais
├── js/
│   └── main.js         # JavaScript principal
├── img/
│   ├── models/         # Imagens das modelos
│   ├── stories/        # Imagens dos stories
│   └── news/           # Imagens das novidades
├── CNAME               # Configuração de domínio
└── README.md           # Documentação
```

## 🎨 Design System

### Cores
- **Primária**: #ff6b35 (Laranja)
- **Fundo**: #0a0a0a (Preto)
- **Superfície**: #1a1a1a (Cinza escuro)
- **Texto**: #ffffff (Branco)
- **Texto secundário**: #cccccc (Cinza claro)

### Tipografia
- **Família**: Inter
- **Pesos**: 300, 400, 500, 600, 700
- **Tamanhos**: 12px a 28px

### Breakpoints
- **Mobile**: < 480px
- **Tablet**: 480px - 768px
- **Desktop**: > 768px

## 🚀 Como Usar

1. Clone o repositório
2. Abra `index.html` no navegador
3. Para desenvolvimento, use um servidor local

### Servidor Local
```bash
# Python 3
python -m http.server 8000

# Node.js
npx serve .

# PHP
php -S localhost:8000
```

## 📱 Responsividade

O site é totalmente responsivo com:
- Layout adaptativo para diferentes telas
- Grid que se ajusta automaticamente
- Navegação otimizada para mobile
- Gestos de toque implementados

## 🔧 Personalização

### Adicionar Novas Modelos
1. Adicione a imagem em `img/models/`
2. Atualize o HTML com o novo card
3. O CSS se ajustará automaticamente

### Modificar Cores
Edite as variáveis CSS no arquivo `style.css`:
```css
:root {
  --primary-color: #ff6b35;
  --background-color: #0a0a0a;
  --surface-color: #1a1a1a;
}
```

## 📈 Performance

- **Lazy Loading**: Imagens carregam conforme necessário
- **Debounce**: Otimização de eventos de scroll
- **CSS Otimizado**: Estilos eficientes
- **JavaScript Modular**: Código organizado e eficiente

## 🔒 Segurança

- Validação de entrada
- Sanitização de dados
- Headers de segurança (quando implementado)

## 📞 Suporte

Para dúvidas ou sugestões, entre em contato através do repositório.

## 📄 Licença

Este projeto é privado e de uso exclusivo.

---

**Desenvolvido com ❤️ para SPLOVE**

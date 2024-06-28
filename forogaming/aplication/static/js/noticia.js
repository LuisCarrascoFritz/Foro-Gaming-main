// Definir la URL de la API y tu clave de API
const apiKey = '37f5a2d32cdc4718be682287dc5f5920';
const apiUrl = `https://newsapi.org/v2/top-headlines?country=us&category=gaming&apiKey=${apiKey}`;
// Función para obtener y mostrar noticias
async function getNews() {
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        const articles = data.articles;

        // Limpiar el contenido existente
        const newsContainer = document.getElementById('news');
        newsContainer.innerHTML = '';

        // Iterar sobre los artículos y mostrar cada noticia
        articles.forEach(article => {
            const { title, description, url, urlToImage } = article;

            const articleElement = document.createElement('div');
            articleElement.classList.add('article');

            articleElement.innerHTML = `
                <h2><a href="${url}" target="_blank">${title}</a></h2>
                <img src="${urlToImage}" alt="${title}">
                <p>${description}</p>
            `;

            newsContainer.appendChild(articleElement);
        });
    } catch (error) {
        console.error('Error al obtener noticias:', error);
    }
}

// Llamar a la función para obtener noticias cuando la página cargue
document.addEventListener('DOMContentLoaded', () => {
    getNews();
});
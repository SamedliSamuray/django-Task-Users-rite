const values = document.getElementsByTagName('h4');
const paragraphs = Array.from(values);

paragraphs.forEach(paragraph => {
    if (paragraph.textContent.includes("Messi")) {
        
        paragraph.style.color = 'goldenrod'; 
    }
});

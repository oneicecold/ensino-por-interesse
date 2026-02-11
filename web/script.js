document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('ibl-form');
    const topicInput = document.getElementById('topic');
    const interestInput = document.getElementById('interest');
    const generateBtn = document.getElementById('generate-btn');
    const btnText = generateBtn.querySelector('.btn-text');
    const loader = generateBtn.querySelector('.loader');
    
    const resultArea = document.getElementById('result-area');
    const resultTitle = document.getElementById('result-title');
    const resultContent = document.getElementById('result-content');
    const resetBtn = document.getElementById('reset-btn');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const topic = topicInput.value.trim();
        const interest = interestInput.value.trim();
        
        if (!topic || !interest) return;

        // UI Loading State
        setLoading(true);
        resultArea.classList.add('hidden');

        try {
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ topic, interest }),
            });

            if (!response.ok) {
                throw new Error('Erro na geração da aula');
            }

            const data = await response.json();
            
            // Display Result
            resultTitle.textContent = data.title;
            // Simple conversion of basic markdown symbols for better display
            // In a real app, use a library like marked.js
            resultContent.innerHTML = parseSimpleMarkdown(data.content);
            
            resultArea.classList.remove('hidden');
            form.classList.add('hidden');

        } catch (error) {
            alert('Ocorreu um erro ao gerar a aula. Tente novamente.');
            console.error(error);
        } finally {
            setLoading(false);
        }
    });

    resetBtn.addEventListener('click', () => {
        form.classList.remove('hidden');
        resultArea.classList.add('hidden');
        topicInput.value = '';
        interestInput.value = '';
        topicInput.focus();
    });

    function setLoading(isLoading) {
        generateBtn.disabled = isLoading;
        if (isLoading) {
            btnText.classList.add('hidden');
            loader.classList.remove('hidden');
        } else {
            btnText.classList.remove('hidden');
            loader.classList.add('hidden');
        }
    }

    function parseSimpleMarkdown(text) {
        if (!text) return '';
        
        let html = text
            // Bold (**text**)
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            // Italic (*text*)
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            // Headers (### Text)
            .replace(/^### (.*$)/gm, '<h3>$1</h3>')
            .replace(/^## (.*$)/gm, '<h2>$1</h2>')
            // Blockquotes (> Text)
            .replace(/^> (.*$)/gm, '<blockquote>$1</blockquote>')
            // Lists (- Item)
            .replace(/^- (.*$)/gm, '<li>$1</li>');
            
        return html;
    }
});

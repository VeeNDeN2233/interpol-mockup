document.addEventListener('DOMContentLoaded', () => {
    // Инициализация табов
    document.querySelectorAll('.tab-link').forEach(tab => {
        tab.addEventListener('click', function(e) {
            e.preventDefault();
            const tabId = this.dataset.tab;
            document.querySelectorAll('.tab-link').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            this.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });

    // Модальные окна
    const modalTriggers = document.querySelectorAll('[data-modal]');
    const modals = document.querySelectorAll('.modal-overlay');

    modalTriggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const modalId = trigger.dataset.modal;
            document

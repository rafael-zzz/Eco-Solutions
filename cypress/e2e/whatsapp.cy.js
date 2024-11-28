describe('template spec', () => {
  beforeEach(() => {
    // Acesse a página de login e autentique
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('#username').type('nong');
    cy.get('#password').type('nong');
    cy.get('.bg-green-600').click();
  });

  it('whatsapp link verification', () => {
    
    cy.get('.leaflet-marker-icon').first().click();

    
    cy.get('#whatsappLink').should('have.attr', 'href', 'https://wa.me/5581994382896');

    
    cy.get('#whatsappLink').then((link) => {
      const href = link.prop('href');
      expect(href).to.include('https://wa.me/5581994382896');
    });

    
    cy.get('#whatsappLink').should('have.attr', 'target', '_blank');
  });

  afterEach(() => {
    
  });
});

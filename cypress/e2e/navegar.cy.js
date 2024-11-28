describe('waze link verification', () => {
    beforeEach(() => {
      
      cy.visit('http://127.0.0.1:8000/login/');
      cy.get('#username').type('nong');
      cy.get('#password').type('nong');
      cy.get('.bg-green-600').click();
    });
  
    it('verifica o link do Waze', () => {
      
      cy.get('.leaflet-marker-icon').first().click();
  
      // Verifique se a URL contém os parâmetros necessários
      cy.get('#wazeLink').should('have.attr', 'href').and('include', 'll=-8.03656,-34.921494');
      cy.get('#wazeLink').should('have.attr', 'href').and('include', 'navigate=yes');
  
      // Verifique se o link está configurado para abrir em uma nova aba
      cy.get('#wazeLink').should('have.attr', 'target', '_blank');
    });
  
    afterEach(() => {
     
    });
  });
  
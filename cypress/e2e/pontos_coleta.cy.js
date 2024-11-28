describe('template spec', () => {
    beforeEach(() => {
      cy.visit('http://127.0.0.1:8000/login/')
      cy.get('#username').type('nong')
      cy.get('#password').type('nong')
      cy.get('.bg-green-600').click()
    })
  
    it('pontos de coleta', () => {
        cy.get('.leaflet-marker-icon').first().click();
        cy.get('#localendereco').should('have.text', 'Propriedade de São João, 200')
        
      
    })
    afterEach(() => {
      
      
    })
  })
  
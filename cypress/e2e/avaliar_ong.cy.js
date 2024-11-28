describe('template spec', () => {
    beforeEach(() => {
      cy.visit('http://127.0.0.1:8000/login/')
      cy.get('#username').type('nong')
      cy.get('#password').type('nong')
      cy.get('.bg-green-600').click()
    })
  
    it('avaliar ong', () => {
        cy.get('.leaflet-marker-icon').first().click();
        cy.get('.justify-between > .bg-yellow-500').click();
        cy.get(':nth-child(5) > .form-radio').click();
        cy.get('.space-x-2 > .bg-yellow-500').click();
        cy.get('.leaflet-marker-icon').first().click();
        cy.get('#localNota').should('have.text', 'Nota: 5.0/5')
      
    })
    afterEach(() => {
      
      
    })
  })
  
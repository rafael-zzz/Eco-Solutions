describe('template spec', () => {
    beforeEach(() => {
      cy.visit('http://127.0.0.1:8000/login/')
      cy.get('#username').type('teste_ong')
      cy.get('#password').type('teste_ong')
      cy.get('.bg-green-600').click()
      cy.get(':nth-child(5) > .p-4').click()
      cy.get('#tipo').type('meias')
      cy.get('#quantidade').type('10')
      cy.get('#peso').type('20')
      cy.get('#descricao').type('meia fedorenta')
      cy.get('#addResiduForm > form > .px-4').click()
      cy.get(':nth-child(7) > .p-4').click()
      cy.visit('http://127.0.0.1:8000/mapa/')
      
    })
  
    it('checar capacidade', () => {
        cy.get('.leaflet-marker-icon').first().click();
        cy.get('#capacidadeText').should('have.text', 'Capacidade: 20 / 200')

      
      
    })
    afterEach(() => {
    cy.get('[href="/ong/2/"]').click();
    cy.get(':nth-child(6) > .p-4').click();
    cy.get('.bg-red-600').click()
      
    })
  })
  
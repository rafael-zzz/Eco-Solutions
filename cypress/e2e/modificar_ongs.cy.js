describe('template spec', () => {
    beforeEach(() => {
      cy.visit('http://127.0.0.1:8000/admin/')
      cy.get('#id_username').type('admin')
      cy.get('#id_password').type('admin')
      cy.get('.submit-row > input').click()
    })
  
    it('modificar ong', () => {
        cy.get('.model-ong > :nth-child(3) > .changelink').click();
        cy.get(':nth-child(2) > .field-__str__ > a').click();
        cy.get('#id_nome').clear().type('Doe nunca');
        cy.get('.default').last().click();
        cy.get(':nth-child(2) > .field-__str__ > a').should('have.text', 'Doe nunca');
        

        

       
      
    })
    afterEach(() => {
        cy.get(':nth-child(2) > .field-__str__ > a').click();
        cy.get('#id_nome').clear().type('Doe agora');
        cy.get('.default').last().click();

      
      
    })
  })
  